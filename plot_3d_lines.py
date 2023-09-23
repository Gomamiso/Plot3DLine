
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# データポイントの作成
t = np.linspace(0, 20, 600)  # 600ポイントで20秒分
x = np.sin(t)
y = np.cos(t)
z = t

# 3Dプロットの準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

line, = ax.plot([], [], [], lw=2)

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def animate(i):
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    return line,

ani = FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True, interval=1000/30)  # 30 FPS

# ラベル等の設定
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 20])
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Line Animation Example')

plt.show()
