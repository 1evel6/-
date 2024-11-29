import matplotlib.pyplot as plt



#下面使用 Matplotlib 绘制一张简单的折线图，再对其进行定制，以实现信息更丰富的数据
#可视化效果。我们将使用平方数序列 1、4、9、16 和 25 来绘制这个图形。
#要创建简单的折线图，只需指定要使用的数，Matplotlib 将完成余下的工作：
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)






# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


plt.show()



