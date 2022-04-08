# lingo
## lingo介绍
LINGO是Linear Interactive and General Optimizer的缩写，即“交互式的线性和通用优化求解器”，由美国LINDO系统公司（Lindo System Inc.）推出的，可以用于求解非线性规划，也可以用于一些线性和非线性方程组的求解等，功能十分强大，是求解优化模型的最佳选择。

其特色在于内置建模语言，提供十几个内部函数，可以允许决策变量是整数（即整数规划，包括 0-1 整数规划），方便灵活，而且执行速度非常快。能方便与EXCEL，数据库等其他软件交换数据。[^1]LINGO19.0为最新版本。
[^1]:百度百科https://baike.baidu.com/item/LINGO/8835111

## lingo下载
官网地址： https://www.lindo.com/
进入DOWNLOADA栏目下载合适的版本（通常都是选择”Download LINGO“
##  lingo函数
**1.  算数运算符**
+、-、*、/、^分别表示加减乘除及乘方
**2. 逻辑运符**
#not#:非
#eq#：相等
#ne#：不等
#gt#：大于
#ge#：大于或等于
#lt#：小于
#le#：小于或等于
#and#：和（且，交）
#or#：或（并）
==*lingo不区分大小写*==
==*逻辑运算不同于关系运算，逻辑运算仅用于判断一个关系是否满足，即得到的结果为真假（True或False）*==
**3. 关系运算符**
等于、大于或等于、小于或等于分别用“=”、“>=”、“<=”表示
==*lingo中没有严格的大于或者严格的小于，所以">"还是表示大于或等于*==
**4. 数学函数**
**==lingo中所有的数学函数前面都要加“@”==**
@abs(x):x的绝对值；
@sin(x)
@cos(x)
@tan(x)
@exp(x)
@log(x):以e为底的对数函数
@mod(x,y):x除以y的余数
@sign(x):符号函数
@floor(x):向下取整
@smax(x1,x2,...,xn):返回最大值
@smin(x1,x2,...,xn):返回最小值
**5. 变量界定函数**
@bin(x):0-1型变量
@bnd(L,xU):介于L和U之间的变量
@gin(x):整型变量
@free(x):自由变量，即x为任意实数
==*如果不做说明，则x为非负实数*==
**6. 其他函数，遇到时再具体说明**

## lingo的基本操作
### 注意事项
- lingo不区分大小写
- lingo中注释使用“！”
- lingo不读取空格
- lingo每行后面需要加分号，注释语句特别注意加“；”
- lingo中默认的变量为非负
- lingo中的矩阵式按行存储，即x,y=1,2,3,4的意思式x=1,3,y=2,4，这和matlab、python的习惯都不一样
- lingo中数据部分不是使用分数
### lingo编程
 lingo程序以**model**开始（但也可以省略），一个程序基本上可以分为三大部分：
#### 集合，主要用于定义变量
sets……endsets的方式也被称为矩阵工厂，这种操作方式不仅可以简化变量的定义，在做for循环时也非常有效。
```lingo
sets:
set/list/:attribute;
demand/1..3/:a,b;
!定义了集合demand，其中3个变量，每个变量有2个属性a,b
c(set,demand):x;
endsets
```
程序中前面两行生成的是一维矩阵，通过c(set,demand)可以实现二位甚至更高维的矩阵,其中c是任意起的名字，即将两个工厂set和demand合并成一个大工厂c。


**派生集合中一定要注意行列关系**

