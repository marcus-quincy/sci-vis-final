import numpy as np
import glob
import os

def read_csv_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    data = []  # Initialize an empty list to store data
    
    for file_name in sorted(glob.glob(os.path.join(input_dir, '*.csv'))):
        current_data = np.genfromtxt(file_name, delimiter=',', dtype=str)
        previous_ids = set()
        if len(data) > 0:
            previous_ids = set(data[-1][:, -1])
        
        current_ids = set(current_data[:, -1]) if len(current_data) > 0 else set()
        missing_ids = previous_ids - current_ids
        for missing_id in missing_ids:
            missing_row = np.where(data[-1][:, -1] == missing_id)[0]
            if len(missing_row) > 0:
                current_data = np.vstack([current_data, data[-1][missing_row]])
        
        # Save the modified data back into the file
        output_file = os.path.join(output_dir, os.path.basename(file_name))
        np.savetxt(output_file, current_data, delimiter=',', fmt='%s')
        
        data.append(current_data)  # Append the current data to the list

if __name__ == "__main__":
    input_dir = "<path>"  # Change this to the input directory containing CSV files
    output_dir = "<path>"  # Change this to the output directory to save modified CSV files
    read_csv_files(input_dir, output_dir)
