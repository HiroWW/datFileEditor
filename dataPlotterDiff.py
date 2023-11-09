import matplotlib.pyplot as plt

# テーブルからのデータ
data = {
    '1': {'x': '80%', 'y1': 3.114, 'y2': '117.86%'},
    '2': {'x': '70%', 'y1': 3.105, 'y2': '115.90%'},
    '3': {'x': '60%', 'y1': 3.122, 'y2': '113.63%'},
    '4': {'x': '厳密50', 'y1': 3.070, 'y2': '112.27%'},
    '5': {'x': '45%', 'y1': 3.214, 'y2': '109.67%'},
    '6': {'x': '40%', 'y1': 3.265, 'y2': '108.21%'},
    '7': {'x': '25%', 'y1': 3.487, 'y2': '103.36%'},
    '8': {'x': '18%', 'y1': 3.62, 'y2': '100.89%'},
    '9': {'x': '10%', 'y1': 3.813, 'y2': '97.92%'},
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
    y1_diff_values.append(abs((value['y1'] / 3.555) * 100 - 100))
    
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
