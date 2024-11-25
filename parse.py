import os

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import pandas as pd

# my_list = []
# df = pd.read_excel('1000.xlsx')
# test_data = df.iloc[:, 1]

# 读取excel表格


def read_table(inputpath):
    filetype = os.path.splitext(inputpath)[-1]
    if filetype == '.csv':
        filename = os.path.splitext(inputpath)[0]  # 提取输入 CSV 文件的文件名
        output_file = f"{filename}.xlsx"  # 输出 Excel 文件名与输入 CSV 文件名保持一致
        df2 = pd.read_csv(inputpath)
        df2.to_excel(output_file, index=False)
        df1 = pd.read_excel(output_file)
        return df1
    elif filetype == '.xlsx':
        df1 = pd.read_excel(inputpath)
        return df1
    elif inputpath is None:
        return 10


#  生成一个数据列表，筛选相邻数据为1 0 的数据


def column_data(inputpath, brand):
    my_data = []
    dataframe = read_table(inputpath)
    column1_data = dataframe.iloc[:, 1]
    column0_data = dataframe.iloc[:, 0]
    if brand == '10':
        for i in range(0, len(column1_data) - 1):
            # 四川零点使用column1_data[i] == 0 and column1_data[i + 1] == 1
            # 信捷使用column1_data[i] == 1 and column1_data[i + 1] == 0
            if column1_data[i] == 0 and column1_data[i + 1] == 1:
                value = column0_data[i + 1] - column0_data[i]
                if 0.1 / 1000 < value < 20.0 / 1000:
                    my_data.append(
                        [column0_data[i + 1], column0_data[i], value])
    elif brand == '01':
        for i in range(0, len(column1_data) - 1):
            # 四川零点使用column1_data[i] == 0 and column1_data[i + 1] == 1
            # 信捷使用column1_data[i] == 1 and column1_data[i + 1] == 0
            if column1_data[i] == 1 and column1_data[i + 1] == 0:
                value = column0_data[i + 1] - column0_data[i]
                if 0.1 / 1000 < value < 20.0 / 1000:
                    my_data.append(
                        [column0_data[i + 1], column0_data[i], value])
    return my_data

# 生成一个表格数据


def Excel_Data(inputpath, brand):
    Mydata_Frame = pd.DataFrame(
        column_data(inputpath, brand), columns=[
            'i', 'i+1', 'diff'])
    return Mydata_Frame


def Toexcel(inputpath, brand):
    result_excel = Excel_Data(inputpath, brand)
    result_excel.to_excel('result.xlsx', index=True)


def DrawPlot(inputpath, brand):
    result_excel = Excel_Data(inputpath, brand)
    # result_excel.to_excel('result.xlsx', index=True)
    x = result_excel.index
    y = result_excel['diff'] * 1000
    myexcel1=plt.figure()
    plt.plot(
        x,
        y,
        marker='o',
        color='b',
        linestyle='-',
        linewidth=0.5,
        markersize=3)
    plt.ylim(0, 20)
    return myexcel1


def DrawBar(inputpath, brand):
    result_excel = Excel_Data(inputpath,brand)
    value = round(result_excel['diff'] * 1000, 1)
    num_bins = 10
    # 计算最小值和最大值
    min_val = min(value)
    max_val = max(value) + 1
    # 计算每个区间的宽度
    bin_width = (max_val - min_val) / num_bins
    # 给x轴赋值
    bins = [min_val + i * bin_width for i in range(num_bins)]
    bins.append(max_val)
    # for bin in bins[:-1]:
    #     print(bin)
    # bins = []
    # for i in range(num_bins):
    #     x_value = min_val+i*bin_width
    #     bins.append(x_value)
    # bins.append(max_val)
    # 统计每个区间中数据的个数
    # 使用字典方式实现,类似于HASH表
    counts = {bins_start: 0 for bins_start in bins[:-1]}
    for d in value:
        for bins_start in bins[:-1]:
            if bins_start <= d < bins[bins.index(bins_start) + 1]:
                counts[bins_start] += 1
    # ######## 绘制柱状图 ########
    outbar=plt2.figure()
    mybar = plt2.bar(
        range(
            1,
            num_bins + 1),
        counts.values(),
        align='center',
        width=0.5)
    plt2.xticks(range(1, num_bins + 1),
               ['[{:.1f}-{:.1f})'.format(bins[i],
                                         bins[i + 1]) for i in range(num_bins)])
    plt2.xlabel('t/ms')
    plt2.ylabel('count')
    for bar in mybar:
        height = bar.get_height()
        plt2.text(bar.get_x() + bar.get_width() / 2 - 0.2, height + 0.3, '%s' % int(height), size=10)
    plt2.title(' IO \'s   responding   time ')
    return outbar


def GetMaxValue(inputpath, brand):
    result_excel = Excel_Data(inputpath, brand)
    value = result_excel['diff']
    MaxValue = max(value)
    return round(MaxValue * 1000, 6)


def GetMinValue(inputpath, brand):
    result_excel = Excel_Data(inputpath, brand)
    value = result_excel['diff']
    MinValue = min(value)
    return round(MinValue * 1000, 6)


def GetAverageValue(inputpath, brand):
    result_excel = Excel_Data(inputpath, brand)
    value = result_excel['diff']
    length = len(value)
    sumvalue = sum(value)
    average = sumvalue / length * 1000
    return average


def GetCounts(inputpath, brand):
    result_excel = Excel_Data(inputpath, brand)
    value = result_excel['diff']
    length = len(value)
    return length
# 可以通过len(test_data)，读取到行数，不包含第一行，第一行为索引行
# test_data1 = df.iloc[:, 0]
# result_data = []
# for i in range(0, 110):
#     if test_data[i] == 1 and test_data[i + 1] == 0:
#         value = test_data1[i + 1] - test_data1[i]
#         print(test_data1[i + 1], test_data1[i], value)
#         my_list.append(value)
#         result_data.append([test_data1[i + 1], test_data1[i], value])
# result_df = pd.DataFrame(result_data, columns=['Value', 'Value2', 'Diff'])
# total = sum(my_list)
# count = len(my_list)
# average = total / count
# print(count)
# print(average * 1000)
# result_df.to_excel('result.xlsx', index=False)
# inputpath = input("输入文件路径：")
# graph = GetMaxValue(inputpath)
# Toexcel(inputpath)
# print(graph*1000)