#### 数据，主要提供数据
此部分的主要目的是为矩阵工厂定义的矩阵提供具体的数值。
```lingo
data:
属性1=数据列表;
属性2=数据列表;
enddata
```
#### 变量初始化（init），在给定初值时才会用到该部分
```lingo
init:
	 x,y = 0,1;
endinit
```
#### 目标与约束
```lingo
max = 3*x1+2*x2-5*x1^2;
x1+x2 <=20;
@gin(x1);
```
## Example 1
关于矩阵工厂和函数的应用。
已知$a_i = i,i=1,2,3,4,5$,求$\sum_{i=1}^5 \frac{1}{a_i}$.
```lingo
sets:
set/1..5/:a,x;
endsets
data:
a = 1,2,3,4,5;
enddata
@for(set(i):1/a(i)=x(i));
s = @sum(set:x);
```
**通常可以通过设置一些变量，实现类似的运算**
已知$a_i = i, i= 1,2,3,4,5$,且$\sum_{i=1}^5 x_i = 5000$,求$max S = a_i*x_i, i=1,2,3,4,5$. [^2]
[^2]:https://blog.csdn.net/weixin_45755332/article/details/107355499
```lingo
model: 
sets: gc /1..5/  : a,x; 
endsets 
data: 
a =  1,2,3,4,5; 
enddata 
max = S; 
@for(  gc(i)  :  a(i)*x(i)  = S ); 
@sum(  gc(i)  :  x(i)  )  =  5000; 
end
```
**思考:** 条件不变，如何计算$max S = \sum_{i=1}^5 a_i*x_i$
```lingo
model:
sets:
gc /1..5/ : a,x,S;
endsets
data:
a = 1,2,3,4,5;
enddata
max = @sum(gc:S);
@for( gc(i) : a(i)*x(i) = S(i) );
@sum( gc(i) : x(i) ) = 5000;
end
```

## Example 2
**问题** 有6个建筑工地，已知其位置$(a,b)$及其水泥用量$d$如表中所示。
(1) 假设有两个临时料场位于$P(5,1)$及$Q(2,7)$，它们的日储量均为20吨。设置合理的运输方案，使得吨千米数最小。
(2) 如果要新建两个料场，则该选址何处，使得吨千米数最小。
表1 建筑工地的位置及其日水泥需求量
| 工地 | 1    | 2    | 3    | 4    | 5   | 6    |
| ---- | ---- | ---- | ---- | ---- | --- | ---- |
| $a$  | 1.25 | 8.75 | 0.5  | 5.75 | 3   | 7.25 |
| $b$  | 1.25 | 0.75 | 4.75 | 5    | 6.5 | 7.75 |
| $d$  | 3    | 5    | 4    | 7    | 6   | 11   |
**假设**
 运费只和吨公里数有关
**符号**
设建筑工地的位置为$(a_i,b_i),i=1,2,...,6$，水泥用量为$d_i,i=1,2,...,6$，料场位置为$(x_j,y_j),j=1,2$，日储存量为$z_j,j=1,2$；从料场j到建筑工地i的运算量为$c_{ij}$。
**模型**
由题意可知，
$$
\begin{aligned}
 &min f=\sum_{j=1}^2 \sum_{i=1}^6c_{ij}\sqrt{(x_j-a_i)^2 +(y_j-b_i)^2} \\
  &s.t ~~~~~~~ \sum_{j=1}^2 c_{ij}= d_i, ~i=1,2,...,6\\
&\quad ~~~~~~~ \sum_{i=1}^6 c_{ij}\le z_j ,~j = 1,2 \\
&\quad ~~~~~~~ c_{ij}\ge 0,~i=1,2,...,6;j=1,2
& \end{aligned}
 $$
 **lingo求解**
 ```lingo
 sets:
     demand/1..6/:a,b,d;
! 工地;
     supply/1..2/:x,y,z;
!料场;
     link(demand,supply):c;
!运输量，由工地和料场构造的派生集，6行2列;
 endsets
 
data:
     a = 1.25,8.75,0.5,5.75,3,7.25;
     b = 1.25,0.75,4.75,5,6.5,7.75;
     d = 3,5,4,7,6,11;
	z = 20,20;
     x = 5,2;
     y = 1,7;
 enddata
  
 [OBJ] min=@sum(link(i,j):c(i,j)*((y(j)-b(i))^2+(x(j)-a(i))^2)^(1/2));
 ![OBJ]中的内容不影响程序的运行，只是为了提高可读性,可以删除;
 @for(demand(i):@sum(supply(j):c(i,j))=d(i));
 @for(supply(j):@sum(demand(i):c(i,j))<=z(j));
 @for(supply:@free(x);@free(y));
 ```
