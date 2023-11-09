import matplotlib.pyplot as plt

# Data from the table
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

# Convert data to lists and calculate the new y values
x_values = []
y1_values = []
y2_values = []

for key, value in data.items():
    # Convert the x-axis values from percentage strings to float
    x_value = float(value['x'].replace('厳密50', '50').strip('%'))
    x_values.append(x_value)
    
    # Calculate the new y1 values (3.555 divided by 100)
    y1_values.append((value['y1'] / 3.555) * 100)
    
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
