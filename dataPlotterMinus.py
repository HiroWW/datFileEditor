import matplotlib.pyplot as plt

# Data from the table
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


# Convert data to lists and calculate the new y values
x_values = []
y1_values = []
y2_values = []

for key, value in data.items():
    # Convert the x-axis values from percentage strings to float
    x_value = float(value['x'].replace('厳密50', '50').strip('%'))
    x_values.append(x_value)
    
    # Calculate the new y1 values (3.555 divided by 100)
    y1_values.append((value['y1'] / 5.25) * 100)
    
    # Convert y2 values from percentage strings to float
    y2_value = float(value['y2'].strip('%'))
    y2_values.append(y2_value)

# Plotting the data
plt.figure(figsize=(10, 5))

# First plot
plt.plot(x_values, y1_values, label='ALMwing : AoA', color='blue', marker='o')

# Second plot
plt.plot(x_values, y2_values, label='RANS wing : CL', color='red', marker='x')

# Adding titles and labels
# plt.title('Comparison of Y1 and Y2 Values')
plt.xlabel('chord (%)')
plt.ylabel('value / RANS (%)')
plt.legend()

# 縦軸100%の位置に薄い直線を引く
plt.axhline(100, color='gray', linewidth=0.5)

# Show the plot
plt.show()
