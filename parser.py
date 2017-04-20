import numpy as np

def calculation (start, end):
	start_tk = start.split(':')
	end_tk = end.split(':')
	start_time = np.zeros((3,1))
	end_time = np.zeros((3,1))
	elapsed_time = np.zeros((3,1))
	#print start_tk
	#print end_tk
	for i in [0,1,2]:
		start_time[i] = int(start_tk[i])
		end_time[i] = int(end_tk[i])
	#print start_time
	#print end_time
	if(start_time[0] == end_time[0]):
		elapsed_time[1] = end_time[1] - start_time[1]
		elapsed_time[2] = end_time[2] - start_time[1]
	else:
		elapsed_time[1] = 60 - start_time[1] + end_time[1]
		elapsed_time[2] = 60 - start_time[2] + end_time[2]
	
	if( elapsed_time[2] < 0):
		elapsed_time[2] +=60
		elapsed_time[1] -=1
	if(elapsed_time[2] > 59):
		elapsed_time[2] -=60
		elapsed_time[1] +=1 	
	
	print elapsed_time[0],elapsed_time[1],elapsed_time[2]
	print '-------------------'
	return	


infile = open('AESY_SOBEL.txt');
#outfile = open('out.txt');

for line in infile:
	words = line.split(' ')
	#print words
	if ( ('0%' in words) & ('map' in words) ):
		print words[1]	
		start = words[1]
	if( ('100%' in words) & ('map' in words) ):
		print words[1]
		calculation(start, words[1])

infile.close();

