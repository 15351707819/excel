import os

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import pandas as pd
import csv

# my_list = []
# df = pd.read_excel('1000.xlsx')
# test_data = df.iloc[:, 1]

# 读取excel表格


def read_table(inputpath):
    if inputpath is None:
        return 10

    filetype = os.path.splitext(inputpath)[-1].lower()

    if filetype == '.csv':
        filename = os.path.splitext(inputpath)[0]
        output_file = f"{filename}.xlsx"

        try:
            # 添加COMMENT=';'，就是忽略掉注释的地方comment=';'：如果某行以 ; 开头，该行会被作为注释行跳过，不会被读取。
            # quotechar="'"：用单引号 ' 来包裹含有特殊字符或分隔符的字段内容。csv.QUOTE_NONE:pandas 在读取过程中，将非数字字段中的引号去除。数字字段会保持原样，不受影响。
            # on_bad_lines='skip'：遇到格式有问题的行时，将跳过，不会报错。
            df2 = pd.read_csv(inputpath, encoding='utf-8', sep=',', comment=';', quoting=csv.QUOTE_NONE, on_bad_lines='skip')
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return None

        try:
            df2.to_excel(output_file, index=False)
            df1 = pd.read_excel(output_file)
            return df1
        except Exception as e:
            print(f"Error converting/reading Excel: {e}")
            return None

    elif filetype == '.xlsx':
        try:
            df1 = pd.read_excel(inputpath)
            return df1
        except Exception as e:
            print(f"Error reading Excel: {e}")
            return None


#  生成一个数据列表，筛选相邻数据为1 0 的数据


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
            column1_data = dataframe.iloc[:, 3]  # 正点原子第4列数据
            column0_data = dataframe.iloc[:, 1]  # 正点原子第2列数据
        elif channel == 2:
            column1_data = dataframe.iloc[:, 2]  # 正点原子第3列数据
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
    return my_data

# 生成一个表格数据


def Excel_Data(inputpath, brand, logic, channel):
    Mydata_Frame = pd.DataFrame(
        column_data(inputpath, brand, logic, channel), columns=[
            'i', 'i+1', 'diff'])
    return Mydata_Frame


def Toexcel(inputpath, brand):
    result_excel = Excel_Data(inputpath, brand)
    result_excel.to_excel('result.xlsx', index=True)


def DrawPlot(inputpath, brand, logic, channel):
    result_excel = Excel_Data(inputpath, brand, logic,channel)
    result_excel.to_excel('result.xlsx', index=True)
    print(type(result_excel))
    x = result_excel.index
    y = result_excel['diff'] * 1000
    myexcel1 = plt.figure()
    plt.plot(
        x,
        y,
        marker='o',
        color='b',
        linestyle='-',
        linewidth=0.5,
        markersize=3)
    plt.ylim(0, 100)
    plt.show()
    return myexcel1


def DrawBar(inputpath, brand, logic,channel):
    result_excel = Excel_Data(inputpath, brand, logic,channel)
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
    outbar = plt2.figure()
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
        plt2.text(
            bar.get_x() +
            bar.get_width() /
            2 -
            0.2,
            height +
            0.3,
            '%s' %
            int(height),
            size=10)
    plt2.title(' IO \'s   responding   time ')
    return outbar


def GetMaxValue(inputpath, brand, logic, channel):
    result_excel = Excel_Data(inputpath, brand, logic, channel)
    value = result_excel['diff']
    MaxValue = max(value)
    return round(MaxValue * 1000, 6)


def GetMinValue(inputpath, brand, logic, channel):
    result_excel = Excel_Data(inputpath, brand, logic, channel)
    value = result_excel['diff']
    MinValue = min(value)
    return round(MinValue * 1000, 6)


def GetAverageValue(inputpath, brand, logic, channel):
    result_excel = Excel_Data(inputpath, brand, logic, channel)
    value = result_excel['diff']
    length = len(value)
    sumvalue = sum(value)
    average = sumvalue / length * 1000
    return average


def GetCounts(inputpath, brand, logic, channel):
    result_excel = Excel_Data(inputpath, brand, logic, channel)
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
