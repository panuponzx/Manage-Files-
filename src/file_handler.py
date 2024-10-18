import zipfile
import os
import csv

class FileHandler:
    def __init__(self, zip_file_path):
        self.zip_file_path = zip_file_path
        self.sub_zip_files = []

    def read_main_zip(self):
     
        with zipfile.ZipFile(self.zip_file_path, 'r') as main_zip:
            self.sub_zip_files = [name for name in main_zip.namelist() if name.endswith('.zip')]
            print("Sub ZIP files found:")
            for sub_zip in self.sub_zip_files:
                print(f"- {sub_zip}")

    def export_to_csv(self, output_file_path):
        with open(output_file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Sub ZIP Files']) 
            for sub_zip in self.sub_zip_files:
                writer.writerow([sub_zip])  

if __name__ == "__main__":
    zip_file_path = input(r"Enter the path to the main ZIP file: ")

    if not os.path.isfile(zip_file_path) or not zip_file_path.endswith('.zip'):
        print("Invalid file path. Please provide a valid ZIP file.")
    else:
        file_handler = FileHandler(zip_file_path)
        file_handler.read_main_zip()

        print(f"Total sub ZIP files found: {len(file_handler.sub_zip_files)}")
        for sub_zip in file_handler.sub_zip_files:
            print(f"Sub ZIP: {sub_zip}")

        output_file_path = input("Enter the output CSV file name (e.g., output.csv): ")
        file_handler.export_to_csv(output_file_path)
        print(f"Exported to {output_file_path} successfully.")
