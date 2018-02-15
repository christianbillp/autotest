FROM ubuntu:16.04

# Create folder for application
RUN mkdir /app

# Update apt sources and extra programs (python:slim)
RUN apt update
RUN apt install -y git bash python3 python3-pip nano vim screen microcom

# Dependency for serial communication
RUN pip3 install pyserial

# Add and run application
ADD application.py /app/application.py

# Run application at startup
#CMD [ "python", "/app/application.py" ]
