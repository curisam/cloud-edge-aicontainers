#------------------------------------------------------
# vnv
#------------------------------------------------------

#!/bin/bash

# http://keticmr.iptime.org:22809

# <ubuntu> 
# $ sudo apt install speedtest-cli

# <rpi> 
# $ sudo pip3 install speedtest-cli

import os
import time
from model_selector import ModelSelection

def run(cmd, is_show=False):

    # import subprocess
    # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    # if(is_show):
    #     print(p.communicate())
    stream = os.popen(cmd)
    output = stream.read()

    if is_show:
        print( output )
        return output
    else:
        return None


def main(mode = 'baseline'):
    #----------------------------------
    # 프로세스를 시작합니다.
    #----------------------------------
    st_total = time.time() #---------------------

    if mode == 'baseline' or mode == 'advanced':
        print(f'[+] Start {mode} experiment')
    else:
        print(f'[-] error, there is no [{mode}] mode.')
        return
    #----------------------------------
    # 에지 디바이스의 상태정보를 얻습니다.
    #----------------------------------
    st_getstatus = time.time() #---------------------
    wdir = ' /home/jpark/WorkDevEdgeAI/cloud-edge-aicontainers/v2/vnv/mission2/'
    py = ' /usr/bin/python3'
    selected_model = 'resnet152' # default
    device = 'cuda'
    N = 10
    ask_pass_option = '' #  '--ask-become-pass'
    model_selector = ModelSelection()

    print( wdir )
    print( py )
    print( selected_model )
    print(' ')
    #cmd_sub = ' /usr/bin/python3 -c "import torch; print(torch.cuda.is_available())" '
    cmd = f'ansible vnv -m shell -a "cd {wdir}; {py} cuda_is_available.py " -i hosts.ini '
    z = run(cmd, True)
    print('z = ', z)

    if 'True' in run(cmd, True) : is_cuda_available = 1 
    else: is_cuda_available = 0
    print( 'is_cuda_available = ', is_cuda_available )

    # for ubuntu
    cmd = f'ansible vnv -m shell -a "cat /proc/cpuinfo" -i hosts.ini > ./tmp/baseline_cpuinfo.txt'
    run(cmd, False)

    cmd = f'cat ./tmp/baseline_cpuinfo.txt | grep "model name" '
    run(cmd, False)

    cmd = f'ansible vnv -m shell -a "cat /proc/meminfo" -i hosts.ini > ./tmp/baseline_meminfo.txt '
    run(cmd, False)

    cmd = f'cat ./tmp/baseline_meminfo.txt | grep "MemTotal" '
    run(cmd, False)

    et_getstatus = time.time() #---------------------

    #----------------------------------
    # 추론을 위한 AI 모델을 선택합니다.
    #----------------------------------
    
    st_modelselection = time.time() #---------------------
    if mode == 'baseline':
        selected_model = model_selector.greedModelSelection()
    elif mode == 'advanced':
        selected_model = model_selector.advancedModelSelection()

    print(f'mode = {mode}, selected_model = {selected_model}')
    et_modelselection = time.time() #---------------------
    

    #----------------------------------
    # 에지 디바이스에서 추론을 수행합니다. 
    #----------------------------------
    st_inference = time.time() #---------------------
    cmd = f'ansible vnv -i hosts.ini -m shell -a "cd {wdir}; pwd; {py} vnv03.py --model {selected_model} --device {device} --N {N};"  {ask_pass_option} ' 
    run(cmd, False)
    et_inference = time.time() #---------------------
    
    #---------------------------------------------------
    et_total = time.time()
    #---------------------------------------------------

    T = et_total - st_total
    
    title = 'Get status time'
    t = et_getstatus - st_getstatus
    ratio = t / T
    disp_time(title, t, ratio)
    
    title = 'Model selection time'
    t = et_modelselection - st_modelselection
    ratio = t / T
    disp_time(title, t, ratio)

    title = 'Inference time'
    t = et_inference - st_inference
    ratio = t / T
    disp_time(title, t, ratio)
    
    title = 'Total time'
    t = et_total - st_total
    ratio = t / T
    disp_time(title, t, ratio)

    print(f'[+] Done baseline experiment')


def disp_time(title, t, ratio):
    print(f'{t}, {ratio * 100} %, {title} ')



import sys
if __name__ == "__main__":
    
    # total arguments
    n = len(sys.argv)
    for i in range(1, n):
        print(sys.argv[i], end = " ")

    if n != 2:
        print('[-] argument error')
        print('    e.g. python3 run_vnv.py baseline')
        print('    e.g. python3 run_vnv.py advanced')
    main(sys.argv[1])

#------------------------------------------------------
# End of this file
#------------------------------------------------------
