import os
import csv
import numpy as np

def calculate_centroid(data):
    """
    Calculate the centroid of the data.
    """
    # Extract x, y, and z coordinates
    x_values = [float(row['x']) for row in data]
    y_values = [float(row['y']) for row in data]
    z_values = [float(row['z']) for row in data]
    
    # Calculate centroid
    centroid_x = np.mean(x_values)
    centroid_y = np.mean(y_values)
    centroid_z = np.mean(z_values)
    
    return centroid_x, centroid_y, centroid_z

def save_centroid_to_csv(centroid, output_file):
    """
    Save the centroid to a CSV file with x, y, z coordinates.
    """
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y', 'z'])
        writer.writerow(centroid)

def process_csv_files(input_dir, output_dir):
    """
    Process CSV files in the input directory and save centroids as separate CSV files in the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in sorted(os.listdir(input_dir)):
        if file_name.endswith('.csv'):
            # Read CSV file
            with open(os.path.join(input_dir, file_name), 'r', newline='') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
            
            # Calculate centroid
            centroid = calculate_centroid(data)
            
            # Save centroid to CSV
            output_file = os.path.join(output_dir, f'centroid_{file_name}')
            save_centroid_to_csv(centroid, output_file)

if __name__ == "__main__":
    input_dir = "<path>"  # Change this to the input directory containing CSV files
    output_dir = "<path>"  # Specify the output directory to save centroid CSV files
    
    process_csv_files(input_dir, output_dir)
