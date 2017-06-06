#######################################
#AUTHOR: VINAYAK.V.NAVALE
#DATE:06/06/2017
#######################################


from  BASIC_STAT import get as Basic
import sys
import argparse

try:
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', '--list', help='delimited list input', type=str)
	args = parser.parse_args()
	my_list = [int(item) for item in args.list.split(',')]


	Basic_Stat= Basic.Stats(my_list)
	print Basic_Stat.mean()
	print Basic_Stat.mode()
	print Basic_Stat.median()
except: print "provide delimited list of input ex :- python main.py -l 1,2,2,4"

