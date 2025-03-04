# encoding: utf-8
# @File  : numpy_logistic_example_train.py
# @Author: GUIFEI
# @Desc :  numpy 实现逻辑回归示例训练
# @Date  :  2025/03/04

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

'''
定义模型运算函数，将线性方程计算结果转换为概率模型
'''
def forward(theta, x, bias):
    # 定义线性方程组
    Z = np.dot(theta, x.T) + bias
    # 使用sigmoid 函数将线性方程计算结果转化为概率模型
    y_hat = 1 / (1 + np.exp(-Z))
    return y_hat

'''
定义损失函数，注意需要添加一个极小值，避免出现log 0 的情形
'''
def loss_fun(y_hat, y):
    e = 1e-8
    # 定义损失函数，此处加 e 是为了避免log 0 的情况出现，因为在log 0是没有意义的
    return -y * np.log(y_hat + e) - (1 - y) * np.log(1 - y_hat + e)

'''
计算梯度（权重）及 截距（bias）
'''
def calc_gradient(x, y, y_hat):
    m = x.shape[-1]
    delta_theta = np.dot((y_hat - y), x) / m
    delta_b = np.mean(y_hat - y)
    return delta_theta, delta_b

def train(theta, bias, x, y, iter_num):
    iter = 0
    while iter < iter_num:
        # 2. 模型运算
        y_hat = forward(theta, train_X, bias)
        # 3. 计算损失的均值
        loss = np.mean(loss_fun(y_hat, train_y))
        # 4. 计算梯度
        dw, db = calc_gradient(train_X, train_y, y_hat)
        # 5. 更新参数
        theta = theta - lr * dw
        bias = bias - lr * db
        iter += 1

if __name__ == '__main__':
    # 定义模型初始参数
    # 定义theta 其实参数符合标准正太分布 （均值0，标准差1）的随机数
    theta = np.random.randn(1, 20)
    # 截距
    bias = 0
    # 学习率
    lr = 0.001
    # 模型训练轮数
    iter_num = 1e4
    # 加载数据
    train_X = np.load("train_X.npy")
    train_y = np.load("train_y.npy")
    # 开始训练
    train(theta, bias, train_X, train_y, iter_num)
    # 保存训练后得到的权重参数、截距参数
    np.save("numpy_theta.npy", theta)
    np.save("numpy_bias.npy", bias)
    print("训练结束，模型参数保存完毕")
