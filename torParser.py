#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Ce bout de code permet de changer d'identité en utilisant Tor (IP), sans utiliser la librairie TorCtrl
# Tout en l'intégrant dans un code Pyhthon. (Développé à titre éducationnel

import socket
import urllib2


class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    
class texte:
    APPLICATION_Header = bcolors.WARNING
    APPLICATION_Header += "Ce bout de code permet de changer d'identité en utilisant Tor (IP) \r\n"
    APPLICATION_Header += "              (Développé à titre éducationnel) \r\n"
    APPLICATION_Header += "__________________________________________________________________ \r\n"
    APPLICATION_Header += bcolors.ENDC 



print "\r\n" + texte.APPLICATION_Header ;
proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
print "Adresse IP avant le 1er changement"
ip_before = urllib2.urlopen("http://www.ifconfig.me/ip").read()
print bcolors.OKBLUE + "IP = %s" %ip_before + bcolors.ENDC

try:
    tor_ctrl = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tor_ctrl.connect(("127.0.0.1", 9051))
    tor_ctrl.send('AUTHENTICATE "{}"\r\nSIGNAL NEWNYM\r\n'.format("your_password"))
    response = tor_ctrl.recv(1024)
    print "Réponse du port de contrôle Tor:"
    print response
    if response != '250 OK\r\n250 OK\r\n':
        print('Réponse innatendue du port de contrôle de Tor: {}\n'.format(response))
                
        
    else :
        print "Après le 1er changement"
        ip_after = urllib2.urlopen("http://www.ifconfig.me/ip").read()
        print bcolors.OKGREEN + "IP = %s" %ip_after + bcolors.ENDC
        print "Changement effectué avec succès."
        
        
        
except Exception, e:
    print('Erreur de connexion sur le port de contrôle de Tor: {}\n'.format(repr(e)))
    
    