import pandas as pd
import os
import glob

def merge_sales_data(raw_path,output_path):
    all_files=glob.glob(os.path.join(raw_path,"*.csv"))
    
    if not all_files:
        print(f"Error: No CSV files found in {raw_path}")
        return
    
    df_list=[pd.read_csv(file) for file in all_files]
    df_sum=pd.concat(df_list,axis=0,ignore_index=True)
    os.makedirs(os.path.dirname(output_path),exist_ok=True)
    df_sum.to_csv(output_path,index=False)

    print(f"Successfully merged{len(all_files)} files into {output_path}")
    print(f"Total rows:{len(df_sum)}")

if __name__=="__main__":
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAW_DIR=os.path.join(BASE_DIR,"data","raw","Sales-Analysis-Dataset")
    PROCESSED_FILE=os.path.join(BASE_DIR,"data","processed","all_data.csv")
    print(f"Looking for files in {RAW_DIR}")
    merge_sales_data(RAW_DIR,PROCESSED_FILE)
    
