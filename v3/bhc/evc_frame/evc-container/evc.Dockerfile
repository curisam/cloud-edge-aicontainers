FROM python:3.8.15

MAINTAINER keti <ethicsense@keti.re.kr>

WORKDIR /home/

## download scripts
ADD get-docker.sh .
ADD grafana_10.0.3_amd64.deb .

## EVC modules
ADD evc.tar.gz .

## set env
RUN apt-get update && apt-get install -y sudo
RUN chmod +w /etc/sudoers
RUN echo 'irteam ALL=(ALL) NOPASSWD:ALL' | tee -a /etc/sudoers
RUN chmod -w /etc/sudoers
RUN sudo apt-get install -y libgl1-mesa-glx
RUN sudo apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN apt-get install -y vim

RUN pip install ansible

RUN sh get-docker.sh
RUN sudo apt-get install -y adduser libfontconfig1
RUN sudo dpkg -i grafana_10.0.3_amd64.deb

RUN sudo apt-get install sqlite3
RUN pip install pysqlite3
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -N ""

RUN pip install pandas
RUN pip install opencv-python
RUN pip install gradio
RUN pip install ultralytics