import pandas as pd
import os

def clean_data(input_path,output_path):
    df=pd.read_csv(input_path)
    df=df.dropna(how="all")
    df=df[df["Order Date"].str[0:2]!="Or"]
    
    df["Quantity Ordered"]=pd.to_numeric(df["Quantity Ordered"])
    df["Price Each"]=pd.to_numeric(df["Price Each"])
    df["Order Date"]=pd.to_datetime(df["Order Date"],format='%m/%d/%y %H:%M')
    
    df["Sales"]=df["Quantity Ordered"]*df["Price Each"]
    
    df.to_csv(output_path,index=False)
    print(f"Cleaning Complete : {output_path}")
    print(df.head())
    
if __name__=="__main__":
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    INPUT=os.path.join(BASE_DIR,"data","processed","all_data.csv")
    OUTPUT=os.path.join(BASE_DIR,"data","processed","cleaning_data.csv")
    clean_data(INPUT,OUTPUT)
    
    