import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf')  # 你可以根据实际情况调整字体路径

# 读取 Excel 文件
df = pd.read_excel('D:\\AAAPycharmProjects\\ACG\\acg_output.xlsx')

# 提取关注人数并转换为数组
members = df['关注人数'].to_numpy()

# 定义量级区间
bins = [10**i for i in range(int(np.log10(members.min())), int(np.log10(members.max())) + 2)]

# 计算每个量级内的个数
hist, bin_edges = np.histogram(members, bins=bins)

# 绘制柱形图
plt.figure(figsize=(10, 6))
plt.bar(range(len(hist)), hist, width=0.6, tick_label=[f'{int(bin_edges[i]):.0e} - {int(bin_edges[i+1]):.0e}' for i in range(len(bin_edges)-1)])

# 添加标题和标签
plt.title('关注人数量级分布图', fontproperties=font)
plt.xlabel('关注人数量级区间', fontproperties=font)
plt.ylabel('数量', fontproperties=font)

# 显示图表
plt.show()
