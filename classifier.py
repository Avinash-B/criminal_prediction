"""
A python program for predicting if a person has chances of becoming a criminal using machine learning.

This can be done by using random forest method for it's prediction.
Number of parameters = 70
Subsample of each decision tree = 30
Total number of trees in the forest = 2000
Training set = 45718
Testing set = 11430
"""

import csv
import random
import numpy as np
from sklearn import tree

class classifier:
	def __init__(self,trainlist):
		self.trainlist = trainlist
	def test(self,ls):
		result = 0
		for i in range(0,2001):
			#30 for random subset from the dataset
			treelist = []
			treelist = random.sample(self.trainlist,30)
			treeresult = []
			for one in treelist:
				one.pop(0)
				treeresult.append(one.pop())
				for every in one:
					every = float(every)
			for every in treeresult:
				every = int(every)
			clf = tree.DecisionTreeClassifier()
			clf = clf.fit(treelist,treeresult)
			result+= clf.predict(ls)
		return result


if __name__ == "__main__":
	with open('criminal_train.csv') as trainfile:
		traindata = csv.reader(trainfile)
		trainlist = list(traindata)
		forest = classifier(trainlist)
		with open('criminal_test.csv') as testfile:
			testdata = csv.reader(testfile)
			testlist = list(testdata)
			for element in testlist:
				PERID = element.pop(0)
				ls = list(element)
				result = forest.test(ls)
				# if result>1000:
				# 	print str(PERID)+" "+str(1)
				# else:
				# 	print str(PERID)+" "+str(0)
	# with open(result.csv) as resultfile: