#!/usr/bin/env python3

import sys
import re

def processpairs(pairs):
	sortedpairs = sorted(pairs, key=lambda x: x[1], reverse=True);

	d={};
	prev=();
	for e in sortedpairs:
		md5=e[1]
		if md5 != prev:
			d[md5] = [];
			d[md5].append(e[0]);
		if md5 == prev:
			d[md5].append(e[0]);
		prev=md5

	d2={}
	for i in d:
		if(len(d[i]) > 1):
			d2[i] = d[i]

	return d2

#def identicalfiles(data):
#
#	pairs=[]
#	for line in data:
#		pairs.append((line[3], (int(line[0]), int(line[1]), line[2], line[4])));
#
#	return processpairs(pairs)

#def dupdirs(data):
#
#	pairs=[]
#
#	dirs={}
#	for line in data:
#		if (line[3] not in dirs):
#			dirs[line[3]]=[];
#
#		dirs[line[3]].append((int(line[0]), int(line[1]), line[2], line[4]))
#
#	for d in dirs:
#		pairs.append((d, tuple(dirs[d])));
#			
#	return processpairs(pairs)

def dupdirs_wholetrees(data):

	pairs=[]

	dirs={}
	for line in data:
		input_size=line[0]
		input_time=line[1]
		input_hash=line[2]
		input_path=line[3]
		input_file=line[4]
		dir_components=input_path.split('/')
		path=""
		for c in dir_components:
			if c == "":
				continue

			if c == ".":
				path="."
			else:
				path=path + '/' + c

			if (path not in dirs):
				dirs[path]=[];

			dirs[path].append((int(input_size), int(input_time), input_hash, input_file))

	for d in dirs:
		pairs.append((d, tuple(dirs[d])));
			
	processedpairs = processpairs(pairs)

	#Clean away cases of directories that only have one subdirectory and
	#thus they appear to be duplicates.
	keys_to_pop=[]
	for p in processedpairs:
		what_to_remove=[]
		for d in processedpairs[p]:
			for e in processedpairs[p]:
				#print("Testing :" + d + ": against :" + e + ":")
				if d in e and d != e:
					#print("True!")
					what_to_remove.append(e)
		for w in what_to_remove:
			if w in processedpairs[p]:
				#print("Removing " + w)
				processedpairs[p].remove(w)
				if len(processedpairs[p]) == 1:
					#print("Only one left")
					keys_to_pop.append(p)

	for k in keys_to_pop:
		#print("Deleting!")
		#print(processedpairs[k])
		processedpairs.pop(k)

	#Clean out subdirectories of duplicate parent directories.
	keys_to_pop=[]
	for x in processedpairs:
		for y in processedpairs:
			if set(x).issubset(set(y)) and set(x) != set(y) and x != y:
				keys_to_pop.append(x)

	for k in keys_to_pop:
		if k in processedpairs:
			processedpairs.pop(k)

	return processedpairs

#dev=sys.argv[1]
#pairs = [
#	(1, 2), (6, 6), (3, 2), (5, 5), (4, 5), (2, 2),
#]

#pairs = [
#	(('a', 'b'), ('c', 'd')), (('a', 'c'), ('a', 'h')), (('f', 'h'), ('c', 'd')), (('a', 'b'), ('e', 'e')), (('x', 'x'), ('c', 'd')), 
#]

#test = {3: (4, 1), 2: (6,11), 5: (1,6), 2: (7, 3), 4: (10, 10), 1: (1, 0)};

#print(sorted(test, key=lambda x: ))

n=0
readdata=[]
for line in sys.stdin.readlines():
	if (line != '\n'):
		n=n+1
		#print(line)
		fields=re.split(' +', line.rstrip('\n').lstrip(' '))
		file_sections = fields[3].rpartition('/')
		readdata.append((fields[0], fields[1], fields[2], file_sections[0], file_sections[2]))

#d2 = identicalfiles(readdata)

#for key in sorted(d2, reverse=True):
	#print(key, d2[key])

d3 = dupdirs_wholetrees(readdata)

for key in sorted(d3, reverse=True, key=lambda x: sum(e[0] for e in x)):
	print(sorted(d3[key]))


