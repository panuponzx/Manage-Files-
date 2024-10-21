import os
from file_handler import FileHandler
from csv_exporter import CSVExporter 
from open_terminal_and_run_script import open_terminal_and_run_script

def main():
    zip_file_path = input(r"Enter the path to the main ZIP file: ")

    if not os.path.isfile(zip_file_path) or not zip_file_path.endswith('.zip'):
        print("Invalid file path. Please provide a valid ZIP file.")
        return

    file_handler = FileHandler(zip_file_path)
    file_handler.find_sub_zip_files() 
    file_handler.access_sub_zip_files()  

    print(f"Total sub ZIP files found: {len(file_handler.sub_zip_files)}")
    for sub_zip in file_handler.sub_zip_files:  
        print(f"Sub ZIP: {sub_zip}")
        
    output_file_path = input("Enter the output CSV file name (e.g., output.csv): ")
    csv_exporter = CSVExporter(file_handler.xml_files) 
    csv_exporter.export_to_csv(output_file_path) 

    print(f"Exported to {output_file_path} successfully.")

    open_terminal_and_run_script(zip_file_path)

if __name__ == "__main__":
    main()
