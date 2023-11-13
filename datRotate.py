import numpy as np
import matplotlib.pyplot as plt
import os
import math

def load_dat_files(directory):
    """ Load all .dat files from the specified directory. """
    data_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".dat"):
            data_path = os.path.join(directory, filename)
            data = np.loadtxt(data_path)
            data_files.append((filename, data))
    return data_files

def rotate_data(data, angle_degrees):
    """ Rotate 2D data around the origin by the specified angle. """
    angle_radians = math.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                [np.sin(angle_radians),  np.cos(angle_radians)]])
    rotated_data = np.dot(data, rotation_matrix)
    return rotated_data

def plot_data(data, title="Rotated Data"):
    """ Plot 2D data. """
    plt.figure()
    plt.scatter(data[:, 0], data[:, 1])
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def save_rotated_data(rotated_data, original_filename, directory):
    """ Save rotated data to a new .dat file. """
    new_filename = f"rotated_{original_filename}"
    new_path = os.path.join(directory, new_filename)
    np.savetxt(new_path, rotated_data)
    return new_path

# Example usage
directory = "/home/hiroaki/b4/datFileEditor/origindat"  # Replace with the actual directory path
angle_degrees = 5 # Replace with the desired rotation angle

# Process each .dat file
for filename, data in load_dat_files(directory):
    rotated_data = rotate_data(data, angle_degrees)
    plot_data(rotated_data, title=f"Rotated Data - {filename}")
    save_rotated_data(rotated_data, filename, directory)
