import matplotlib.pyplot as plt
import sys

# 引数からファイル名を取得
if len(sys.argv) != 2:
    print("Usage: python script.py <dat_file>")
    sys.exit(1)

dat_file = sys.argv[1]

# データを読み込む
x_values = []
y_values = []
with open(dat_file, 'r') as file:
    for line in file:
        # 行の先頭が数字でない場合はスキップ
        if not line.strip()[0].isdigit():
            continue
        # スペースまたはタブで分割して数値部分を抜き出す
        values = line.split()
        x = float(values[0])
        y = float(values[1])
        x_values.append(x)
        y_values.append(y)

# データを二次元座標にプロット
plt.scatter(x_values, y_values, s=1)  # sはプロットのマーカーサイズ
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Scatter Plot')
plt.show()
