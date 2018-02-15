import serial
import time
import os

cap = 'Module-id:'
point = 'U-Boot>'
enter = '\r\n'.encode('utf-8')
device = '/dev/' + os.popen('ls /dev|grep USB').read().strip('\n')

with serial.Serial(device, 115200, timeout=0.1) as ser:
    print('Waiting to break into U-Boot')
    while True:
        line = ser.readline().decode('utf-8', 'ignore')#;print(line)
        if line.startswith(cap) == True:
            print("Attempting to break into U-Boot")
            ser.write(enter)
        if line.startswith(point) == True:
            print('Connected to U-Boot terminal')
            break

    commands = [b'printenv ipaddr\n', b'printenv serverip\n']
    for command in commands:
        ser.write(command)
        time.sleep(0.5)
    
        while ser.in_waiting:  # Or: while ser.inWaiting():
            print(ser.readline().decode('utf-8', 'ignore'))
