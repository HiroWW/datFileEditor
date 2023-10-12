import matplotlib.pyplot as plt
import sys
import os

# 引数からファイル名と縮小倍率を取得
if len(sys.argv) != 3:
    print("Usage: python script.py <dat_file> <scaling_factor>")
    sys.exit(1)

dat_file = sys.argv[1]
scaling_factor = float(sys.argv[2])

# 出力ファイル名の生成
base_filename, file_extension = os.path.splitext(dat_file)
output_filename = f"{base_filename}_{1/scaling_factor:.2f}x{file_extension}"

# データを読み込んで縮小
x_values = []
y_values = []
with open(dat_file, 'r') as file:
    for line in file:
        if not line.strip()[0].isdigit():
            continue
        values = line.split()
        x = float(values[0]) / scaling_factor
        y = float(values[1]) / scaling_factor
        x_values.append(x)
        y_values.append(y)

# 縮小したデータを保存
with open(output_filename, 'w') as output_file:
    for x, y in zip(x_values, y_values):
        output_file.write(f"{x} {y}\n")

# プロット
plt.scatter(x_values, y_values, s=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'2D Scatter Plot (1/{scaling_factor:.2f} scaling)')
plt.show()
