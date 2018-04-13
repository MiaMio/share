import json

macd={}
shares=[]
with open("closeData.json") as macd_file:
	macd=json.load(macd_file)
with open("shareData.json") as share_file:
	shares=json.load(share_file)

#i=0
for share in shares:
#	print(len(macd[share][0]))
	for m in macd[share][0]:
#		print(i)
#		i+=1
		if m is None:
			print(share)
			print(macd[share][0])
			break
#			exit()

#print("no None")