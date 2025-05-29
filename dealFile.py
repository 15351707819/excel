import pandas as pd
import csv
import os


def read_table(inputpath):
    if inputpath is None:
        return 10

    fileType = os.path.splitext(inputpath)[-1].lower()
    if fileType == 'csv':
        filename = os.path.splitext(inputpath)[0]
        outputpath = f"{filename}.xlsx"

        try:
            df2 = pd.read_csv(inputpath, seq=',', encoding='utf-8', on_bad_lines='skip', comment=';', quoting=csv.QUOTE_NONE)
        except Exception as e:
            print(f"Read_csv appear Error:{e}")
        try:
            df2.to_excel(outputpath,index=False)
            df1 = pd.read_excel(outputpath)
            return df1
        except Exception as e:
            print(f"Read_excel appear Error:{e}")