运行程序，显示最小吨千米数为136.2275，进一步可以读取
|Variable| Value| Reduced Cost|
|--------|--------|---------|
| C( 1, 1) | 3.000000 | 0.000000|
| C( 1, 2) | 0.000000 | 3.852207|
| C( 2, 1) | 5.000000 | 0.000000|
| C( 2, 2) | 0.000000 | 7.252685|
| C( 3, 1) | 0.000000 | 1.341700|
| C( 3, 2) | 4.000000 | 0.000000|
| C( 4, 1) | 7.000000 | 0.000000|
| C( 4, 2) | 0.000000 | 1.992119|
| C( 5, 1) | 0.000000 | 2.922492|
| C( 5, 2) | 6.000000 | 0.000000|
| C( 6, 1) | 1.000000 | 0.000000|
| C( 6, 2) | 10.00000 | 0.000000|
通过 `Solver Status` 知道，该模型为一个线性规划模型（`LP`）。
**问题（2）中料场的位置变成了未知量**，此时只要删除模型中对 x，y 进行赋值的语句，就可以得到相应问题的解，最小吨千米数为 85.26604，料场的坐标为 `(3.254883,5.652332)` 和 `(7.250000,7.750000)`;而根据`Solver Status` 知道，该模型为一个非线性规划模型（`NLP`），解是一个局部最优解 `Local Opt`.
事实上，在解决非线性规划时，通常可以设置**初始值**，`Lingo` 中用 `init:... endinit`标识初值，如果对上述问题设置初值的话，程序为
```lingo
sets:
     demand/1..6/:a,b,d;
     supply/1..2/:x,y,z;
     link(demand,supply):c;
 endsets
 data:
     a = 1.25,8.75,0.5,5.75,3,7.25;
     b = 1.25,0.75,4.75,5,6.5,7.75;
     d = 3,5,4,7,6,11;
     z = 20,20;
 enddata

 init:
     x = 5,2;
     y = 1,7;
 endinit

 [OBJ] min=@sum(link(i,j):c(i,j)*((y(j)-b(i))^2+(x(j)-a(i))^2)^(1/2));
 ![OBJ]中的内容不影响程序的运行，只是为了提高可读性,可以删除;
 @for(demand(i):@sum(supply(j):c(i,j))=d(i););
 @for(supply(j):@sum(demand(i):c(i,j))<=z(j););
 @for(supply:@free(x);@free(y););
```

 ## 读取结果
  - Local optimal solution found：局部最优解，或者出现Global optimal solution found(全局最优解）
  -   Objective value:  目标值
  -   Infeasibilities:   矛盾的约束数目，理想值是0
  -   Total solver iterations:    迭代次数
  -   Variable：变量名
  -    Value：最优解对应的变量的值
  -    Reduced Cost：变量增加1个单位，目标值付出的代价，如果该值为2则意味着变量增加1，目标值就要减少（max问题中）或增加（min问题中）2；
  - Row：约束条件序号，其中1为目标函数
  - Slack or Surplus：松弛（过剩）变量，约束条件右边剩余（min问题）或超过（max问题）的量。
  - Dual Price：影子价格，约束条件右边的部分增加一个单位，目标值改变的数量（max中增大，min中减小）

## 灵敏度分析
1. 打开solver中的options选项
2. 找到options中的General Solver
3. 找到Dual Computations一栏，将状态调整为Prices&Ranges点击OK。
4. 写好代码以后，按Ctrl+r
5. 灵敏度分析报告如下：
   ```
   Ranges in which the basis is unchanged:

                                      Objective Coefficient Ranges
                                  Current        Allowable        Allowable
                Variable      Coefficient         Increase         Decrease
                C( 1, 1)         3.758324         3.852207         INFINITY
                ...  ...
                                        Righthand Side Ranges
                     Row          Current        Allowable        Allowable
                                      RHS         Increase         Decrease
                       2         3.000000         4.000000         3.000000

     ```
     其中，`Objective Coefficient Ranges` 给出了最优解不变（最优值可能会变）的情况下，目标函数系数允许变化的范围： `Current Coefficient` 为模型中给定的系数，`Allowed Increase` 为系数允许增加的量，`Allowable Decrease` 表示允许减小的量，如C(1,1) 系数的的范围为（3.758324-infinity，3.758324 + 3.852207）————保证其它系数不变的情况下； `Righthand Side Ranges` （约束中右端项）：`Current RHS` 为模型中的约束右端项，如第一个约束（模型中的第2行）右端的值在（3-3，3+4）的范围内时最优基不变————其它约束条件不变的情况下。此时最优解和最优值可能会变化。

## Example 3
#### 问题
某工厂制造三种产品，生产这三种产品需要三种资源：技术服务、劳动力和行政管理，具体需求量如下：
|产品|技术服务|劳动力|行政管理|利润|
|---|---|---|---|---|
|A|1|10|2|10|
|B|1|4|2|6|
|C|1|5|6|4|

现有 100 h 的技术服务、600 h 的劳动力和 300 h 的行政管理时间可以使用，求最优产品品种规划，且回答一下问题：
（1） 若产品C值得生产的话，它的利润是多少？假使产品C的利润增加至 25/3 元，求获得最多利润的产品品种规划；

（2） 确定全部资源的影子价格；

（3） 制造部门提出建议，要生产一种新产品，该产品需要技术服务 1 h、劳动力 4 h 和行政管理 4 h。销售部门预测销售时有 8 元的单位利润。管理部门应该怎样决策？

（4） 假定该工厂至少生产 10 件产品C,试确定最优产品品种规划。

#### 符号假设
|symbols|Meaning|
|---|---|
|$x_i$|The number of product i(int)|
|$l_i$|Profit of i|
|$r_j$| The amount of resouce j|
|$c_{ij}$|The amount of resource j in Product i|

#### 模型
$$
max Z = \sum\limits_{i=1}^3 l_ix_i\\
s.t. \sum\limits_{i=1}^3 c_{ij}x_i \leq r_j,(j = 1,2,3)\\
     x_i \in N^*
$$

#### lingo求解
```{lingo}
sets:
product/1..3/:lr,x;
ziyuan/1..3/:zy;
link(ziyuan,product):c;
endsets

data:
lr = 10,6,4;
zy = 100,600,300;
c = 1,10,2,
    1,4,2,
    1,5,6;
enddata

max = @sum(product(i):lr(i)*x(i));
@for(ziyuan(j):@sum(link(i,j):c(i,j)*x(i))<=zy(j));
@for(product(i):@gin(x(i)));

```

#### 结果分析
运行上述程序，得到结果为：
```
Global optimal solution found.
  Objective value:                              732.0000
  Objective bound:                              732.0000
  Infeasibilities:                              0.000000
  Extended solver steps:                               0
  Total solver iterations:                             2


                       Variable           Value        Reduced Cost
                         LR( 1)        10.00000            0.000000
                         LR( 2)        6.000000            0.000000
                         LR( 3)        4.000000            0.000000
                          X( 1)        33.00000           -10.00000
                          X( 2)        67.00000           -6.000000
                          X( 3)        0.000000           -4.000000
                         ZY( 1)        100.0000            0.000000
                         ZY( 2)        600.0000            0.000000
                         ZY( 3)        300.0000            0.000000
                       C( 1, 1)        1.000000            0.000000
                       C( 1, 2)        10.00000            0.000000
                       C( 1, 3)        2.000000            0.000000
                       C( 2, 1)        1.000000            0.000000
                       C( 2, 2)        4.000000            0.000000
                       C( 2, 3)        2.000000            0.000000
                       C( 3, 1)        1.000000            0.000000
                       C( 3, 2)        5.000000            0.000000
                       C( 3, 3)        6.000000            0.000000

                            Row    Slack or Surplus      Dual Price
                              1        732.0000            1.000000
                              2        0.000000            0.000000
                              3        2.000000            0.000000
                              4        100.0000            0.000000
```
最优产品品种规划为：A 33 件；B 67 件；C 0 件。
回答其它问题，需要用到**灵敏度分析**，打开程序，并按下“Ctrl + r”，得到如下提示：
```
RANGE ANALYSIS NOT ALLOWED ON INTEGER PROGRAMMING MODELS.
```
整型规划不允许进行灵敏度分析！
为了顺利开展工作，可以改变假设，即允许产品数量是实型数值，程序改为如下形式：
```{lingo}
sets:
product/1..3/:lr,x;
ziyuan/1..3/:zy;
link(ziyuan,product):c;
endsets

data:
lr = 10,6,4;
zy = 100,600,300;
c = 1,10,2,
    1,4,2,
    1,5,6;
enddata

max = @sum(product(i):lr(i)*x(i));
@for(ziyuan(j):@sum(link(i,j):c(i,j)*x(i))<=zy(j));
!@for(product(i):@gin(x(i)));
```
程序运行结果为：
```
Global optimal solution found.
  Objective value:                              733.3333
  Infeasibilities:                              0.000000
  Total solver iterations:                             2


                       Variable           Value        Reduced Cost
                         LR( 1)        10.00000            0.000000
                         LR( 2)        6.000000            0.000000
                         LR( 3)        4.000000            0.000000
                          X( 1)        33.33333            0.000000
                          X( 2)        66.66667            0.000000
                          X( 3)        0.000000            2.666667
                         ZY( 1)        100.0000            0.000000
                         ZY( 2)        600.0000            0.000000
                         ZY( 3)        300.0000            0.000000
                       C( 1, 1)        1.000000            0.000000
                       C( 1, 2)        10.00000            0.000000
                       C( 1, 3)        2.000000            0.000000
                       C( 2, 1)        1.000000            0.000000
                       C( 2, 2)        4.000000            0.000000
                       C( 2, 3)        2.000000            0.000000
                       C( 3, 1)        1.000000            0.000000
                       C( 3, 2)        5.000000            0.000000
                       C( 3, 3)        6.000000            0.000000

                            Row    Slack or Surplus      Dual Price
                              1        733.3333            1.000000
                              2        0.000000            3.333333
                              3        0.000000           0.6666667
                              4        100.0000            0.000000

```
`Ctrl + r` 得到灵敏度分析报告如下：
```
Ranges in which the basis is unchanged:

                                      Objective Coefficient Ranges
                                  Current        Allowable        Allowable
                Variable      Coefficient         Increase         Decrease
                   X( 1)         10.00000         5.000000         4.000000
                   X( 2)         6.000000         4.000000         2.000000
                   X( 3)         4.000000         2.666667         INFINITY

                                           Righthand Side Ranges
                     Row          Current        Allowable        Allowable
                                      RHS         Increase         Decrease
                       2         100.0000         50.00000         40.00000
                       3         600.0000         400.0000         200.0000
                       4         300.0000         INFINITY         100.0000
```
**有时会提示该模型不能用灵敏度分析**，重启lingo，运行一下，在 `Ctrl + r` 又可以用了。
有灵敏度分析报告可知，
（1） 若要生产产品 C，其利润应该增加 2.666667 以上，即达到 6.666667 元；当其利润为 25/3 元时，只要将原程序中的 $l_3$ 改为 25/3（`lingo`不能是别分数，所以改为 8.33），得到得产品品种规划为：A 29.12；B 45.83；C 25.

（2） 三种资源得影子价格根被为： 3.33；0.67；0.

（3） 增加了一种产品，则 $i = 1,2,3,4$，此时更能突出 `sets` 部分的优势，模型改为
```
sets:
product/1..4/:lr,x;
ziyuan/1..3/:zy;
link(product,ziyuan):c;
endsets

data:
lr = 10,6,4,8;
zy = 100,600,300;
c = 1,10,2,
    1,4,2,
    1,5,6,
   1,4,4;
enddata

max = @sum(product(i):lr(i)*x(i));
@for(ziyuan(j):@sum(link(i,j):c(i,j)*x(i))<=zy(j));
!@for(product(i):@gin(x(i)));

```
运行结果显示，最优产品品种规划为：33.33；16.67；0；50.
（4） 增加一个约束条件： $x_3 \geq 10$,得到的结果为：31.67；58.33；10


