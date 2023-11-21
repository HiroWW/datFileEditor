import matplotlib.pyplot as plt
import numpy as np
import math

# 翼の形状データを読み込む
# ここでは実際のファイルを使用できないため、仮の翼形状を作成します。
# 実際の使用時には、適切なファイルからデータを読み込んでください。
wing_shape = np.array([[0, 0], [1, 0], [0.5, 0.2], [0, 0]])  # 仮の翼形状

# 半径のリスト
radii = [1, 2, 3]  # この半径のリストを使用者が提供する

# 全ての座標に翼を配置する関数
def plot_wing_at_coordinates(coordinates):
    for x, y in coordinates:
        plt.plot(x + wing_shape[:, 0], y + wing_shape[:, 1], 'b-')

# 円周上の8点を計算する関数
def calculate_circle_points(radius):
    return [(math.cos(2 * math.pi / 8 * i) * radius, math.sin(2 * math.pi / 8 * i) * radius) for i in range(8)]

# 各半径について処理を行う
for radius in radii:
    # 円周上の点を計算
    circle_points = calculate_circle_points(radius)
    
    # 翼を配置
    plot_wing_at_coordinates(circle_points)
    
    # 円を描画
    circle = plt.Circle((0, 0), radius, color='g', fill=False)
    plt.gca().add_artist(circle)

# 原点にも翼を配置
plot_wing_at_coordinates([(0, 0)])

# グラフの設定
plt.axis('equal')
plt.gca().set_aspect('equal', adjustable='box')

# グラフを保存して表示
plt.savefig('naca_positions.png')
plt.show()
