# Get IP and location from URL
#@shadowoff09


import socket
import os
import time
from ip2geotools.databases.noncommercial import DbIpCity

class color:
	Default  = "\033[39m"
	Yellow   = "\033[33m"

    

os.system('cls' if os.name == 'nt' else 'clear')

url = input("\nInsert a URL: ")
IP = socket.gethostbyname(url)
response = DbIpCity.get(IP, api_key='free')
time.sleep(1)

print(f'\n{color.Yellow}IP{color.Default}: ', IP)
print(f'{color.Yellow}City{color.Default}: ', response.city)
print(f'{color.Yellow}Region{color.Default}: ', response.region)
print(f'{color.Yellow}Country{color.Default}: ', response.country)
print(f'{color.Yellow}Latitude{color.Default}: ', response.latitude)
print(f'{color.Yellow}Longitude{color.Default}: ', response.longitude)
