#!/usr/bin/env python

#import os
import sys
#import paramik
import subprocess
#import re



### python pars_bedtoucsc-view.py /home/varma/proj/HCM_WGS_ANNOTATION_ANNOVAR/HCM_B00H7EW-B00H7EX-B00H7EY_chr1-MT_variants_GATK_ANNOVAR_het_bamtobed12-inter-rcc2.bed /home/varma/proj/HCM_WGS_ANNOTATION_ANNOVAR/HCM_B00H7EW-B00H7EX-B00H7EY_chr1-MT_Variants_GATK_ANNOVAR_het_CADD-indels-score_ReMM-Score.txt /home/varma/proj/HCM_WGS_ANNOTATION_ANNOVAR/HCM_B00H7EW-B00H7EX-B00H7EY_chr1-MT_variants_GATK_ANNOVAR_het_bed12-allScore2.bed


#awk 'FNR==NR {a[$1]=$2; b[$3]; next} ($1 in a && $3 in b) {print $1,a[$1],$2}' het_bamtobed12-inter-rcc2_head_nochr.bed het_CADD-indels-score_ReMM-Score_head.txt
#awk 'FNR==NR{a[$3]=$2 FS $3;next}{ print $0, a[$3]}' het_CADD-indels-score_ReMM-Score_head.txt het_bamtobed12-inter-rcc2_head_nochr.bed
#awk 'FNR==NR{a[$2]=$3;next}{print $0,a[$2]?a[$2]:"NA"}' het_CADD-indels-score_ReMM-Score_head.txt het_bamtobed12-inter-rcc2_head_nochr.bed
#join -1 1 -1 3 -2 1 -2 3 het_bamtobed12-inter-rcc2_head_nochr.bed het_CADD-indels-score_ReMM-Score_head.txt


#chrom	chromStart	chromEnd	name	score	strand	thickStart	thickEnd	itemRgb

readfl1=sys.argv[1]
readfl2=sys.argv[2]

owrite1 = open(sys.argv[3],'w')

dictbed = {}
infile1_hd  = open(readfl2,'r').readlines()[0]
owrite1.write(str("#chrom	chromStart	chromEnd	name	score	strand	thickStart	thickEnd	itemRgb")+"\t"+str(infile1_hd))

infile1_hd  = open(readfl1,'r').readlines()[1:]
for infl in infile1_hd:
	infll = infl.strip().split()
	infll1 = infll[0][3:]
	infll2 = ";".join(infll)
	dictbed[infll1+":"+infll[2]] = infll2

dictbed1 = {}
infile2_hd  = open(readfl2,'r').readlines()[1:]
for infl in infile2_hd:
	infll = infl.strip().split()
	infll2 = ";".join(infll)
	dictbed1[infll[0]+":"+infll[2]] = infll2

for k,v in dictbed1.iteritems():
	if k in dictbed.keys():
		###-----

		v1 = v.split(";")
		k1 = dictbed[k].split(";")
		#print v1[23],v1[26],v1[28],v1[29],v1[30],v1[36]

		if ((v1[12] == 'PASS') and (v1[23] == 'exonic') and (v1[26] != 'synonymous_SNV') and ((v1[28] <= "0.05") or (v1[28] == ".")) and (v1[29] == '.') and (v1[30] == '.') and ((v1[36] <= "0.05") or (v1[36] == ".")) and (v1[-1:] >= "0.9")):
			k1[k1.index('0,0,255')] = '255,55,55'

		elif ((v1[12] == 'PASS') and (v1[23] == 'exonic') and (v1[26] != 'synonymous_SNV') and ((v1[28] <= "0.05") or (v1[28] == ".")) and (v1[29] == '.') and (v1[30] == '.') and ((v1[36] <= "0.05") or (v1[36] == "."))):
			k1[k1.index('0,0,255')] = '255,55,0'

		elif ((v1[12] == 'PASS') and (v1[23] == 'exonic') and (v1[26] != 'synonymous_SNV') and ((v1[28] <= "0.05") or (v1[28] == ".")) and ((v1[36] <= "0.05") or (v1[36] == "."))):
			k1[k1.index('0,0,255')] = '255,0,55'

		elif ((v1[12] == 'PASS') and (v1[23] == 'exonic')):
			k1[k1.index('0,0,255')] = '255,0,0'

		elif (v1[23] == 'exonic'):
			k1[k1.index('0,0,255')] = '200,50,10'


		###----non-exonic -----

		elif ((v1[12] == 'PASS') and (v1[23] != 'exonic') and ((v1[28] <= "0.05") or (v1[28] == ".")) and (v1[-1:] >= "0.9")):
			k1[k1.index('0,0,255')] = '55,55,255'

		elif ((v1[12] == 'PASS') and (v1[23] != 'exonic') and ((v1[28] <= "0.05") or (v1[28] == "."))):
			k1[k1.index('0,0,255')] = '0,55,255'

		elif ((v1[12] == 'PASS') and (v1[23] != 'exonic')):
			k1[k1.index('0,0,255')] = '0,255,55'

		elif ((v1[23] != 'exonic')):
			k1[k1.index('0,0,255')] = '0,255,0'

		v2 = "\t".join(v1)
		fnout = "\t".join(k1)+"\t"+str(v2)
		owrite1.write(str(fnout)+"\n")
owrite1.close()

print ("job has been done...")




