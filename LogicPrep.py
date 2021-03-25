
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