import json
from EmQuantAPI import *
from datetime import timedelta, datetime
import time

loginResult = c.start("ForceLogin=1")

if(loginResult.ErrorCode != 0):
	print("login in fail")
	exit()

shares=[]
with open("shareData.json", "r") as json_file:
	shares=json.load(json_file)

macd={};
for share in shares:
	macd[share]=[]

with open("macdData.json", "w") as macd_file:
	macd_file.write(json.dumps(macd))
	