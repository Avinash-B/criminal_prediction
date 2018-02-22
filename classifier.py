"""
A python program for predicting if a person has chances of becoming a criminal using machine learning.

This can be done by using random forest method for it's prediction.
Number of parameters = 70
Subsample of each decision tree = 100
Total number of trees in the forest = 2000
Training set = 45719
Testing set = 11430
"""

#Applying multiprocessing for cloud usage
from multiprocessing import Process 
import csv
import random
import copy
import numpy as np
import time
from sklearn import tree

class classifier:
	def __init__(self,trainlist):
		self.trainlist = trainlist
		for every in self.trainlist:
			every.pop(0)

	def test(self,ls):
		result = 0
		for i in range(0,10000,1):
			#100 for random subset from the dataset
			treelist = []
			treelist = random.sample(self.trainlist,500)
			copied = []
			copied = copy.deepcopy(treelist)
			treeresult = []
			for one in copied:
				ans = one.pop()
				treeresult.append(ans)
			clf = tree.DecisionTreeClassifier()

			#Converting the input data into int
			arr=[]
			for element in copied:
				arr2 = []
				for elements in element:
					elements = int(float(elements))
					arr2.append(elements)
				arr.append(arr2)
			copied = arr
			#Done changing float to int part
			#Starting converting treeresult part
			arr = []
			for element in treeresult:
				element = int(float(element))
				arr.append(element)
			treeresult = arr
			#Done changing float to int part
			clf = clf.fit(copied,treeresult)
			#Now we are changing datatype of testting part
			ls = np.asarray(ls)
			arr = []
			for element in ls:
				element = int(float(element))
				arr.append(element)
			arr2 = []
			arr2.append(arr)
			result+= clf.predict(arr2)
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
		with open('submission.csv','w') as writefile:
			writer = csv.writer(writefile)
			writer.writerow(['PERID','Criminal'])
			with open('criminal_test.csv') as testfile:
				testdata = csv.reader(testfile)
				testlist = list(testdata)
				del testlist[0]
				count = 1
				process = 0
				for element in testlist:
					PERID = element.pop(0)
					if process==0:
						time.sleep(1)
						p1 = Process(target=test,args=(element,))
						process+=1
						p1.start()
						p4.join()
						del p4
					elif process==1:
						time.sleep(1)
						p2 = Process(target=test,args=(element,))
						process+=1
						p2.start()
						p1.join()
						del p1
					elif process==2:
						time.sleep(1)
						p3 = Process(target=test,args=(element,))
						process+=1
						p3.start()
						p2.join()
						del p2
					elif process==3:
						time.sleep(1)
						p4 = Process(target=test,args=(element,))
						process=0
						p4.start()
						p3.join()
						del p3
					if result>=5000:
						result = 1
					else:
						result = 0
					writer.writerow([''+str(PERID),''+str(result)])
				print("Completed "+str(count)+" item")
				count+=1
