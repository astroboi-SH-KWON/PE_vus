import time
import os
from Bio import SeqIO
import multiprocessing as mp
import numpy as np
import platform

# import Util
# import Logic
# import LogicPrep
#################### st env ####################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    REF_DIR = "../hg38/"
    pass
else:
    # DEV
    WORK_DIR = ""
    REF_DIR = "D:/000_WORK/000_reference_path/"

IN = 'input/'
OU = 'output/'

os.makedirs(WORK_DIR + IN, exist_ok=True)
os.makedirs(WORK_DIR + OU, exist_ok=True)

TOTAL_CPU = mp.cpu_count()
MULTI_CNT = int(TOTAL_CPU*0.8)
#################### en env ####################

def test():
    pass

if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    test()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))