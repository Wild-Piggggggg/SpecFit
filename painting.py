"""本文件的功能为绘制设计谱和目标谱的曲线"""

"""导入数据处理库和绘图库"""
import numpy as np
import matplotlib.pyplot as plt

class Painting:
    def __init__(self):
        # 初始化
        self.fig = plt.figure(figsize=(5, 4))


    def draw(self, path_pre, path_fit, data_num, head_cal):
        # 先绘制原反应谱，再绘制设计谱
        # path_pre是反应谱
        # path_fit是设计谱
        # print(data_num)
        fre_list_pre = []
        acc_list_pre = []
        with open(path_pre, 'r') as f:
            if head_cal:
                content = f.readlines()
            else:
                content = f.readlines()[1:]
            n = len(content)
                
            for i in range(n):
                string = content[i].strip().replace("\t", ",").split(',')
                fre = float(string[0])
                acc = float(string[1])
                fre_list_pre.append(fre)
                acc_list_pre.append(acc)

        fre_list_fit = []
        acc_list_fit = []
        with open(path_fit, 'r') as f:
            content = f.readlines()
            n = len(content)
            for i in range(n - data_num, n):
                string = content[i].strip().replace("        ", ",")
                fre = float(string[:-7])
                acc = float(string[-6:])
                fre_list_fit.append(fre)
                acc_list_fit.append(acc)

        return np.array(fre_list_pre), np.array(acc_list_pre), np.array(fre_list_fit), np.array(acc_list_fit)
        # plt.plot(fre_list_pre, acc_list_pre, label='Design Response Spectra', color='b')
        # plt.plot(fre_list_fit, acc_list_fit, label='Seismic Response Spectra', color='r')
        # plt.xscale('log')
        # plt.xlabel("Frequency")
        # plt.ylabel("Acceleration")
        # plt.legend(loc=1)
        # plt.grid()
        # plt.show()

# path = "./running/output_simqke.dat"
# path1 = 'C:\\Users\\Red Fox\\Desktop\\目标谱.txt'
# Painting().draw(path, path1)
