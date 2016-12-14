#!/usr/bin/env python

import os
import sys
#import paramik
import subprocess
import re

### python pars_5smpl.py /home/varma/proj/HCM_WGS_Scripts/pars_file_format/ fam348cmh3610348cmh9011348cmh9611_head

readfl1=sys.argv[1]+sys.argv[2]+"_step2_annovar.hg19_multianno.txt"
readfl2=sys.argv[1]+sys.argv[2]+"_step2_annovar.hg19_multianno.vcf"

owrite1 = open(sys.argv[1]+sys.argv[2]+"_ANNOVAR_het_bed3.bed",'w')
owrite2 = open(sys.argv[1]+sys.argv[2]+"_ANNOVAR_het_bedDetail.bed",'w')
owrite3 = open(sys.argv[1]+sys.argv[2]+"_ANNOVAR_het.vcf",'w')

infile1_hd  = open(readfl1,'r').readlines()[0]
infile_ech = infile1_hd.split()

infile2_hd  = open(readfl2,'r').readlines()
for infl in infile2_hd:
	infll = infl.strip()
	if infll[0]=="#" and infll[1]!="#":
		readhd_other = '\t'.join(infll.split()[3:])

oustr_head1 = str("#")+infile_ech[0]+"\t"+str("Start")+"\t"+infile_ech[2]
oustr_head2 = str("#")+infile_ech[0]+"\t"+str("Start")+"\t"+infile_ech[2]+"\t"+str(readhd_other)+"\t"+str('\t'.join(infile_ech[5:70]))

owrite1.write(str(oustr_head1)+"\n")
owrite2.write(str(oustr_head2)+"\n")

#print oustr_head1
#print oustr_head2

infile1  = open(readfl1,'r').readlines()[1:] #[200:] #[140:]  #[144:]
for infl in infile1:
	infl1 = infl.strip().split()
	infl2 = "\t".join(infl1[-9:])
	infl3 = infl1[-3:]
	lst = 0
	for tt in infl3:
		tt1 = tt.split(":")[0]
		el2 = re.compile("[|/]").split(tt1)
		if el2[0] != el2[1]:
			True
			lst += 1
		if lst == 3:
			True
			oustr1 = str("chr")+str(infl1[0])+"\t"+str(int(infl1[-11])-int(1))+"\t"+infl1[2]

			oustr2 = str("chr")+str(infl1[0])+"\t"+str(int(infl1[-11])-int(1))+"\t"+infl1[2]+"\t"+str(infl2)+"\t"+str('\t'.join(infl1[5:70]))
			owrite1.write(str(oustr1)+"\n")
			owrite2.write(str(oustr2)+"\n")
owrite1.close()
owrite2.close()


infile22=[]
infile2  = open(readfl2,'r').readlines()
for infl in infile2:
	infll = infl.strip()
	if infll[0]!="#":
		infile22.append(infll)
	elif infll[0]=="#":
		owrite3.write(str(infll)+"\n")

for vfl in infile22:
	vfl1 = vfl.strip().split()
	vfl2 = vfl1[-3:]
	lst1 = 0
	for tt in vfl2:
		tt1 = tt.split(":")[0]
		el2 = re.compile("[|/]").split(tt1)
		if el2[0] != el2[1]:
			True
			#print el2
			lst1 += 1
		if lst1 == 3:
			True
			#print str(vfl)
			owrite3.write(str(vfl)+"\n")
owrite3.close()
	
print ("job has been done...")



