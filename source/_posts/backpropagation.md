---
title: 无痛入门神经网络(2) 反向传播
date: 2017-07-15 20:36:00
tags:
  - deep learning
  - machine learning
  - data mining
categories: algorithms
---

## 引子
> Lolita, light of my life, fire of my loins. My sin, my soul. 

上次讲感知器的时候有提到，由于感知器是线性的且只有两层,所以我们需要一个非线性的多层的神经网络。但随之而来的问题就是如何去训练一个这样复杂的神经网络。深度学习的本质是通过输入和输出得到一个拟合曲线，所以如果我们找到了输出误差和权重之间的变化关系（也就是偏函数），我们就可以利用梯度下降等算法找到最优解，而反向传播就是一个高效寻找输出误差和权重变化关系的算法。

## 非线性的神经元
为了构建一个非线性的多层神经网络，我们需要做两件事情，第一是将训练的规则从线性推广到非线性，第二个是增加神经网络的层数,我们先做第一步。
* sigmoid 函数
在这里我介绍一种非线性函数，sigmoid 它的定义如下:
$$
y = \frac{1}{1+e^{-z}}\ 
$$
选用sigmoid 函数的其中一 个原因是它的导函数很简单,方便我们后面的解释:
$$
\frac{\partial y}{\partial z} = z(1-z)
$$
需要注意，非线性的激活函数有很多种，比如relu函数，tanh函数等等。

## 反向传播算法
现在我们已经有了非线性的激活函数，我们只要在多层的非线性神经元上找到输出误差和权重的导数关系，就可以完成神经网络的训练。

反向传播的本质是理由求导的链式法则高效地解出输出误差和权重的偏函数，下面我用对某一层求解来说明这个过程。
![backpropagation](http://7xq2dq.com1.z0.glb.clouddn.com/WechatIMG503-min.jpeg)
图中yj表示j层神经元的输出，zj表示j层神经元的数据， yi表示i层神经元的输出,我们用wij来表示i层到j层的权重向量
我们已经知道我们目标是求出输出误差(E)和权重变化(wij)的关系(偏导数)，由链式法则我们可以知道

![derivatives](http://7xq2dq.com1.z0.glb.clouddn.com/WechatIMG265-min.jpeg)
这样我们就明白了反向传播就是利用了链式求导的性质，每次都是通过后一层的误差来计算前一层的误差，这样就避免了重复计算某一层的误差多次。从而节约了计算量，让大规模的神经网络有了可以被计算的可能。

# 代码实现
明白了反向传播的本质就是链式求导+梯度下降之后，我们来尝试自己实现一遍反向传播算法。

数据集可以用上次在讲感知器时候最后提到的异或问题,即判断两个输入x1,x2是否一致。
```python
import numpy as np
np.random.seed(1)
# 生成输入向量X
X = np.array(
    [[0,0,1],
     [0,1,1],
     [1,0,1],
     [1,1,1]]
)
# 生成目标向量y
y = np.array(
    [[0],
     [1],
     [1],
     [0]]
)

# 定义sigmoid 和它的导函数
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# 随机生成初始的随机向量 
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

# 一开始我们先来5万次循环吧:)
for j in xrange(50000):

# 在反向传播前先正向传播，计算出每一层的输出
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # 计算出输入层和目标向量的差值(输出误差)
    l2_error = y - l2

    # 每循环一万次，打印一次输出误差的数值
    if (j% 10000) == 0:
        print "Error:" + str(np.mean(np.abs(l2_error)))
        print(l2)

    # 计算输出层的误差
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # 计算前一层对后一层的误差影响
    l1_error = l2_delta.dot(syn1.T)

    # 计算输入层对整体的误差
    l1_delta = l1_error * nonlin(l1,deriv=True)

    # 修改权重向量让结果越来越逼近目标向量 
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

```
如果你执行了上面的代码，你会发现这种非线性的多层神经网络成功地解决了感知器无法解决的异或问题，当输入x1，x2 相同时，会输出0，不相同时，会输出1。但是我们学习反向传播和神经网路肯定不是来解决，这么简单的异或问题的。下一次我就来讲一下关于神经网络在文字识别上的应用。










