

from astroboi_bio_tools.ToolLogic import ToolLogics


class Logics(ToolLogics):
    def __init__(self,init, brcd_dict):
        super().__init__()
        self.brcd_dict = brcd_dict
        self.prefix_len_fr = init[0][0]
        self.prefix_len_bk = init[0][1]
        self.len_tt_brcd = init[1]
        self.win_size = init[2]
        self.len_rp_binding = init[3]
        self.len_umi = init[4]
        self.seq_aftr_umi = init[5]

    def get_brcd_umi_frequency_from_FASTQ(self, fastq_list):
        print("st get_brcd_umi_frequency_from_FASTQ")
        result_dict = {}
        result_brcd_dict = {}

        for fastq in fastq_list:
            for i in range(self.prefix_len_fr, self.prefix_len_bk + self.win_size + 1):
                tt_brcd_fr_fastq = fastq[i: i + self.len_tt_brcd]
                if tt_brcd_fr_fastq in self.brcd_dict:
                    len_trgt = self.brcd_dict[tt_brcd_fr_fastq]
                    fastq_aftr_rp_bndng = fastq[i + self.len_tt_brcd + len_trgt + self.len_rp_binding:]

                    idx_seq_aftr_umi = fastq_aftr_rp_bndng.find(self.seq_aftr_umi)
                    if idx_seq_aftr_umi >= 0:
                        seq_tmp_umi = fastq_aftr_rp_bndng[idx_seq_aftr_umi - self.len_umi: idx_seq_aftr_umi]
                        ext_seq_umi = ""
                        if len(seq_tmp_umi) < self.len_umi:
                            ext_seq_umi += fastq[i + self.len_tt_brcd + len_trgt + self.len_rp_binding - (
                                        self.len_umi - len(
                                    seq_tmp_umi)):i + self.len_tt_brcd + len_trgt + self.len_rp_binding]
                        seq_umi = ext_seq_umi + seq_tmp_umi

                        if tt_brcd_fr_fastq + "_" + seq_umi in result_dict:
                            result_dict[tt_brcd_fr_fastq + "_" + seq_umi] += 1
                        else:
                            result_dict.update({tt_brcd_fr_fastq + "_" + seq_umi: 1})

                        if tt_brcd_fr_fastq in result_brcd_dict:
                            result_brcd_dict[tt_brcd_fr_fastq] += 1
                        else:
                            result_brcd_dict.update({tt_brcd_fr_fastq: 1})

        print("DONE get_brcd_umi_frequency_from_FASTQ")
        return result_dict, result_brcd_dict
