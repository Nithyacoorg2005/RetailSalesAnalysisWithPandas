import os
import src

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RAW_DIR = os.path.join(BASE_DIR, "data", "raw", "Sales-Analysis-Dataset")
    ALL_DATA = os.path.join(BASE_DIR, "data", "processed", "all_data.csv")
    CLEAN_DATA = os.path.join(BASE_DIR, "data", "processed", "cleaning_data.csv")

    print("--- Starting Pipeline ---")
    src.merge_sales_data(RAW_DIR, ALL_DATA)
    src.clean_data(ALL_DATA, CLEAN_DATA)
    src.run_analysis(CLEAN_DATA)
    
    print("--- Pipeline Complete ---")

if __name__ == "__main__":
    main()