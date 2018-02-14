"""
A python program for predicting if a person has chances of becoming a criminal using machine learning.

This can be done by using random forest method for it's prediction.
Number of parameters = 70
Subsample of each decision tree = 100
Total number of trees in the forest = 2000
Training set = 45719
Testing set = 11430
"""

import csv
import random
import copy
import numpy as np
from sklearn import tree

class classifier:
	def __init__(self,trainlist):
		self.trainlist = trainlist
		for every in self.trainlist:
			every.pop(0)
	def test(self,ls):
		result = 0
		for i in range(0,2001,1):
			#100 for random subset from the dataset
			treelist = []
			treelist = random.sample(self.trainlist,10)
			copied = []
			copied = copy.deepcopy(treelist)
			treeresult = []
			for one in copied:
				ans = one.pop()
				treeresult.append(ans)
			clf = tree.DecisionTreeClassifier()
			clf = clf.fit(copied,treeresult)
			#Error in this line, some thing about the shape of the predicting ones
			ls = np.asarray(ls)
			
			result+= clf.predict(ls)
		return result


if __name__ == "__main__":
	with open('criminal_train.csv') as keyfile:
		keylist = csv.DictReader(keyfile)
		for row in keylist:
			keyls = row.keys()
			break
	with open('criminal_train.csv') as trainfile:
		traindata = csv.reader(trainfile)
		trainlist = list(traindata)
		del trainlist[0]
		forest = classifier(trainlist)
		with open('criminal_test.csv') as testfile:
			testdata = csv.reader(testfile)
			testlist = list(testdata)
			del testlist[0]
			for element in testlist:
				PERID = element.pop(0)
				result = forest.test(element)
				if result>1000:
					print str(PERID)+" "+str(1)
				else:
					print str(PERID)+" "+str(0)