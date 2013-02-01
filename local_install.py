#!/bin/python
'''

	Should use "pip install -r requirements.txt" however it was having some errors on one system so this was created

'''
import os
import subprocess
import argparse  # TODO add in flags for system to use easy_install to get pip! ...or to just use easy install?


def file_parse(req_file):
	i = 0
	for line in req_file:
		print str(i), line.rstrip()
		i += 1
		subprocess.Popen(['sudo', 'pip', 'install', line.rstrip()]).wait()


def file_pase_easy(req_file):
	i = 0
	for line in req_file:
		print str(i), line.rstrip()
		i += 1
		subprocess.Popen(['sudo', 'easy_install', line.rstrip()]).wait()


req_file = file("requirements.txt")
file_parse(req_file)