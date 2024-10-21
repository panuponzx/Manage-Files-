from logging import FileHandler
import csv
from typing import List, Tuple

class CSVExporter:
    def __init__(self, xml_files: List[Tuple[str, str]]):
        self.xml_files = xml_files

    def export_to_csv(self, output_file_path: str):
        """Export CSV"""
        with open(output_file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Sub ZIP File', 'Files'])  

            for sub_zip, file_name in self.xml_files:
                csv_writer.writerow([sub_zip, file_name]) 

        print(f"Exported CSV to {output_file_path} successfully.")

if __name__ == "__main__":
    path_to_main_zip = input("Enter the path to the main ZIP file: ")
    file_handler = FileHandler(path_to_main_zip)
    file_handler.find_sub_zip_files()
    file_handler.access_sub_zip_files()
    
    output_csv_name = input("Enter the output CSV file name (e.g., output.csv): ")
    csv_exporter = CSVExporter(file_handler.xml_files)
    csv_exporter.export_to_csv(output_csv_name)