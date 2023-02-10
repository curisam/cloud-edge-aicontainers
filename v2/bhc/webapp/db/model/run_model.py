import os
import sqlite3
import schedule
import time
import base64

import re


def get_input(host, path, conn):

    img_list = os.listdir(path)
    encoded_list = []
    data = []

    for f in img_list:
        print(f)
        # img_path = (path+'/'+f)
        tmp = []

        # with open(img_path, 'rb') as img:
        #     base64_str = base64.b64encode(img.read())
        #     encoded_list.append(base64_str)

        tmp.append(round(time.time()))
        tmp.append(host)
        tmp.append(f)
        # tmp.append(base64_str)

        tmp = tuple(tmp)
        data.append(tmp)
    
    cur = conn.cursor()
    query = "insert or ignore into input_image values(?,?,?);"
    cur.executemany(query, data)
    conn.commit()



def get_pred(playbook, hosts_file, host, conn):
    
    os.system("ansible-playbook {playbook} -l {host_name} -i {hosts_file} -t pred > tmp/predlog.txt".format(playbook=playbook, host_name=host, hosts_file=hosts_file))

    rows = []
    p_start = re.compile('Prediction :.+')
    p_end = re.compile('PLAY RECAP.+')

    with open ("tmp/predlog.txt", 'r') as f:
        lines = f.readlines()

        for line in lines:
            start = p_start.search(str(line))

            if start:
                idx = lines.index(line)
                run = True

                while run:
                    ## drop no-useful strings and characters
                    lines[idx] = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s\.]", "", lines[idx])
                    lines[idx] = re.sub("\n", "", lines[idx])
                    lines[idx] = re.sub("n\d+", "", lines[idx])

                    rows.append(lines[idx])
                    ## search end of task
                    end = p_end.search(lines[idx])

                    idx += 1

                    if end:
                        run = False
                        

    data = rows[0].split()
    data = data[1:]
    cls = data[0::2]
    data = data[1::2]

    nodes = []

    ## load current nodes info from hosts table
    con = conn
    cur = con.cursor()
    cur.execute('select name from nodes where type = "builder"')
    tmp = cur.fetchall()

    ## save node lists
    for node in tmp:
        node = list(node)
        node = str(node)
        node = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", node)
        nodes.append(node)
        
    now = round(time.time())
    log = []

    for i in range(len(cls)):
        tmp = []
        tmp.append(now)
        tmp.append(nodes[0])
        tmp.append(cls[i])
        tmp.append(data[i])
        tmp = tuple(tmp)
        log.append(tmp)

    ## insert data into DB
    query = "insert into modelpred values(?,?,?,?);"
    cur.executemany(query, log)
    con.commit()

    ## show result
    cur.execute('select * from modelpred')
    out = cur.fetchall()

    for col in out:
        print(col)



if __name__ == "__main__":

    host = 'rpi6402'
    path = '/var/www/html/tmp'
    conn = sqlite3.connect('../edge_logs.db3')

    get_input(host, path, conn)