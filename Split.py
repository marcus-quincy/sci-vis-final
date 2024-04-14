import os
import csv

def split_csv_files_by_ids(input_dir, output_dir, ids_to_keep):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in sorted(os.listdir(input_dir)):
        if file_name.endswith('.csv'):
            with open(os.path.join(input_dir, file_name), 'r', newline='') as input_file:
                reader = csv.DictReader(input_file)
                rows_to_keep = []
                rows_to_exclude = []
                for row in reader:
                    if row['id'] in ids_to_keep:
                        rows_to_keep.append(row)
                    else:
                        rows_to_exclude.append(row)
            
            # Write CSV files for rows containing specified IDs
            if rows_to_keep:
                output_file = os.path.join(output_dir, f'ids_{file_name}')
                with open(output_file, 'w', newline='') as output_file:
                    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows_to_keep)
            
            # Write CSV files for rows not containing specified IDs
            if rows_to_exclude:
                output_file = os.path.join(output_dir, f'no_ids_{file_name}')
                with open(output_file, 'w', newline='') as output_file:
                    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows_to_exclude)

if __name__ == "__main__":
    input_dir = "<path>"  # Change this to the input directory containing CSV files
    output_dir = "<path>"  # Change this to the output directory to save modified CSV files
    ids_to_keep = ["22770",
"6621",
"29582",
"50170",
"34497",
"59117",
"4591",
"10466",
"19600",
"35526",
"26771",
"16750",
"46586",
"26765",
"54442",
"5856",
"38199",
"3150",
"47597",
"63358",
"59636",
"8011",
"49827",
"57839",
"46544",
"53000",
"57698",
"1797",
"23650",
"50534",]  # Specify the list of IDs to keep
    
    split_csv_files_by_ids(input_dir, output_dir, ids_to_keep)