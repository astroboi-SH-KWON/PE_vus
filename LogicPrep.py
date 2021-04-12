
from astroboi_bio_tools.ToolLogicPrep import ToolLogicPreps


class LogicPreps(ToolLogicPreps):
    def make_df_to_dict(self, df, key_idx, val_idx):
        result_dict = {}
        len_df = len(df)
        for i in range(len_df):
            key = df.loc[i][key_idx]
            val = df.loc[i][val_idx]
            if key in result_dict:
                print(key, "is NOT unique!!!!")
            else:
                result_dict.update({key: val})
        return result_dict

    def make_dict_to_list(self, result_dict, brcd_result_dict):
        result_list = []
        for key, val in result_dict.items():
            tmp_arr = [key.split("_")[0], brcd_result_dict[key.split("_")[0]], key.split("_")[1], val]
            result_list.append(tmp_arr)
        return result_list

    def merge_dict_pool_list(self, pool_list):
        merge_dict = {}
        brcd_merge_dict = {}

        for data_dict, brcd_cnt_dict in pool_list:
            for brcd_umi, freq in data_dict.items():
                if brcd_umi in merge_dict:
                    merge_dict[brcd_umi] += freq
                else:
                    merge_dict.update({brcd_umi: freq})

            for brcd_key, freq in brcd_cnt_dict.items():
                if brcd_key in brcd_merge_dict:
                    brcd_merge_dict[brcd_key] += freq
                else:
                    brcd_merge_dict.update({brcd_key: freq})
        return merge_dict, brcd_merge_dict
