import dealFile
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

import pandas as pd
from pandas import DataFrame


def DrawPlot(result_cel: DataFrame):
    x = result_cel.index
    y = result_cel['diff'] * 1000
    maxvalue = max(y)
    myexcel1 = plt.figure()
    plt.plot(x, y, 'bo', linestyle='-', linewidth=0.5, markersize=3)
    plt.ylim(0, maxvalue+maxvalue*4)
    plt.show()
    return myexcel1


def DrawBargraph(result_cel: DataFrame):
    values = round(result_cel['diff'] * 1000, 1)
    # 设置柱形图柱子的个数
    bar_num = 10
    # 确定每个区间的大小
    max_value = max(values) + 1
    min_value = min(values)
    interval_value = (max_value - min_value) / bar_num
    # 给x轴赋值
    bar_x = [min_value + interval_value * i for i in range(bar_num)]
    bar_x.append(max_value)
    # 给Y轴赋值，对每一个区间进行计数
    # 对每个区间的计数值使用HASH表的方式进行计数
    counts = {bar_start: 0 for bar_start in bar_x[:-1]}
    for value in values:
        for bar_start in bar_x[:-1]:
            if bar_start <= value < bar_x[bar_x.index(bar_start) + 1]:
                counts[bar_start] += 1
    # #########  绘制柱状图 ###########
    BarGraphs = plt2.bar(
        range(1, bar_num+1), counts.values(), align='center', width=0.5
    )
    plt2.xticks(range(1, bar_num+1),
                         ['[{:.1f}-{:.1f})'.format(bar_x[i],
                                                   bar_x[i+1])for i in range(bar_num)])
    plt2.xlabel('t/ms')
    plt2.ylabel('count')
    for bar in BarGraphs:
        height = bar.get_height()
        plt2.text(bar.get_x()+bar.get_width()/2-0.2, height+0.4, '%s' % int(height), size=10)  # 为每个条形图添加文本
    plt2.title(' IO \'s   responding   time ')
    plt2.show()


def GetMax(result_cel: DataFrame):
    MaxValue = round(max(result_cel['diff']*1000), 6)
    return MaxValue


def GetMin(result_cel: DataFrame):
    MinValue = round(min(result_cel['diff']*1000), 6)
    return MinValue


def GetCounts(result_cel: DataFrame):
    Counts = len(result_cel['diff'])
    return Counts


def GetAverage(result_cel: DataFrame):
    value = result_cel['diff']*1000
    counts = len(value)
    sum_value = sum(value)
    average = round(sum_value / counts, 6)
    return average
