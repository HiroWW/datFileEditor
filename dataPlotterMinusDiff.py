import matplotlib.pyplot as plt

# テーブルからのデータ
# 新しいテーブルからのデータ
data = {
    '1': {'x': '10%', 'y1': 6.056, 'y2': '83.20%'},
    '2': {'x': '20%', 'y1': 5.982, 'y2': '83.19%'},
    '3': {'x': '25%', 'y1': 5.931, 'y2': '83.39%'},
    '4': {'x': '30%', 'y1': 5.869, 'y2': '83.74%'},
    '5': {'x': '40%', 'y1': 5.713, 'y2': '84.97%'},
    '6': {'x': '50%', 'y1': 5.51,  'y2': '86.96%'},
    '7': {'x': '60%', 'y1': 5.26,  'y2': '89.71%'},
    '8': {'x': '70%', 'y1': 4.983, 'y2': '93.15%'},
    '9': {'x': '80%', 'y1': 4.68,  'y2': '97.12%'},
    '10': {'x': '90%', 'y1': 4.373, 'y2': '101.74%'}
}


# リストにデータを変換し、新しいy値を計算
x_values = []
y1_diff_values = []
y2_diff_values = []

for key, value in data.items():
    # x軸の値をパーセント文字列から浮動小数点数に変換
    x_value = float(value['x'].replace('厳密50', '50').rstrip('%'))
    x_values.append(x_value)
    
    # 新しいy1の値を計算（3.555で割って100倍した後、100との差の絶対値を取る）
    y1_diff_values.append(abs((value['y1'] / 5.25) * 100 - 100))
    
    # y2の値をパーセント文字列から浮動小数点数に変換し、100との差の絶対値を取る
    y2_diff_value = abs(float(value['y2'].rstrip('%')) - 100)
    y2_diff_values.append(y2_diff_value)

# データのプロット
plt.figure(figsize=(10, 5))

# 最初のプロット（Y1の差）
plt.plot(x_values, y1_diff_values, label='ALMwing : AoA', color='blue', marker='o')

# 二番目のプロット（Y2の差）
plt.plot(x_values, y2_diff_values, label='RANS wing : CL', color='red', marker='x')

# タイトルとラベルの追加
plt.xlabel('chord (%)')
plt.ylabel('Error (%)')
plt.legend()

# 縦軸100%の位置に薄い直線を引く
plt.axhline(0, color='gray', linewidth=0.5)

# プロットの表示
plt.show()
