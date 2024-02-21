# 基于文本分析的客户战联盟指标的构建
## 一、基本思路
由论文《客户战略联盟如何激发企业创新？——基于文本分析的经验证据》得到，具体文本匹配过程如下图所示：
![alt text](image\image.png)

## 二、环境配置
```
# pip install chardet
pip install chardet -i https://pypi.tuna.tsinghua.edu.cn/simple

# pip install openpyxl
pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple

# pip install tqdm
pip install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple

# pip install seaborn
pip install seaborn -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 三、数据分析
### 1、数据清理

数据获取，百度云:

```
链接：https://pan.baidu.com/s/1vep7hse14jxZOitFvcUTtw?pwd=9m2n 
提取码：9m2n
```

在给出的企业年度报告文件中，存在有乱码文件，这些乱码文件恢复不了，不能用于数据分析，因此需要将其清除掉。具体实现过程如下：
1. 运行`checkEncode.py`，找到异常编码格式文件； 
![alt text](image\Cache_-2271835918771a73..jpg)
![alt text](image\encode.png)
其中以`ISO-8859-1`编码格式进行编码的为乱码文件，然后进行自动删除。
### 2、文本分析
通过前面的文本匹配规则进行匹配关键字，得到一份含有`企业股票代码、年份、是否存在客户战略联盟、存在联盟个数`的excel表格文件，其中存在联盟个数是指出现客户与联盟等词的句子数。
![alt text](image\excelmoban.png)

1. 运行`generateExcel.py`即可，会将生成的excel文件保存在`results`目录下；

### 3、数据分析
1. 运行`dataAnalysis.py`，进行数据分析； 
通过分析excel中的数据，我们发现。。。。。

