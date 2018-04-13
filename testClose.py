import json

with open("closeData.json", "r") as json_file:
	data=json.loads(json_file.read())
	print(data["000001.SZ"])
