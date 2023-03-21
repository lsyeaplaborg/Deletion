#for i in *delmap.txt; do python 1bpdelpos_count.py $i ${i/_A_delmap.txt/_A_filt_clones.txt} ${i/_A_delmap.txt/_1bpdelpos_count.txt} ${i/_A_delmap.txt/}; done
import sys
f = open(sys.argv[1], 'r').readlines()
filt_clones = open(sys.argv[2], 'r').readlines() #filt_clones
o = open(sys.argv[3], 'w')#output file
reads_count = len(filt_clones)-1

delpos = []
for i in range(1, len(f)):
	if f[i].strip().split('\t')[7]=='1':
		delpos.append(int(f[i].strip().split('\t')[1]))
del_cnt = {}
for i in range(20, 202):
	if int(i) in delpos:
		del_cnt[i] = delpos.count(i)
	else :
		del_cnt[i] = 0

o.write('\t'+sys.argv[4]+'\n')
o.write('total_reads'+'\t'+str(reads_count)+'\n')
for k, v in del_cnt.items():
	o.write(str(k)+'\t'+str(v)+'\n')
for k, v in del_cnt.items():
	o.write(str(k)+'\t'+str(float(v)/reads_count*100)+'\n')
	
