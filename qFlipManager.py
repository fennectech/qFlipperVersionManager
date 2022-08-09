#!/usr/bin/python
from requests import get
import wget
import os
import json

def start(filename):
	os.system("./"+filename)
	
url = 'https://update.flipperzero.one/qFlipper/directory.json'
request = get(url)
data = dict(request.json())
link = data["channels"][2]["versions"][0]["files"][2]["url"]
filename = link.split("/")[-1]

if not os.path.exists(filename):
	print("New version available")
	print("Deleting previous version...")
	os.system("rm ./*.AppImage")
	print("Downloading...")
	wget.download(link, filename)
	print("Setting things up...")
	os.system("chmod +x "+filename)
	print("Starting...")
start(filename)
