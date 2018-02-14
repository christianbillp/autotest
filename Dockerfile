FROM ubuntu 16.04

RUN apt update
RUN apt install -y git python3 microcom nano vim screen
