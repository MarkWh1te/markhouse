---
title: Spark 总结(一) 基础
date: 2017-03-30 10:36:00
tags:
  - Spark
  - Scala
categories: bigdata
---

### RDDs

#### 在Spark中RDDs是最基本的容器 , 它支持和scala collection 类似的API,比如map，fold，和filter.可以将它理解为这样的一个抽象类

``` scala
val points = sc.textFile(...).map(parsePoint).persist()
var w = Vector.zeros(d)
for (i<-1 to numIterations){
  val gradient = points.map{
        p=> (1/(1+exp(-p.y*w.dot(p.x)))-1)*p.y*p.y 
  }.reduce(_+_)
  w -= alpha*gradient
}
```

#### 创建一个RDD有两种办法：
* 从HFDS或者本地文件系统中读取一个txtfile
* 在已有的RDD上做Transformations
      
      
      
### Transformations and Actions

1. Transformations
    Transformations 是惰性的，它返回的是另一个RDD,比如filter，map，groupBy
2. Actions 
    Actions 会立刻执行，会返回一个数值作为运算结果，比如，reduce，count
3. 某些Transformations可以对两个RDD 进行集合运算:
    * union
    * intersection
    * subtract
    * cartesian
4. 除此之外，还有一些的较为常用的actions
    * takeSample
    * takeOrdered
    * saveAsTextFile
    * saveAsSequenceFile
        
        
### Spark的运算效率

1.  spark 通过使用 immutable数据结构使其在做并行计算的过程中所有的计算都是in-memory的,不需要进行磁盘IO
2.  通过使用persist()和cache（）等方法可以提高spark的效率,以逻辑回归算法为例, 在读取数据的使用persist ()，之后整个程序的运行效率会提高很多
    
``` scala
val points = sc.textFile(...).map(parsePoint).persist()
var w = Vector.zeros(d)
for (i<-1 to numIterations){
  val gradient = points.map{
        p=> (1/(1+exp(-p.y*w.dot(p.x)))-1)*p.y*p.y 
  }.reduce(_+_)
  w -= alpha*gradient
}
```


### Spark程序执行过程:
1. Driver Program(Spark Context)
2. Cluster Manager(yearn,mesos)
3. work node(executer)
如果说对RDD 执行了一个foreach println的操作，其实你是看不到任何东西的， 因为foreach在work node 执行的，所以println这个函数的副作用是显示在work node上的。

这也提醒了我们在spark的代码的时候要做在action之前都是referential transparency! 
        
        
        
        
        
        
        
