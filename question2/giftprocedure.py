from que2 import CoupleObjectList,GiftObjectList
import csv, logging,math	

def gift():
	for cp in CoupleObjectList:
		if int(cp.boy.budget)< int(GiftObjectList[0].cost):
			cp.boy.budget = int(GiftObjectList[0].cost)
			#print(cp.boy.budget)
		if cp.boy.type == "Miser":
			miser(cp)
		elif cp.boy.type == "Generous":
			generous(cp)
		else:
			geek(cp)

def miser(cp):
	giftbudget = int(cp.girl.maintenance_budget)
	if giftbudget <  int(GiftObjectList[0].cost):
		giftbudget = int(GiftObjectList[0].cost)
	for i in GiftObjectList:
		#print(type(i.cost))
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			giftbudget-=int(i.cost)
 
def generous(cp):
	giftbudget = int(cp.boy.budget)
	for i in GiftObjectList:
		#print(int(i.cost))
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			giftbudget-=int(i.cost)



def geek(cp):
	t=0
	x=0
	luxurycost=100	
	giftbudget = int(cp.girl.maintenance_budget)
	for i in GiftObjectList:
		#print(i.cost)
		if giftbudget-int(i.cost)>=0:
			cp.gifts.append(i)
			giftbudget-=int(i.cost)
			t=t+1
		else:
			break

	for i  in range (t,len(GiftObjectList)):
		if GiftObjectList[i].type=="Luxury" and int(GiftObjectList[i].cost)< luxurycost:
			 luxurycost=int(GiftObjectList[i].cost)
			 x=i

	if (int(cp.boy.budget)-int(cp.girl.maintenance_budget) + giftbudget) >= luxurycost:
		cp.gifts.append(GiftObjectList[x])

