#!/bin/python3
import requests
from lxml.html import fromstring
from colorama import Fore
import sys

def print_help():
	print(f"""
{Fore.CYAN}	
______                                  _      
|  _  \\                                | |     
| | | |_ __ _   _ _ __  _ __   ___   __| | ___ 
| | | | '__| | | | '_ \\| '_ \\ / _ \\ / _` |/ _ \\
| |/ /| |  | |_| | |_) | | | | (_) | (_| |  __/
|___/ |_|   \\__,_| .__/|_| |_|\\___/ \\__,_|\\___|
                 | |                           
                 |_|                             
{Fore.WHITE}
	
	Usage: 
		./drupnode.py <host> (<range>)
	Exemple:
		./drupnode.py https://example.com/node/ 20-100
	""")

if len(sys.argv) < 2:
	print_help()
	sys.exit(0)
if len(sys.argv) == 3:
	node_range = [int(sys.argv[2].split("-")[0]),int(sys.argv[2].split("-")[1])]
else:
	node_range = [1,100]

URL = sys.argv[1]
print(f"{Fore.YELLOW}[-] Using URL: {URL}<i> from {node_range[0]} to {node_range[1]}{Fore.WHITE}")
for i in range(node_range[0],node_range[1]):
	r = requests.get(f"{URL}{i}")
	if r.status_code != 404:
		if r.status_code == 403:
			color = Fore.RED
		elif r.status_code == 500:
			color = Fore.YELLOW
		elif r.status_code == 200:
			color = Fore.GREEN
		else:
			color = Fore.CYAN
		tree = fromstring(r.content)
		title = tree.findtext('.//title')
		print(f"[{color}{r.status_code}{Fore.WHITE}] {URL}{i} ({Fore.BLUE}{title}{Fore.WHITE})")
