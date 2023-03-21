#for i in *delmap.txt; do python delsize_count.py $i ${i/_delmap.txt/_filt_clones.txt} ${i/_delmap.txt/_delsize_count.txt} ${i/_delmap.txt/}; done

import sys
f = open(sys.argv[1], 'r').readlines()
filt_clones = open(sys.argv[2], 'r').readlines() #filt_clones
o = open(sys.argv[3], 'w')
total_reads = len(filt_clones)-1
del_len = []
for i in range(1, len(f)):
	if int(f[i].strip().split('\t')[1]) >= 20:
		del_len.append(int(f[i].strip().split('\t')[7]))

del1bp = 0
del2_20bp = 0
delgt20bp = 0


for i in range(0, len(del_len)):
	if del_len[i] == 1:
		del1bp += 1
	elif 2 <= del_len[i] <=	20:
		del2_20bp += 1
	else:
		delgt20bp += 1

o.write('\t'+sys.argv[4]+'\n')
o.write('total_reads\t'+str(total_reads)+'\n')
o.write('del1bp'+'\t'+str(del1bp)+'\n')
o.write('del2_20bp'+'\t'+str(del2_20bp)+'\n')
o.write('delgt20bp'+'\t'+str(delgt20bp)+'\n')

o.write('1'+'\t'+str(del1bp/total_reads*100)+'\n')
o.write('2_20'+'\t'+str(del2_20bp/total_reads*100)+'\n')
o.write('>20'+'\t'+str(delgt20bp/total_reads*100)+'\n')
	

