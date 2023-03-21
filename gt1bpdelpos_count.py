#for i in *delmap.txt; do python gt1bpdelpos_count.py $i ${i/_delmap.txt/_filt_clones.txt} ${i/_delmap.txt/_gt1bpdelpos_count.txt} ${i/_delmap.txt/}; done
import sys
f = open(sys.argv[1], 'r').readlines()
filt_clones = open(sys.argv[2], 'r').readlines() #filt_clones
o = open(sys.argv[3], 'w')#output file
total_reads = len(filt_clones)-1

delpos = []
for i in range(1, len(f)):
	if int(f[i].strip().split('\t')[7]) > 1:
		delpos.append(int(f[i].strip().split('\t')[1]))
for i in range(1, len(f)):
	if int(f[i].strip().split('\t')[7]) > 1:
		delpos.append(int(f[i].strip().split('\t')[2]))
		
		
	
del20_30bp = 0
del31_45bp = 0
del46_60bp = 0
del61_75bp = 0
del76_90bp = 0
del91_105bp = 0
del106_120bp = 0
del121_135bp = 0
del136_150bp = 0
del151_165bp = 0
del166_180bp = 0
del181_195bp = 0
del196_210bp = 0


for i in range(0, len(delpos)):
	if 20 <= delpos[i] <=	30:
		del20_30bp += 1
	elif 31 <= delpos[i] <=	45:
		del31_45bp += 1
	elif 46 <= delpos[i] <=	60:
		del46_60bp += 1
	elif 61 <= delpos[i] <=	75:
		del61_75bp += 1
	elif 76 <= delpos[i] <=	90:
		del76_90bp += 1
	elif 91 <= delpos[i] <=	105:
		del91_105bp += 1
	elif 106 <= delpos[i] <= 120:
		del106_120bp += 1
	elif 121 <= delpos[i] <= 135:
		del121_135bp += 1
	elif 136 <= delpos[i] <= 150:
		del136_150bp += 1
	elif 151 <= delpos[i] <= 165:
		del151_165bp += 1
	elif 166 <= delpos[i] <= 180:
		del166_180bp += 1
	elif 181 <= delpos[i] <= 195:
		del181_195bp += 1
	else:
		del196_210bp += 1
	
o.write('\t'+sys.argv[4]+'\n')
o.write('total_reads\t'+str(total_reads)+'\n')
o.write('del20_30bp'+'\t'+str(del20_30bp)+'\n')
o.write('del31_45bp'+'\t'+str(del31_45bp)+'\n')
o.write('del46_60bp'+'\t'+str(del46_60bp)+'\n')
o.write('del61_75bp'+'\t'+str(del61_75bp)+'\n')
o.write('del76_90bp'+'\t'+str(del76_90bp)+'\n')
o.write('del91_105bp'+'\t'+str(del91_105bp)+'\n')
o.write('del106_120bp'+'\t'+str(del106_120bp)+'\n')
o.write('del121_135bp'+'\t'+str(del121_135bp)+'\n')
o.write('del136_150bp'+'\t'+str(del136_150bp)+'\n')
o.write('del151_165bp'+'\t'+str(del151_165bp)+'\n')
o.write('del166_180bp'+'\t'+str(del166_180bp)+'\n')
o.write('del181_195bp'+'\t'+str(del181_195bp)+'\n')
o.write('del196_210bp'+'\t'+str(del196_210bp)+'\n')



o.write('20_30'+'\t'+str(del20_30bp/total_reads*100)+'\n')
o.write('31_45'+'\t'+str(del31_45bp/total_reads*100)+'\n')
o.write('46_60'+'\t'+str(del46_60bp/total_reads*100)+'\n')
o.write('61_75'+'\t'+str(del61_75bp/total_reads*100)+'\n')
o.write('76_90'+'\t'+str(del76_90bp/total_reads*100)+'\n')
o.write('91_105'+'\t'+str(del91_105bp/total_reads*100)+'\n')
o.write('106_120'+'\t'+str(del106_120bp/total_reads*100)+'\n')
o.write('121_135'+'\t'+str(del121_135bp/total_reads*100)+'\n')
o.write('136_150'+'\t'+str(del136_150bp/total_reads*100)+'\n')
o.write('151_165'+'\t'+str(del151_165bp/total_reads*100)+'\n')
o.write('166_180'+'\t'+str(del166_180bp/total_reads*100)+'\n')
o.write('181_195'+'\t'+str(del181_195bp/total_reads*100)+'\n')
o.write('196_210'+'\t'+str(del196_210bp/total_reads*100)+'\n')





	
