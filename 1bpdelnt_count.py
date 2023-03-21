#for i in *_delmap.POS.txt; do python 1bpdelnt_count.py $i ${i/_delmap.POS.txt/_filt_clones.txt} ${i/_delmap.POS.txt/_1bpdelnt_count.txt} ${i/_delmap.POS.txt/}; done

import sys
f = open(sys.argv[1], 'r').readlines()
print(sys.argv[1])
filt_clones = open(sys.argv[2], 'r').readlines() #filt_clones
o = open(sys.argv[3], 'w')
total_reads = len(filt_clones)-1
del_nt = []
for i in range(1, len(f)):
	if int(f[i].strip().split('\t')[1]) >= 20 :
		del_nt.append(f[i].strip().split('\t')[3])
			


delA = 0
delT = 0
delC = 0
delG = 0
delAT = 0
delCG = 0


for i in range(0, len(del_nt)):
	if del_nt[i] == 'A':
		delA += 1	
	elif del_nt[i] == 'T':
		delT += 1
	elif del_nt[i] == 'C':
		delC += 1
	else:
		delG += 1

delAT = delA + delT
delCG = delC + delG		
deltotal = delA + delT +delC + delG

o.write('\t'+sys.argv[4]+'\n')
o.write('total_reads'+'\t'+str(total_reads)+'\n')
o.write('delA'+'\t'+str(delA)+'\n')
o.write('delT'+'\t'+str(delT)+'\n')
o.write('delC'+'\t'+str(delC)+'\n')
o.write('delG'+'\t'+str(delG)+'\n')
o.write('delAT'+'\t'+str(delAT)+'\n')
o.write('delCG'+'\t'+str(delCG)+'\n')

o.write('delA'+'\t'+str(delA/total_reads*100)+'\n')
o.write('delT'+'\t'+str(delT/total_reads*100)+'\n')
o.write('delC'+'\t'+str(delC/total_reads*100)+'\n')
o.write('delG'+'\t'+str(delG/total_reads*100)+'\n')
o.write('delAT'+'\t'+str(delAT/total_reads*100)+'\n')
o.write('delCG'+'\t'+str(delCG/total_reads*100)+'\n')

o.write('delA'+'\t'+str(delA/deltotal*100)+'\n')
o.write('delT'+'\t'+str(delT/deltotal*100)+'\n')
o.write('delC'+'\t'+str(delC/deltotal*100)+'\n')
o.write('delG'+'\t'+str(delG/deltotal*100)+'\n')
o.write('delAT'+'\t'+str(delAT/deltotal*100)+'\n')
o.write('delCG'+'\t'+str(delCG/deltotal*100)+'\n')








