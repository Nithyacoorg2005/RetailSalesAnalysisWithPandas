import pandas as pd
import os

def run_analysis(input_path):
    df=pd.read_csv(input_path)
    df['Order Date']=pd.to_datetime(df['Order Date'])
    df['Month']=df['Order Date'].dt.month
    
    monthly_sales=df.groupby('Month')['Sales'].sum()
    print("Monthly Sales Data")
    print(monthly_sales.sort_values(ascending=False))
    
    def get_address(address):
        return address.split(',')[1].strip()
    df['City']=df['Purchase Address'].apply(get_address)
    city_sales=df.groupby('City')['Sales'].sum()
    print('Sales According to City is: ')
    print(city_sales.sort_values(ascending=False))
    
if __name__=="__main__":
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLEAN_DATA=os.path.join(BASE_DIR,"data","processed","cleaning_data.csv")
    run_analysis(CLEAN_DATA)
    
    