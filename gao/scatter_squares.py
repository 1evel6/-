import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')


fig, ax = plt.subplots()


ax.scatter(x_values, y_values, s=10)


ax.scatter(2, 4, s=10)
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Square of Value", fontsize=10)




# 设置刻度标记的样式
ax.tick_params(labelsize=10)


ax.axis([0, 1100, 0,1_100_000])

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.scatter(2, 4)
plt.show()


#如果要将绘图保存到文件中，而不是在 Matplotlib 查看器中显示它，可将 plt.show() 替
#换为 plt.savefig()：
#plt.savefig('squares_plot.png', bbox_inches='tight')