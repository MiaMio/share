def judgeLeave(data):
	print("comin leave")
	top=[]
	judge=1
	if data[1]<data[0]:
		# print("comin 04")
		top.append(data[0])

	for i in range(1, len(data)-1):
		if data[i]>data[i-1] and data[i]>data[i+1]:
			top.append(data[i])
	# print("top", end=": ")
	# print(top)
	if len(top)==1 or len(top)==0:
		return False
	for i in range(1, len(top)):
		if top[i]<top[i-1]:
			# print("comin041")
			judge=0
			break
	print(judge)
	if judge==1:
		return False
	return True

def judgeGold(data):
	usefulList=[]
	i=len(data)-1
	while i>=0:
		if data[i]>0:
			usefulList.append(data[i])
			i-=1
		else:
			break
	usefulList.reverse()		
	if len(usefulList)==0:
		# print("comin 1")
		return False
	elif len(usefulList)==1:
		# print("comin 2")
		return True
	elif len(usefulList)==2:
		# print("comin 3")
		return False
	else:
		# print("comin 4")
		if judgeLeave(usefulList)==False:
			# print("comin 41")
			if usefulList[len(usefulList)-2]<usefulList[len(usefulList)-3] and usefulList[len(usefulList)-2]<usefulList[len(usefulList)-1]:
				# print("comin 411")
				return True
		return False

#data=[-1, -2, -0.001, 3, -0.005, -0.006]
#data=[1, 6, 2, 7, 2, 3]
#data=[1,2,4,7,6,4,5,3,2,5]
# if judgeGold(data)==True:
# 	print("True")
# else:
# 	print("Fasle")