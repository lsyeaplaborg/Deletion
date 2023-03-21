#for i in *delmap.txt; do python delsize_count_sep2.py $i ${i/_delmap.txt/_filt_clones.txt} ${i/_delmap.txt/_delsize_count_sep2.txt} ${i/_delmap.txt/}; done

import sys
f = open(sys.argv[1], 'r').readlines()
filt_clones = open(sys.argv[2], 'r').readlines() #filt_clones
o = open(sys.argv[3], 'w')
total_reads = len(filt_clones)-1
del_len = []
for i in range(1, len(f)):
	if int(f[i].strip().split('\t')[1]) >= 20:
		del_len.append(int(f[i].strip().split('\t')[7]))

len_cnt = {}
for i in range(1, 151):
	if int(i) in del_len:
		len_cnt[i] = del_len.count(i)
	else :
		len_cnt[i] = 0
gt150 = 0
for i in del_len:
	if int(i) > 150:
		gt30 += 1
len_cnt['>150'] = gt150

o.write('\t'+sys.argv[4]+'\n')
o.write('total_reads\t'+str(total_reads)+'\n')
for k, v in len_cnt.items():
	o.write(str(k)+'\t'+str(v)+'\n')
for k, v in len_cnt.items():
	o.write(str(k)+'\t'+str(float(v)/total_reads*100)+'\n')
	
	

