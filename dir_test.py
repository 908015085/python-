
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
	
#from __future__ import print_function
#import os
#import sys


#def main():
#	if sys.version_info.major >= 3:
#		input_func = input
#	else:
#		input_func = raw_input
		
#	CheckDir = input_func("Enter the name of the directory to check: ")
#	print()
	
#	if os.path.exists(CheckDir):
#		print("The directory exists")
#	else:
#		print("No directory found for " + CheckDir)
#		print()
#		os.makedirs(CheckDir)
#		print("Directory created for " + CheckDir)
		
#if __name__ == '__main__':
#	main()