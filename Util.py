from Bio import SeqIO

from astroboi_bio_tools.ToolUtil import ToolUtils


class Utils(ToolUtils):
    def make_fastq_file_to_list(self, path):
        temp = list(SeqIO.parse(path, "fastq"))
        return [str(temp[k].seq) for k in range(len(temp))]
