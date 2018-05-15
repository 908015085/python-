
import os
filenames = []
def findFile(path):
	for x in os.listdir(path):
		if os.path.isfile(os.path.join(path, x)):
			filenames.append(x)
		elif os.path.isdir(os.path.join(path,x)):
			findFile(os.path.join(path, x))

def containCertainStr(filenames, str):
	for x in filenames:
		if x.find(str) != -1:
			print(x)

if __name__ == '__main__':
	root = 'F:\\src\\mock'
	findFile(root)
	containCertainStr(filenames, 'use')