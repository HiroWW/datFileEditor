import matplotlib.pyplot as plt
import numpy as np
import math

# 再び仮の翼形状を作成
# wing_shape = np.array([[0, 0], [1, 0], [0.5, 0.2], [0, 0]])  # 仮の翼形状
wing_shape = np.loadtxt('naca0012_sharpTE.dat')


# 半径のリスト
# radii = [1, 1.5, 2, 3, 5]  # この半径のリストを使用者が提供する
radii = [1, 1.5, 2]  # この半径のリストを使用者が提供する

# 色のリスト（半径ごとに異なる色を割り当てる）
# colors = ['blue', 'red', 'green', 'magenta', 'cyan']
plt.style.use('ggplot')
colors = plt.cm.tab10.colors[:5] 

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

    # plt.text(0.5+(radius)*math.cos(30/180*math.pi), radius*math.sin(30/180*math.pi), f'r={radius}', horizontalalignment='center', fontsize=12, verticalalignment='center')

# 原点にも翼を配置（原点の翼の色は最初の色を使用）
origin_color = 'black'
plot_wing_at_coordinates([(0, 0)], origin_color)

# 角度5度の矢印を描画（左下から伸びる）
arrow_angle = math.radians(5)  # 角度をラジアンに変換
arrow_length = 1  # 矢印の長さ
plt.arrow(-2.7, -1, arrow_length * math.cos(arrow_angle), arrow_length * math.sin(arrow_angle), head_width=0.2, head_length=0.3, fc='purple', ec='purple')

# 矢印に対するラベルを追加（TeX表記）
plt.text(-2.7, -0.5,   r'$U_\infty$', fontsize=18, color='purple')

# プロット範囲の設定
# plt.xlim(-7, )  # x軸の範囲
# plt.ylim(-5, 5)  # y軸の範囲

# ここで角度目盛りを追加する（例：0度、45度、90度）
def plot_angle_mark(radius, angle_deg, label):
    angle_rad = math.radians(angle_deg)
    end_x = radius * math.cos(angle_rad)
    end_y = radius * math.sin(angle_rad)
    plt.arrow(0.5, 0, end_x, end_y, head_width=0.1, head_length=0.15, fc='black', ec='black')
    if (angle_deg == 0):
        plt.text(end_x * 1.3, end_y * 1.1, label, fontsize=10, ha='center', va='center')
    else : 
        plt.text(end_x * 1.1, end_y * 1.1, label, fontsize=10, ha='center', va='center')
# 角度の目盛りを45度ごとに表示
for angle in range(0, 360, 45):
    plot_angle_mark(2.5, angle, f'{angle}°')

# グラフの設定
plt.axis('equal')
plt.gca().set_aspect('equal', adjustable='box')
# plt.figure(figsize=(10, 10))  # この数字を調整してグラフのサイズを変更

# グラフを保存して表示
# plt.xlim(-7.5, 7.5)
# plt.ylim(-7.5, 7.5)
plt.ylim(-3.25, 3.25)
plt.xlim(-3, 3.5)
plt.savefig('naca_positions_colored.png')
plt.show()
