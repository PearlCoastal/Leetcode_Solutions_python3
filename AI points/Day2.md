## 1.   逻辑回归相比线性回归，有何异同

- 线性回归：假设**因变量**和**自变量**之间是有**线性关系**的。

    例子：
    监督学习中，数据集包括：**一列观测 y 因变量**，和 **多列特征 X 自变量** 组成。
    线性回归的目的就是找到和样本拟合程度最佳的线性模型，在寻找过程中需要确定 **系数β** 和 **干扰项ε**。
    找到了最优的 **β** 和 **ε**，就找到了最优的模型。

    线性回归的公式：    y = Xβ + ε
    参数估计方法：最小二乘法（最小化预测 + 实际之间的欧氏距离）
  
    --> 将线性回归应用到分类问题中，比如二分类问题：将 X 对应的 y 分为 类别0 和 类别1。但是线性回归本身的输出是连续的，随意要用单位阶跃函数映射到{0， 1}

- 逻辑回归：广义线性回归 中的一种以 **对数几率函数** 为联系函数的特例。联系函数： Sigmoid()

    参数估计方法：极大似然法（通过最大化预测属于实际的概率来最小化预测和实际之间的距离）

- 线性回归 和 逻辑回归 的**区别和联系**
    1.  都是 广义线性回归模型的特例
    2.  线性回归只能用于 **回归问题**，逻辑回归用于**分类问题**
    3.  线性回归没有联系函数，逻辑回归的联系函数是 **对数几率函数** 属于 Sigmoid()
    4.  参数估计方法：线性回归-**最小二乘法**，逻辑回归-**极大似然法**

补充小知识：
    逻辑回归中的逻辑 Logistic 其实来自 Logarithm：对数，与其叫逻辑回归，不如说是：**对数几率回归**


## 2.   回归问题常用的性能度量指标

- 均方误差：

- RMSE均方根误差：

- SSE和方误差：

- MAE：

- MAPE：

- 平均平方百分比误差：

- 决定系数：

## 3.   分类问题常用的性能度量指标

- 混淆矩阵(Confuse Matrix): 更好的理解分类中的错误：TP/TN/FP/FN(针对二分类问题)
![image](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/img-folder/ConfuseMatrix.png)

- 准确率(Accuracy): 所有样本中预测正确的样本占比    
                    
    Accuracy = (TP + TN)/(TP + TN + FP + FN)

- 错误率(Error Rate):   所有样本中预测错误的样本占比

    Error Rate = 1 - Accuracy = (FP + FN) / (TP + TN + FP + FN)

- 精确率(Precision):    在所有预测为正的样本中实际为正样本的概率

    Precision = TP / (TP + FP)

- 召回率(Recall):   在实际为正样本中被预测为正样本的概率
    
    Recall = TP / (TP + FN)

- F1 Score: 通常使用Precision 和 Recall两个指标，来评价二分类模型的效果。但是 Precision 和 Recall指标 有时是此消彼长的，为了兼顾 P 和 R，用F-Measure 来加权调和平均。

    β = 1时，即为 F1 Score = (2*P*R) / (P + R)

    F1 较高时，模型的性能越好。


- ROC(Receiver Operating Charactersitic Curve): 

- AUC(Area under Curve):    曲线下面积，AUC面积值越大，模型的准确度越高。

![image](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/img-folder/AUC.png)

- KS曲线(Kolmogorov-Smirnov): 模型的风险区分能力

- Lift值：指与不利用模型相比，模型的预测能力变好了多少。用该模型 与 没有该模型(随机选择)所得出的结果的壁纸，lift应该要 > 1， 而且lift越大，说明预测效果越好。

- P-R曲线：(Precision Recall Curve):    Precision 和 Recall 之间的关系

![image](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/img-folder/PRCurve.png)


## 4.   逻辑回归的损失函数

- 0-1损失函数(0-1 loss function):

                
    L(Y, f(x)) =  1, Y != f(x)
                  0, Y == f(x)

- 平方损失函数(quadratic loss function):

    L(Y, f(x)) = (Y - f(x))^2

- 绝对值损失函数(absolute loss function):

    L(Y, f(x)) = |Y - f(x)|

- 对数损失函数(logarithmic loss function):

    L(Y, P(Y|X)) = -logP(Y|X)


## 5.   逻辑回归处理多标签分类问题时，一般怎么做

- 根据 k 个类别，都建立一个 二分类 的逻辑回归分类器。第 i 个分类器泳衣区分每个样本是否可以归位第 i 类，训练该分类器时， 需要把标签重新整理为 “第i类标签” 与 “非第i类标签” 2类。

- softmax回归：修改逻辑回归的损失函数，让损失函数适应多分类问题。使损失函数不再只考虑二分类问题的 0/1 损失，而是具体考虑 每个样本标记的损失。


## 6.   全概率公式，贝叶斯公式

- 全概率公式：

    事件 B1, B2, B3...Bn 是样本空间的一个划分
    P(A) = P(A|B1)P(B1) + P(A|B2)P(B2) + P(A|B3)P(B3) +...+ P(A|Bn)P(Bn)

- 贝叶斯公式：

    P(A|B) = P(B|A)P(A) / P(B)

## 7.   朴素贝叶斯为什么“朴素”

朴素贝叶斯 假设样本的特征之中彼此独立，没有相互关系。

    例子：如果一种水果具有 红，椭圆形，直径约3英寸等特征，则可以判定为苹果。
    尽管这些特征相互依赖或者有些特征有其他特征决定，但是朴素贝叶斯认为这些属性在判定该水果是否为苹果的概率分布上是独立的。

朴素贝叶斯适合预测基于各属性的不用累的概率，在文本分类上有广泛应用。

