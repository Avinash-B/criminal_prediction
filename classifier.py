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
	def __init__(self,keyls,trainlist):
		self.keyls = keyls
		self.trainlist = trainlist
		pass
	def test(self,element):
		result = 0
		for i in range(0,2001):
			#30 for random subset from the dataset
			treelist = random.sample(self.trainlist,30)
			print treelist
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
		forest = classifier(keyls,trainlist)
		with open('criminal_test.csv') as testfile:
			testdata = csv.reader(testfile)
			testlist = list(testdata)
			for element in testlist:
				result = forest.test(element)
				if result>1000:
					print str(element[0])+" "+str(1)
				else:
					print str(element[0])+" "+str(0)
	# with open(result.csv) as resultfile: