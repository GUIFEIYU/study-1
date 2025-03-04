# encoding: utf-8
# @File  : numpy_logistic_example_test.py
# @Author: GUIFEI
# @Desc : numpy 实现逻辑回归示例测试
# @Date  :  2025/03/05
import numpy as np
import numpy_logistic_example_train as npl

def predict(x):
    y_hat = npl.forward(theta, x, bias)[0]
    if y_hat > 0.5:
        return 1
    else:
        return 0

def test(theta, bias, x, y):
    m = x.shape[0]
    correct_predictions = []
    for i in range(m):
        trueValue = y[i]
        prediction = predict(x[i])
        print(f'预测值：{prediction} 真实值：{trueValue}')
        if prediction == trueValue:
            correct_predictions.append(y[i])
    # 计算预测结果的准确率
    correct_rete = len(correct_predictions) / m
    print(correct_rete)


if __name__ == '__main__':
    # 加载训练好的模型参数
    theta = np.load("numpy_theta.npy")
    bias = np.load("numpy_bias.npy")
    test_y = np.load("test_y.npy")
    test_X = np.load("test_X.npy")
    test(theta, bias, test_X, test_y)

