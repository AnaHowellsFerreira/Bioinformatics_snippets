#!/usr/bin/python3.5
### This script calculates the average expression per transcript in a file containing TMP as an output 
### from Salmon aligner

import sys
import argparse
import os
import re
import json
from statistics import mean
from itertools import chain
from collections import defaultdict


#Command line Arguments
in_file=sys.argv[1]  # TPM_all_samples/{}_TPM
out_file=sys.argv[2] # TPM_all_samples/{}_TPM_AVG

# initialize empty dictionaries and lists to hold values
data=[]
dict_in={}
dict_out={}
gene_dict = dict()

x=0
in_f=open(in_file,'r')
out=open(out_file,'w')
for line_in in in_f:
    x=x+1
    if(x==1):
        sampleid_tmp=in_file.strip().split("/")[1]
        sample_id=sampleid_tmp.split("_")[1] ## sample ID being parsed from file name
        out.write("1GENE\t"+sample_id+"\n")
    if(x>1):
        col_in=line_in.strip().split("\t")
        if col_in[0] in dict_in.keys():
            dict_in[col_in[0]]=dict_in[col_in[0]]+','+str(col_in[2])
        else:
            dict_in[col_in[0]]=str(col_in[2]) ##col_in[2] is TPM value
for kk in dict_in.keys():
    out.write(kk+"\t"+str(sum(list(map(float,str(dict_in[kk]).split(","))))/len(str(dict_in[kk]).split(",")))+"\n")

