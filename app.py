'''
Author: Qi Han
Date: Apr.6.2020
'''
import random
import os
import sys

def ansCompare(stdAns, cstAns):
	
	return stdAns == cstAns

def orderGenerator(total):

	orderSet = -999
	return orderSet

def main():
	global total 
	settttt={}
	with open("test.txt") as fp:
		content = fp.readlines()
	for line in content:
		m = line
		if("total: " in m):
			word = line.split(' ')
			total = int(word[1])
			print("totallllll " , total)
			orderGenerator(total)
			continue
		if("CorrectAnswer: " in m):
			userInput = input("Your Answer: ")
			co = ansCompare(line[15], userInput)
			if(co):
				print("Your answer is correct!", end = " "),
				continue
			else:
				settttt.setdefault(line[17], []).append(line[19])
				print("Your answer is wrong!", end = " "),
				continue
		print(line)
	print("\n")
	repGenerate(settttt)
	fp.close()
	return None

def repGenerate(settttt):

	s = '{}{}{}'.format("This chapter has ", total, " units,") 
	for x in settttt:
		print(settttt.get(x))

		if("H" in settttt.get(x)):
			a = '{}{}{}'.format("at point: ", x, " you need high improvement")
		elif("M" in settttt.get(x)):
			a = '{}{}{}'.format("at point: ", x, " you need medium improvement")
		elif("L" in settttt.get(x)):
			a = '{}{}{}'.format("at point: ", x, " you need low improvement")
		s+=a
	print(s)

if __name__ == '__main__':

	main()


	