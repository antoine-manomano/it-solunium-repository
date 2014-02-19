#!/usr/bin/python
# -*- coding: UTF-8 -*-
# greenBird description

# Libraries
#from bs4 import BeautifulSoup
#import urllib
import mechanize
import os
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def verifadrmail(ch):
    """verifie la syntaxe d'une adresse mail donnée sous forme de chaine"""
    # extraction de l'adresse même dans le cas 'yyyyy <xxxx@xxxx.xxx>' 
    motif = r"^[^<>]*<([^<>]+)>$|(^[^<>]+$)"
    a = re.findall(motif, ch.strip())
    if len(a)>0:
        adr = ''.join(a[0]).strip()
    else:
        adr = ''
    # vérification de syntaxe de l'adresse mail extraite
    if adr=='':
        return False
    else:
        motif = r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
        return re.match(motif, adr)!=None
    


try:
    fdesc = open("emails.list", "r")


    for line in fdesc.readlines() :
        
        # Declarations
        onlineAnonyMailServiceUrl = 'http://anonymail.info/compose.html'
        #onlineAnonyMailServiceUrl = 'http://www.anonymousend.com/fr/'
        nomExpediteur = 'Person of interest'
        mailTo = str(line.strip())
        mailFrom = "personofinterest@gmail.com" 
        mailSubject = "Rapport Activité mois de 01/2014"
        mailMessage = """
                      Bonne réception
                      Veuillez croire à mes meilleures salutations
                      
                      PS: Rapport à l'adresse : http://bit.ly/1nKpuKF
                      POF
                      -------
                      Responsable systèmes informatiques"""
      
        br_bot = mechanize.Browser();
        try :
                        
            br_bot.set_proxies({"http": "localhost:8118"})
            reponse_Connect = br_bot.open(onlineAnonyMailServiceUrl)
        
            
            if reponse_Connect.code == 200 :
                if mailTo == "":
                    print bcolors.FAIL +  "Adresse mail vide - Annulation" + bcolors.ENDC
                
                elif verifadrmail(mailTo) == False :
                        print bcolors.FAIL +  "Adresse mail invalide (%s) - Annulation" %mailTo + bcolors.ENDC
                else :
                            print "Get page - OK"
                            br_bot.select_form(nr=0)
                            print "Select Form - OK "
                            #http://www.anonymousend.com/fr/
                            #br_bot.form['Nom'] = nomExpediteur
                            #br_bot.form['Email'] = mailTo
                            #br_bot.form['Object'] = mailSubject
                            #br_bot.form['Message'] = mailMessage
                            
                            #http://anonymail.info/compose.html
                            br_bot.form['email'] = mailFrom
                            br_bot.form['dest'] = mailTo
                            br_bot.form['subject'] = mailSubject
                            br_bot.form['msg'] = mailMessage
                            
                            reponse = br_bot.submit()
                            print "server answer : "
                            mail_sent = reponse.read() 
                            #if "Email envoyé avec succès." in str(mail_sent):
                            if "The  email has successfully sent !" in str(mail_sent):
                                print "Email envoyé avec succès à: "
                                print bcolors.WARNING + mailTo + bcolors.ENDC
                            else :
                                print "Le serveur a répondu : "+ str(reponse_Connect.code)
                                print str(mail_sent)
                    
        except Exception as im:
            if "Name or service not known" in str(im):
                #print im
                print "\n Service mail injoignable : (Ex: Name or service not known)\n"
                print "    1-Vérifiez votre connexion\n"
                print "    2-Vérifiez si ce service mail est joignable\n"
            else :
                print "Exception :" + str(im)
    
    fdesc.close()

except Exception as im:
    if "No such file or directory" in str(im):
        print "\n Fichier emails.list innexistant \n"
    