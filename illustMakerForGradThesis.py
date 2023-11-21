import matplotlib.pyplot as plt
import numpy as np
import math

# 再び仮の翼形状を作成
# wing_shape = np.array([[0, 0], [1, 0], [0.5, 0.2], [0, 0]])  # 仮の翼形状
wing_shape = np.loadtxt('naca0012_sharpTE.dat')

# 半径のリスト
radii = [1, 2, 3]  # この半径のリストを使用者が提供する

# 色のリスト（半径ごとに異なる色を割り当てる）
colors = ['blue', 'red', 'green']

# 全ての座標に翼を配置する関数
def plot_wing_at_coordinates(coordinates, color):
    for x, y in coordinates:
        plt.plot(x + wing_shape[:, 0], y + wing_shape[:, 1], color=color)

# 円周上の8点を計算する関数
def calculate_circle_points(radius):
    return [(math.cos(2 * math.pi / 8 * i) * radius, math.sin(2 * math.pi / 8 * i) * radius) for i in range(8)]

# 各半径について処理を行う
for radius, color in zip(radii, colors):
    # 円周上の点を計算
    circle_points = calculate_circle_points(radius)
    
    # 翼を配置（色を半径ごとに変更）
    plot_wing_at_coordinates(circle_points, color)
    
    # 円を描画（色を半径ごとに変更）
    circle = plt.Circle((0.5, 0), radius, color=color, fill=False)
    plt.gca().add_artist(circle)

# 原点にも翼を配置（原点の翼の色は最初の色を使用）
origin_color = 'black'
plot_wing_at_coordinates([(0, 0)], origin_color)

# 角度5度の矢印を描画（左下から伸びる）
arrow_angle = math.radians(5)  # 角度をラジアンに変換
arrow_length = 3  # 矢印の長さ
plt.arrow(-6, -6, arrow_length * math.cos(arrow_angle), arrow_length * math.sin(arrow_angle), head_width=0.2, head_length=0.3, fc='purple', ec='purple')

# グラフの設定
plt.axis('equal')
# plt.gca().set_aspect('equal', adjustable='box')

# グラフを保存して表示
plt.savefig('naca_positions_colored.png')
plt.show()
