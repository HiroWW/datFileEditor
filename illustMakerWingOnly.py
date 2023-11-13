import matplotlib.pyplot as plt
import numpy as np
import math

# 翼の形状データを読み込む
wing_shape = np.loadtxt('wing_shape.dat')

# 座標リストを設定する
coordinates  = [(0, 0),  (0, 1),   (1, 0),  (-1, 0),  (0, -1),  (1/math.sqrt(2), 1/math.sqrt(2)),  (-1/math.sqrt(2), 1/math.sqrt(2)),  (1/math.sqrt(2), -1/math.sqrt(2)),  (-1/math.sqrt(2), -1/math.sqrt(2))]   # ここに翼の形を配置する座標を入れます
# large_points = [(2, 3), (4, 5)]  # ここに大きめの点を配置する座標を入れます

# 各座標に翼の形状を配置する
for x, y in coordinates:
    plt.plot(x + wing_shape[:, 0], y + wing_shape[:, 1], 'b-')  # 翼の形状をプロット

# 大きめの点をプロットする
# for x, y in large_points:
#     plt.scatter(x, y, color='red', s=100)  # 色とサイズは調整可能

# グラフの設定
plt.axis('equal')  # 同じスケールで表示

# グラフを表示する
plt.show()
plt.savefig('naca_positions.png')
