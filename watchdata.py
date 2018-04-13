import json

with open("macdData.json") as macd_file:
	macd=json.load(macd_file)
print(macd["000001.SZ"])