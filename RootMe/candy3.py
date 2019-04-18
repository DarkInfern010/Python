# -*- coding: utf-8 -*-

import socket
import time
import codecs

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'irc.root-me.org' #irc server
PORT = 6667 #port
NICK = 'DarkInfern010'

print('soc created |', s)
remote_ip = socket.gethostbyname(HOST)
print('ip of irc server is:', remote_ip)


s.connect((HOST, PORT))

print('connected to: ', HOST, PORT)

nick_cr = ('NICK ' + NICK + '\r\n').encode()
s.send(nick_cr)
usernam_cr= ('USER megadeath megadeath megadeath :rainbow pie \r\n').encode()
s.send(usernam_cr)
time.sleep(1)
s.send('JOIN #root-me_challenge \r\n'.encode()) #chanel

go = True

while 1:
    data = s.recv(4096).decode('utf-8')
    print(data)
    if data.find('PING') != -1:
        s.send(str('PONG ' + data.split(':')[1] + '\r\n').encode())
        print('PONG sent \n')
    #endif
    if data.find('hi') != -1:
        s.send((str('PRIVMSG ' + data.split('!')[0][1:]) + ' Hi! \r\n').encode())

    if(go):
        s.send((str('PRIVMSG Candy !ep3 \r\n').encode()))
        go=False
    #endif

    if (data.find(':Candy!Candy@root-me.org PRIVMSG DarkInfern010 :') != -1):
        chaine = data.split(':')[2]
        envoie = codecs.encode(chaine, 'rot_13')
        s.send((str('PRIVMSG Candy !ep3 -rep ' + envoie + '\r\n').encode()))
        time.sleep(10)
s.close()