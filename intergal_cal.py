
"""此程序用于进行积分"""

# 导入数据处理库
import numpy as np
import pandas as pd
from scipy.integrate import cumtrapz
import time


class Intergal:
    # 看看有什么需要初始化的
    def __init__(self):
        self.state = 'OK'  # 是的我很好

    def DataTrans(self, data, dt, ConversionType, DataType):
        # 数据转换,函数外提前将data转为array类型，加速度的单位是g
        # 输入: 数据:离散数据，加速度单位应为g，单位为
        # 速度单位为米 / 秒，位移单位为米
        # Dt: 离散数据的时间间隔
        # ConversionType: 用户定义的转换类型
        # 'a2v'
        # 加速度比速度
        # 'v2d'
        # 速度到位移
        # DataType: 用户自定义类型
        # acc的加速度
        # “或者”veloecity
        # 输出: 速度和位移的时间序列

        # s=time.time()

        if DataType == 'acc':
            data = 9.81 * data

        nosamples = len(data)
        newdata = np.zeros(nosamples)

        if ConversionType == 'a2v' or ConversionType == 'v2d':
            t = np.linspace(0, dt * nosamples, nosamples)
            newdata = cumtrapz(data, t)
        # e=time.time()
        # print(f'执行完DataTrans的时间为{e - s}')
        return newdata

    def earPar(self, GMpar, data, dt, zeta):
        # data还是array对象
        # 此代码用于计算地震动参数;
        # 这些地震动参数可以在生成时程时使用
        # % 输入: GMpar
        # '你想计算的强运动参数
        # 'pga' - 峰值地面加速度，其单位为g
        # 'pgv' - 峰值地面速度，其单位为厘米 / 秒
        # 'pgd'——峰值地面位移，单位为cm
        # 'epa' - 有效峰值加速度，单位是g
        # 手臂 - 加速度的均方根，它的单位是g
        # “si”——反应谱强度(Housner, 1959)，其单位为cm
        # 'cav' - 累计绝对速度，单位为cm / sec
        # 'arias' - Arias强度(arias, 1970)，单位为cm / sec
        # 数据——加速度时间历程，单位为: g
        # Dt——加速度时程的时间间隔，单位为SEC

        # s=time.time()
        type_list = ['pga', 'pgv', 'pgd', 'epa', 'arms', 'si', 'cav', 'arias']
        if GMpar not in type_list:
            print("the string 'GMpar' you input is not correct, please change your input")
            return
        number = len(data)
        PGA = max(abs(data))
        vel = self.DataTrans(data, dt, 'a2v', 'acc')
        PGV = max(abs(vel)) * 100
        dis = self.DataTrans(vel, dt, 'v2d', 'vel') * 100
        PGD = max(abs(dis))

        Td = number * dt
        ss = sum(data * data * dt)
        kk = sum(abs(data) * 9.81 * 100 * dt)

        Arms = np.sqrt(ss / Td)
        CAV = kk

        T, Spv = self.spect(dt, zeta, data)
        DT = T[1] - T[0]
        ss = 0
        for i in range(0, 999):
            ss = ss + (Spv[i] + Spv[i + 1]) / 2 * DT

        SI = ss
        ArI = self.AriasInt(data, dt) * 100
        effPGA = self.EFF_PGA(dt, zeta, data)

        ground_motion_parameter = [PGA, PGV, PGD, effPGA, Arms, SI, CAV, ArI]

        # e=time.time()
        # print(f'执行完earpar的时间为{e - s}')
        return ground_motion_parameter

    def spect(self, dt, zeta, data):
        # s=time.time()
        data = 9.81 * 100 * data
        NN = 1000
        T = np.linspace(0.1, 2.5, NN)
        N = len(data)
        omega0 = 2 * np.pi / T
        omegaD = omega0 * np.sqrt(1 - zeta ** 2)
        Spv = np.zeros(NN)

        """尝试重写"""

        A_s = np.exp(-zeta * omegaD * dt) * (zeta / np.sqrt(1 - zeta ** 2) * np.sin(omegaD * dt) + np.cos(omegaD * dt))
        B_s = np.exp(-zeta * omegaD * dt) * (1 / omegaD * np.sin(omegaD * dt))
        C_s = 1 / omega0 ** 2 * (2 * zeta / (omegaD * dt) + np.exp(-zeta * omegaD * dt) * (
                ((1 - 2 * zeta ** 2) / (omegaD * dt) - zeta / np.sqrt(1 - zeta ** 2)) * np.sin(omegaD * dt) - (
                    1 + 2 * zeta / (omegaD * dt)) * np.cos(omegaD * dt)))
        D_s = 1 / omega0 ** 2 * (1 - 2 * zeta / (omegaD * dt) + np.exp(-zeta * omegaD * dt) * (
                (2 * zeta ** 2 - 1) / (omegaD * dt) * np.sin(omegaD * dt) + 2 * zeta / (
                omegaD * dt) * np.cos(omegaD * dt)))
        AA_s = -np.exp(-zeta * omegaD * dt) * (omegaD / np.sqrt(1 - zeta ** 2) * np.sin(omegaD * dt))
        BB_s = np.exp(-zeta * omegaD * dt) * (
                np.cos(omegaD * dt) - zeta / np.sqrt(1 - zeta ** 2) * np.sin(omegaD * dt))
        CC_s = 1 / omega0 ** 2 * (-1 / dt + np.exp(-zeta * omegaD * dt) * (
                (omegaD / np.sqrt(1 - zeta ** 2) + zeta / (dt * np.sqrt(1 - zeta ** 2))) * np.sin(
            omegaD * dt) + 1 / dt * np.cos(omegaD * dt)))
        DD_s = 1 / (omega0 ** 2 * dt) * (1 - np.exp(-zeta * omegaD * dt) * (
                zeta / (1 - zeta ** 2) * np.sin(omegaD * dt) + np.cos(omegaD * dt)))

        for i in range(NN):
            u = np.zeros(N)
            v = np.zeros(N)
            ac = np.zeros(N)
            A = A_s[i]
            B = B_s[i]
            C = C_s[i]
            D = D_s[i]
            AA = AA_s[i]
            BB = BB_s[i]
            CC = CC_s[i]
            DD = DD_s[i]
            v[0] = DD * (-data[0])
            u[0] = D * (-data[0])
            ac[0] = -2 * omega0[i] * zeta * v[0] - omega0[i] ** 2 * u[0]
            v[1:N] = AA * u[0:N - 1] + BB * v[0:N - 1] + CC * (-data[0:N - 1]) + DD * (-data[1:N])
            u[1:N] = A * u[0:N - 1] + B * v[0:N - 1] + C * (-data[0:N - 1]) + D * (-data[1:N])
            ac[1:N] = -2 * omega0[i] * zeta * v[1:N] - omega0[i] ** 2 * u[1:N]
            Spv[i] = max(abs(v))
        # e=time.time()
        # print(f'执行完spect的时间为{e - s}')
        return T, Spv

    def AriasInt(self, acc, dt):
        # pi = np.pi
        # s=time.time()
        num = np.pi / (2.0 * 9.81)
        npts = len(acc)
        arias0 = np.zeros(npts)
        acc = [i * 9.81 for i in acc]
        for i in range(npts):
            arias0[i] = acc[i] ** 2 * num * dt
        ArI = sum(arias0)
        # e=time.time()
        # print(f'执行完ArisInt的时间为{e - s}')
        return ArI

    def EFF_PGA(self, dt, zeta, data):
        # s=time.time()
        NN = 500
        T = np.linspace(0.1, 0.5, NN)  # 为何这样定义
        N = len(data)
        omega0 = 2 * np.pi / T
        # omega0 = [2 * np.pi / i for i in T]
        omegaD = np.sqrt(1 - zeta ** 2) * omega0
        # omegaD = [i * np.sqrt(1 - zeta ** 2) for i in omega0]
        Spa = np.zeros(NN)

        """尝试重写"""
        A_s = np.exp(-zeta * omegaD * dt) * (zeta / np.sqrt(1 - zeta ** 2) * np.sin(omegaD * dt) + np.cos(omegaD * dt))
        B_s = np.exp(-zeta * omegaD * dt) * (1 / omegaD * np.sin(omegaD * dt))
        C_s = 1 / omega0 ** 2 * (2 * zeta / (omegaD * dt) + np.exp(-zeta * omegaD * dt) * (
                ((1 - 2 * zeta ** 2) / (omegaD * dt) - zeta / np.sqrt(1 - zeta ** 2)) * np.sin(omegaD * dt) - (
                1 + 2 * zeta / (omegaD * dt)) * np.cos(omegaD * dt)))
        D_s = 1 / omega0 ** 2 * (1 - 2 * zeta / (omegaD * dt) + np.exp(-zeta * omegaD * dt) * (
                (2 * zeta ** 2 - 1) / (omegaD * dt) * np.sin(omegaD * dt) + 2 * zeta / (
                omegaD * dt) * np.cos(omegaD * dt)))
        AA_s = -np.exp(-zeta * omegaD * dt) * (omegaD / np.sqrt(1 - zeta ** 2) * np.sin(omegaD * dt))
        BB_s = np.exp(-zeta * omegaD * dt) * (
                np.cos(omegaD * dt) - zeta / np.sqrt(1 - zeta ** 2) * np.sin(omegaD * dt))
        CC_s = 1 / omega0 ** 2 * (-1 / dt + np.exp(-zeta * omegaD * dt) * (
                (omegaD / np.sqrt(1 - zeta ** 2) + zeta / (dt * np.sqrt(1 - zeta ** 2))) * np.sin(
            omegaD * dt) + 1 / dt * np.cos(omegaD * dt)))
        DD_s = 1 / (omega0 ** 2 * dt) * (1 - np.exp(-zeta * omegaD * dt) * (
                zeta / (1 - zeta ** 2) * np.sin(omegaD * dt) + np.cos(omegaD * dt)))

        for i in range(NN):
            u = np.zeros(N)
            v = np.zeros(N)
            ac = np.zeros(N)
            A = A_s[i]
            B = B_s[i]
            C = C_s[i]
            D = D_s[i]
            AA = AA_s[i]
            BB = BB_s[i]
            CC = CC_s[i]
            DD = DD_s[i]
            v[0] = DD * (-data[0])
            u[0] = D * (-data[0])
            ac[0] = -2 * omega0[i] * zeta * v[0] - omega0[i] ** 2 * u[0]
            v[1:N] = AA * u[0:N - 1] + BB * v[0:N - 1] + CC * (-data[0:N - 1]) + DD * (-data[1:N])
            u[1:N] = A * u[0:N - 1] + B * v[0:N - 1] + C * (-data[0:N - 1]) + D * (-data[1:N])
            ac[1:N] = -2 * omega0[i] * zeta * v[1:N] - omega0[i] ** 2 * u[1:N]
            Spa[i] = max(abs(ac))

        effPGA = sum(Spa) / len(Spa) / 2.5
        # e=time.time()
        # print(f'执行完eff_PGA的时间为{e - s}')
        return effPGA

    def read_data(self, file_name, head_cal, choice):
        #  choice的值取2或1,2代表紧接着设计谱生成的加速度谱积分，1代表新的积分文件
        #  读取加速度数据并计算、绘图
        #  最终需要得到的值有  三条折线的所有数据  地震动参数
        # s=time.time()
        
        content = pd.read_csv(file_name, header=None)
        # print(content[0][0])
        # print(type(content[0][0]))
        # print('')

        if len(str(content[0][0]).split()) != choice:
            state = False
            return state, False, False, False, False, False, False, False

        if head_cal:
            data = np.array(content).squeeze()
       
        else:
            data = np.array(content[1:]).squeeze()
        
        if choice==2:
            dt = float(content[0][0].split()[1])

            data = data.astype(np.float)
        else:
            dt = 0.005
        # print(f"choice=2 , dt={dt}")
        zeta = 0.05
        ground_motion_parameter = self.earPar('pgd', data, dt, zeta)
        # print(result)
        vel = self.DataTrans(data, dt, 'a2v', 'acc')
        dis = self.DataTrans(vel, dt, 'v2d', 'vel')
        times1 = len(data)
        times2 = len(vel)
        times3 = len(dis)
        t1 = np.linspace(dt, dt * times1, times1)
        t2 = np.linspace(dt, dt * times2, times2)
        t3 = np.linspace(dt, dt * times3, times3)
        # e=time.time()
        # print(f'执行完read_data的时间为{e - s}')
        state = True
        return state, ground_motion_parameter, t1, data, t2, vel, t3, dis


if __name__ == "__main__":
    example = Intergal()
    head_cal = True
    state, ground_motion_parameter, t1, data, t2, vel, t3, dis = example.read_data('C:\\Users\\Red Fox\Desktop\\时程分析文件.txt', head_cal, 0)
    print("done")
