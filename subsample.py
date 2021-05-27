#!/usr/bin/python3
# this sample code takes one fastq at a time and subsample (downsample) it in half the reads
# we used this strategy for verifying sensitivity and which multimodal parameters get severely affected 
# by sequencing less reads, and if downstream analysis would be affected (cluster annotation)

import gzip
import random

random.seed(9001)

record_number = 0
with gzip.open("VDJ_S2_L001_R2_001.fastq.gz", "rt") as in_fh:
    with gzip.open("sub25_VDJ_S2_L001_R2_001.fastq.gz", "w") as out_fh:
        for line in in_fh:
            if line.startswith("@"):
                header = line
            else:
                continue
            seq = in_fh.readline().strip()
            plus = in_fh.readline().strip()
            qual = in_fh.readline().strip()
            if random.randrange(0,2) == 0: # start,stop
                out_fh.write("{}{}\n{}\n{}\n".format(header, seq,plus, qual).encode('utf-8'))
            record_number += 1
