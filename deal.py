import json
from dealMACD import dealMACD

class deal:
	macdShare=[]
	maShare=[]
	result=[]
#	macd={}
	def judgeMACD(self):
		with open("macdData.json", "r") as macd_file:
			macd=json.load(macd_file)
		with open("shareData.json", "r") as share_file:
			shares=json.load(share_file)
		for share in shares:
			d=dealMACD()
			if d.judgeGold(macd[share]) is True:
				self.macdShare.append(share)

	def judgeMA(self):
		with open("maData.json", "r") as ma_file:
			ma=json.load(ma_file)
		with open("shareData.json", "r") as share_file:
			shares=json.load(share_file)
		for share in shares:
			if ma[share]["ma5"]>ma[share]["ma20"] and ma[share]["ma20"]>ma[share]["ma60"] and ma[share]["ma60"]>ma[share]["ma250"]:
				self.maShare.append(share)

	def strategy(self):
		with open("shareData.json", "r") as share_file:
			shares=json.load(share_file)
		for share in shares:
			if share in self.macdShare and share in self.maShare:
				self.result.append(share)

	def __init__(self):
		self.judgeMACD()
		self.judgeMA()

d=deal()
d.strategy()
print(d.result)