import pandas as pd
import csv
import os


def read_table(inputpath):
    if inputpath is None:
        return 10

    fileType = os.path.splitext(inputpath)[-1].lower()
    if fileType == '.csv':
        filename = os.path.splitext(inputpath)[0]
        outputpath = f"{filename}.xlsx"

        try:
            df2 = pd.read_csv(inputpath, sep=',', encoding='utf-8', on_bad_lines='skip', comment=';', quoting=csv.QUOTE_NONE)
        except Exception as e:
            print(f"Read_csv appear Error:{e}")
            return None
        try:
            df2.to_excel(outputpath, index=False)
            df1 = pd.read_excel(outputpath)
            return df1
        except Exception as e:
            print(f"Read_excel appear Error:{e}")
            return None
    elif fileType == '.xlsx':
        try:
            df1 = pd.read_excel(inputpath)
            return df1
        except Exception as e:
            print(f"Error reading Excel: {e}")
            return None
    print(inputpath)


def column_data(inputpath, brand, logic, channel):
    my_data = []
    dataframe = read_table(inputpath)
    #  logic 指的是使用什么逻辑分析仪品牌，k指的值“kvigst”,z指的是“正点原子”
    #  brand 指的是AP的厂家
    if logic == 'k':
        if channel == 1:
            column1_data = dataframe.iloc[:, 1]
            column0_data = dataframe.iloc[:, 0]
        elif channel == 2:
            column1_data = dataframe.iloc[:, 2]
            column0_data = dataframe.iloc[:, 0]
        if brand == '10':
            for i in range(0, len(column1_data) - 1):
                # 四川零点使用column1_data[i] == 0 and column1_data[i + 1] == 1
                # 信捷使用column1_data[i] == 1 and column1_data[i + 1] == 0
                if column1_data[i] == 0 and column1_data[i + 1] == 1:
                    value = column0_data[i + 1] - column0_data[i]
                    if 0.1 / 1000 < value < 20.0 / 1000:
                        my_data.append(
                            [column0_data[i], column0_data[i + 1], value])
        elif brand == '01':
            for i in range(0, len(column1_data) - 1):
                # 四川零点使用column1_data[i] == 0 and column1_data[i + 1] == 1
                # 信捷使用column1_data[i] == 1 and column1_data[i + 1] == 0
                if column1_data[i] == 1 and column1_data[i + 1] == 0:
                    value = column0_data[i + 1] - column0_data[i]
                    if 0.1 / 1000 < value < 20.0 / 1000:
                        my_data.append(
                            [column0_data[i + 1], column0_data[i], value])
    elif logic == 'z':
        if channel == 1:
            column1_data = dataframe.iloc[:, 2]  # 正点原子第4列数据
            column0_data = dataframe.iloc[:, 1]  # 正点原子第2列数据
        elif channel == 2:
            column1_data = dataframe.iloc[:, 3]  # 正点原子第3列数据
            column0_data = dataframe.iloc[:, 1]  # 正点原子第2列数据
        if brand == '01':
            for i in range(0, len(column1_data) - 1):
                # 四川零点使用column1_data[i] == 0 and column1_data[i + 1] == 1
                # 信捷使用column1_data[i] == 1 and column1_data[i + 1] == 0
                if column1_data[i] == 0 and column1_data[i + 1] == 1:
                    value = column0_data[i + 1] - column0_data[i]
                    if 0.1 / 1000 < value < 20.0 / 1000:
                        my_data.append(
                            [column0_data[i], column0_data[i + 1], value])
        elif brand == '10':
            for i in range(0, len(column1_data) - 1):
                # 四川零点使用column1_data[i] == 0 and column1_data[i + 1] == 1
                # 信捷使用column1_data[i] == 1 and column1_data[i + 1] == 0
                if column1_data[i] == 1 and column1_data[i + 1] == 0:
                    value = column0_data[i + 1] - column0_data[i]
                    # if 0.1 / 1000 < value < 20.0 / 1000:
                    my_data.append(
                        [column0_data[i], column0_data[i + 1], value])
    else:
        print(logic)
    Mydata_Frame = pd.DataFrame(my_data, columns=['i', 'i+1', 'diff'])
    return Mydata_Frame
