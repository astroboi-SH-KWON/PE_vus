import time
import os
from Bio import SeqIO
import multiprocessing as mp
import numpy as np
import platform

import Util
import Logic
import LogicPrep
#################### st env ####################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    pass
else:
    # DEV
    WORK_DIR = "D:/000_WORK/YuGooSang/20210325/WORK_DIR/"

IN = 'input/'
OU = 'output/'
FASTQ = 'FASTQ/'

os.makedirs(WORK_DIR + IN, exist_ok=True)
os.makedirs(WORK_DIR + OU, exist_ok=True)
os.makedirs(WORK_DIR + FASTQ, exist_ok=True)

TOTAL_CPU = mp.cpu_count()
MULTI_CNT = int(TOTAL_CPU*0.8)

BRCD_FL = "PE_vus_293T_sub_M50_barcode.xlsx"
prefix_len_fr = 18 + 19 + 76 + 23  # 23 is the shortest length of RT-PBS (23~38)
prefix_len_bk = 18 + 19 + 76 + 38  # 38 is the longest length of RT-PBS (23~38)
len_tt_brcd = 24
win_size = 2
len_umi = 10  # UMI
len_rp_binding = 20
seq_aftr_umi = "CTACTCTACCAC"
# seq_half_rp_binding = "CCTGCCTTTA"
INIT = [[prefix_len_fr, prefix_len_bk], len_tt_brcd, win_size, len_rp_binding, len_umi, seq_aftr_umi]

#################### en env ####################
# brcd_df = Util.Utils().read_excel_to_df(WORK_DIR + IN + BRCD_FL)
# # key : TTTTTT+barcode, val : Target length
# BRCD_DICT = LogicPrep.LogicPreps().make_df_to_dict(brcd_df, 0, 1)


def multi_process():
    util = Util.Utils()
    logic_prep = LogicPrep.LogicPreps()
    brcd_df = Util.Utils().read_excel_to_df(WORK_DIR + IN + BRCD_FL)
    # key : TTTTTT+barcode, val : Target length
    brcd_dict = LogicPrep.LogicPreps().make_df_to_dict(brcd_df, 0, 1)
    logic = Logic.Logics(INIT, brcd_dict)

    sources = util.get_files_from_dir(WORK_DIR + FASTQ + "*.fastq")

    for path in sources:
        fastq_list = util.make_fastq_file_to_list(path)

        # divide data_list by MULTI_CNT
        splited_fastq_list = np.array_split(fastq_list, MULTI_CNT)
        print("platform.system() : ", SYSTEM_NM)
        print("total cpu_count : ", str(TOTAL_CPU))
        print("will use : ", str(MULTI_CNT))
        pool = mp.Pool(processes=MULTI_CNT)

        pool_list = pool.map(logic.get_brcd_umi_frequency_from_FASTQ, splited_fastq_list)

        result_dict, brcd_result_dict = logic_prep.merge_dict_pool_list(pool_list)

        res_list = logic_prep.make_dict_to_list(result_dict, brcd_result_dict)
        sorted_res_list = logic_prep.sort_list_by_ele(res_list, 0)
        header = ["barcode", "#tot_freq_barcode", "umi", "#freq_umi"]
        util.make_tsv(path.replace("FASTQ", "output").replace(".fastq", "_result.txt"), header, sorted_res_list)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    multi_process()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))



