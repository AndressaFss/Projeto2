#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
acao=var.split("=")[0]

import os

print("content-type: text/html")
print("")

if acao == "Iniciar":
        os.system("date >> /var/www/html/cgi-bin/serv.log")
        os.system("sudo /var/www/html/cgi-bin/serv.log bind9 start &>> /var/www/html/cgi-bin/serv.log")
        print "<h1>Start OK</h1>"
elif acao == "Parar":
        os.system("date >> /var/www/html/cgi-bin/serv.log")
        os.system("sudo /var/www/html/cgi-bin/serv.log bind9 stop &>> /var/www/html/cgi-bin/serv.log")
        print "<h1>Stop OK</h1>"
elif acao == "Reiniciar":
        os.system("date >> /var/www/html/cgi-bin/serv.log")
        os.system("sudo /var/www/html/cgi-bin/serv.log bind9 restart &>> /var/www/html/cgi-bin/serv.log")
        print "<h1>Restart OK</h1>"
#elif acao == "Status":
#        os.system("date >> /var/www/html/cgi-bin/serv.log")
#        os.system("sudo /var/www/html/cgi-bin/serv.log bind9 restart &>> /var/www/html/cgi-bin/serv.log")
#       print "<h1>Status</h1>"
elif acao == "IniciarNag":
        os.system("date >> /var/www/html/cgi-bin/serv.log")
        os.system("sudo /var/www/html/cgi-bin/serv.log nagios3 start &>> /var/www/html/cgi-bin/serv.log")
        print "<h1>Start OK</h1>"
elif menu == "PararNag":
        os.system("date >> /var/www/html/cgi-bin/serv.log")
        os.system("sudo /var/www/html/cgi-bin/serv.log nagios3 stop &>> /var/www/html/cgi-bin/serv.log")
        print "Stop OK"
elif menu == "ReiniciarNag":
        os.system("date >> /var/www/html/cgi-bin/serv.log")
        os.system("sudo /var/www/html/cgi-bin/serv.log nagios3 restart &>> /var/www/html/cgi-bin/serv.log")
        print "<h1>Restart OK</h1>"
#elif acao == "Status":
#        os.system("date >> /var/www/html/cgi-bin/serv.log")
#        os.system("sudo /var/www/html/cgi-bin/serv.log nagios3 restart &>> /var/www/html/cgi-bin/serv.log")
#       print "<h1>Status</h1>"
