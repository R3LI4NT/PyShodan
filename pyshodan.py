#!/usr/bind/env python
#_*_ coding: utf8 _*_

from banner.banner import banner
import importlib,sys
from shodan import Shodan
import os
import time

importlib.reload(sys)
PYTHONIOENCODING="UTF-8"  
api_key = "wi4b5Pb398kxwLMIUt9opzaVpLmOydwT"
motor = Shodan(api_key)

banner()
print("\ntype \033[1;34mauto\033[0m or \033[1;34mmanual\033[0m to start.")


def auto():
	try:
		search = input("\n(shodan\033[1;37m@\033[1;34mauto\033[0m) >>> ")
		query = motor.search(search)
		print("\nTotal number of results: \033[1;37m{}\033[0m".format(query['total']))
		for host in query['matches']:
			print(" ")
			print("\033[1;37m-\033[0m" * 30)
			print("\n\033[1;34mIP:\033[0m {}".format(host['ip_str']))
			print("\033[1;34mPort:\033[0m {}".format(host['port']))
			print("\033[1;34mOrganization:\033[0m {}".format(host['org']))
			try:
				print("\033[1;34mASN:\033[0m {}".format(host['asn']))
			except:
				print("Unknown")
			for list_h in host['location']:
				print(f"\033[1;34m{list_h}:\033[0m " + str(host['location'][list_h]))	
			print("")	
	except:
		print("Ocurrio un error")


def manual():
	ip = input("\n(shodan\033[1;37m@\033[1;34mmanual\033[0m) >>> ")
	motor = Shodan(api_key)
	host = motor.host(ip)
	print('''\n\033[1;34mIP:\033[0m {} \n\033[1;34mPorts:\033[0m {} \n\033[1;34mCity:\033[0m {} \n\033[1;34mISP:\033[0m {} \n\033[1;34mOrganization:\033[0m {}
	'''.format(host['ip_str'],host['ports'],host['city'],host['isp'],host['org']))

def restart():
    if input("\033[1;37mBack to main menu \033[0;32my\033[1;37m/\033[0;31mn\033[0;m\033[0m\n>>> ").upper() != "Y":
        time.sleep(1)
        os.system("clear")
        banner()
        exit(0)

    os.system('python3 pyshodan.py')


option = input("(\033[1;37mShodan\033[0m) >>> ")

if option == 'auto':
	os.system("clear")
	banner()
	auto()
	restart()

elif option == 'manual':
	os.system("clear")
	banner()
	manual()
	restart()





