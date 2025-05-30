import dealFile
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

import pandas as pd
from pandas import DataFrame


def DrawPlot(result_cel: DataFrame):
    x = result_cel.index
    y = result_cel['diff'] * 1000
    myexcel1 = plt.figure()
    plt.plot(x, y, 'bo', linestyle='-', linewidth=0.5, markersize=3)
    plt.ylim(0, 100)
    plt.show()
    return myexcel1


def DrawBargraph(result_cel: DataFrame):
    value = round(result_cel['diff'] * 1000, 1)  # 对数据进行四舍五入，小数点保留一位
    num_bins = 10
    # 计算最大值和最小值
    min_val = min(value)
    max_val = max(value)
    # 计算每个区间的宽度
    interval_width = (min_val + max_val) / num_bins
    # 给x轴赋值
    axis_x = [min_val + i * interval_width for i in range(num_bins)]
    axis_x.append(max_val)
    counts = {axis_x_start: 0 for axis_x_start in axis_x[:-1]}
    for d in value:
        for axis_x_start in axis_x[:-1]:
            if axis_x_start <= d < axis_x[axis_x.index(axis_x_start) + 1]:
                counts[axis_x_start] += 1

    ###### 绘制柱状图########
    mybar = plt2.bar(
        range(
            1,
            num_bins + 1),
        counts.values(),
        align='center',
        width=0.5)
    plt2.xticks(range(1,
                      num_bins + 1),
                ['[{:.1f}-{:.1f})'.format(axis_x[i],
                                          axis_x[i + 1]) for i in range(num_bins)])
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
    plt2.title('I/O \'s responding time')

