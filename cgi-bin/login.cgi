#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
usuario=var.split("&")[0].split("=")[1]
senha=var.split("&")[1].split("=")[1]

print("content-type: text/html")
print("")

if usuario == "admin" and senha == "123":
        f = open("site/menu.html","r")
        arquivo = f.read()
        f.close()
        print(arquivo)
else:
        print("<h1>Login Falhou</h1>")
