# -*- coding: utf-8 -*-
from socket import *
from Msg_header import Header
from Msg_body import send_data
import Msg
import socket
import sysv_ipc
import subprocess
from Msg_util import MsgUtil
import time
import socket
import os
import sys
import sys

if len(sys.argv) == 1:          # 옵션 없으면 도움말 출력하고 종료
  print "숫자로 된 옵션을 입력해 주세요"
  exit(1)
resolution = sys.argv[2]

share_acc_gyro_pitch =  sysv_ipc.SharedMemory(510, flags=01000,size = 15, mode=0600)
smp1 =sysv_ipc.Semaphore(22, flags=01000, mode=0600,initial_value = 1)


HOST = '172.24.1.1'
PORT = int(sys.argv[1])
BUFSIZE = 1024
ADDR = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('', 6001))
process  = subprocess.Popen(["python","ak.py"],stdout=subprocess.PIPE)
reqpem = 'redjakfl'
sock.sendto('난 클라이언트', (HOST,PORT))
now_time = 0
selec = 2
ID = "jhjh54"
PW = "1111"
EMAIL = "ssss@naver.com"
share_acc_gyro_pitch.attach()

while(True):
    s, addr = sock.recvfrom(1024)
    #print s
    #Req = MsgUtil.receive(sock)
    # data =  Req.Body.acc_gyro
    #print str(data)

    #tmp = s.replace(" ", "")
    tmp = s.replace(" ", "")
    tmp = tmp.ljust(14," ")

    smp1.acquire(20)
    share_acc_gyro_pitch.write(tmp)
    smp1.release()
    
   #sock.send("1")
    if process.poll() != None:
        print "child exit"
        break
sock.close()

