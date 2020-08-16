#!/usr/bin/python
# 
import  sys, os, subprocess, argparse
from progress.bar import Bar
from subprocess import check_output
from subprocess import call
from subprocess import Popen

#DEF CONSTANTS
PORT = "8888:8888"
DIRS = "default"
LABEL = "coursenotes"



def startJupyterLab(port, directory, label):
	#print(student)#change to progress
	dirs = directory+":/home/jovyan/"+ label
	command = ['docker', 'run', '-p', port, '-v', dirs, 'socsguelph/jupyter-java', 'start.sh', 'jupyter', 'lab']
	print(" ".join(command))
	with Popen(command,stdout=subprocess.PIPE) as p:
		print(p.stdout.read())



def main(args):
	#COMMAND LINE ARGS
	parser = argparse.ArgumentParser()
	parser.add_argument("-p" , "--port", type=str, help="port number", default=PORT)
	parser.add_argument("-d" , "--startdir" , type=str, help="Startup directory", default=DIRS)
	parser.add_argument("-l" , "--label", type=str, help="Label displayed in jupyter", default=LABEL)
	args = parser.parse_args()
	if (args.startdir is 'default'):
		args.startdir = os.getcwd()
	
	#MAIN
	startJupyterLab(args.port, args.startdir, args.label)

	return 

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
