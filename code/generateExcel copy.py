import os
import re
import shutil
import openpyxl

# 读取TXT文档内容
def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# 判断是否包含关键词
def contains_keywords(sentence):
    keywords = ['客户', '战略联盟', '战略同盟', '战略合作', '战略伙伴']
    # 判断句子是否同时包含“客户”和至少一个战略关键词
    if '客户' in sentence and any(keyword in sentence for keyword in keywords[1:]):
        return True
    return False

# 统计包含关键词的句子数量
def count_matched_sentences(sentences):
    count = 0
    for sentence in sentences:
        if contains_keywords(sentence):
            count += 1
    return count

# 主函数
def main(directory):
    parent_directory = os.path.dirname(directory)  # 获取 '2007' 文件夹的父级目录
    save_directory = os.path.join(parent_directory, "results")  # 保存文件的目录，保存到名为 "results" 的文件夹中
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # 创建 Excel 文件
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["股票代码", "年份", "是否存在客户战略联盟", "存在联盟个数"])

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            stock_code, year = filename.split("_")
            year = year.split(".")[0]  # 去除文件名中的扩展名
            filepath = os.path.join(directory, filename)
            text = read_text_file(filepath)
            sentences = re.split(r'([。？！])', text)  # 使用括号捕获分割符号，保留分割符号
            # 重新构建句子，将分割符号添加回去
            reconstructed_sentences = []
            for i in range(len(sentences)//2):
                reconstructed_sentences.append(sentences[2*i] + sentences[2*i+1])
            if len(sentences) % 2 == 1:
                reconstructed_sentences.append(sentences[-1])  # 如果句子的数量为奇数，添加最后一个句子（不包含分割符号）
            
            num_matched_sentences = count_matched_sentences(reconstructed_sentences)
            # 将匹配结果写入 Excel 表格
            if num_matched_sentences > 0:
                ws.append([stock_code, year, "是", num_matched_sentences])
            else:
                ws.append([stock_code, year, "否", 0])

    # 保存 Excel 文件
    excel_filepath = os.path.join(save_directory, "results.xlsx")
    wb.save(excel_filepath)
    print(f"\n匹配结果已保存至 Excel 文件: {excel_filepath}")

# 调用主函数
if __name__ == "__main__":
    directory = r'.\data\2007'  # 使用相对路径，替换为实际的 '2007' 文件夹路径
    main(directory)
