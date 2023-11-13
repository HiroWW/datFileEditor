import matplotlib.pyplot as plt
import numpy as np

# 翼の形状データを読み込む
wing_shape = np.loadtxt('wing_shape.dat')

# 座標リストを設定する
coordinates  = [(0, 0),  (0, 1),   (1, 0),  (-1, 0), (0, -1)]  # ここに翼の形を配置する座標を入れます
large_points = [(0, 0), (0.5, 1), (0.68, 1), (0.1, 1),(0,0)]  # ここに大きめの点を配置する座標を入れます
# matplotlibのデフォルトの色サイクルを取得する
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# 座標ごとに翼と点をプロットする
for i, ((x_wing, y_wing), (x_point, y_point)) in enumerate(zip(coordinates, large_points)):
    color = colors[i % len(colors)]  # 色を選択
    # 翼をプロット
    plt.plot(x_wing + wing_shape[:, 0], y_wing + wing_shape[:, 1], color=color)
    # 点をプロット
    # if(i == 0):
        # plt.scatter(x_point, y_point, color=color, s=1)
    # else :    
        # plt.scatter(x_point, y_point, color=color, s=100)

# グラフの設定
plt.axis('equal')  # 同じスケールで表示

# グラフを表示する
plt.show()

# グラフを保存する
plt.savefig('naca_positions.png')
