import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 读取 Excel 文件
def read_excel_file(filepath):
    df = pd.read_excel(filepath)
    return df

# 进行回归分析
def perform_regression_analysis(df, save_directory):
    # 将分类变量转换为数值变量
    df['Existence of Customer Strategic Alliance'] = df['是否存在客户战略联盟'].apply(lambda x: 1 if x == '是' else 0)

    # 使用 seaborn 绘制回归分析图表
    sns.regplot(x="Existence of Customer Strategic Alliance", y="存在联盟个数", data=df)
    plt.title("Regression Analysis")
    plt.xlabel("Existence of Customer Strategic Alliance")
    plt.ylabel("Number of Alliances")

    # 保存图表到指定目录
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    plt.savefig(os.path.join(save_directory, "regression_analysis.png"))
    plt.show()

# 主函数
def main(filepath):
    # 读取 Excel 文件
    df = read_excel_file(filepath)
    
    # 保存图表到指定目录
    save_directory = os.path.dirname(filepath)
    
    # 进行回归分析
    perform_regression_analysis(df, save_directory)

if __name__ == "__main__":
    filepath = "./results/results.xlsx"  # 替换为实际的 Excel 文件路径
    main(filepath)
