import os
import chardet
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# 定义目录路径
directory = r'.\data'

# 存储编码格式及其出现次数的字典
encoding_count = {}

# 存储需要删除的文件路径列表
files_to_delete = []

# 读取文件内容并进行编码检测
def process_file(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read()
    encoding = chardet.detect(rawdata)['encoding']
    return file_path, encoding

# 遍历目录下的所有文件夹和文件
file_paths = []
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".txt"):
            file_paths.append(os.path.join(root, filename))

# 使用线程池批量处理文件
with ThreadPoolExecutor(max_workers=8) as executor: 
    results = list(tqdm(executor.map(process_file, file_paths), total=len(file_paths), desc="处理文件"))
# 将处理结果分析
for file_path, encoding in results:
    # 如果编码格式为GB2312，则将文件路径添加到待删除列表中
    if encoding == 'GB2312':
        files_to_delete.append(file_path)
        print(f"待删除文件（GB2312编码）: {file_path}")
    # 如果编码格式为ISO-8859-1，则将文件路径添加到待删除列表中
    elif encoding == 'ISO-8859-1':
        files_to_delete.append(file_path)
        print(f"待删除文件（ISO-8859-1编码）: {file_path}")
    else:
        # 记录编码格式出现的次数
        if encoding:
            encoding_count[encoding] = encoding_count.get(encoding, 0) + 1
        else:
            encoding_count['unknown'] = encoding_count.get('unknown', 0) + 1

# 删除需要删除的文件
for file_to_delete in tqdm(files_to_delete, desc="删除文件"):
    os.remove(file_to_delete)

# 打印统计结果
print("\n文件编码格式统计结果:")
for encoding, count in encoding_count.items():
    print(f"{encoding}: {count} 个文件")
