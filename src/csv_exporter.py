import os
import csv
from typing import List, Tuple

class CSVExporter:
    def __init__(self, xml_files: List[Tuple[str, str]]):
        self.xml_files = xml_files

    def get_downloads_folder(self):
        """ Return the path to the Downloads folder based on the OS. """
        if os.name == 'nt':  # Windows
            return os.path.join(os.path.expanduser("~"), "Downloads")
        elif os.sys.platform == 'darwin':  # macOS
            return os.path.join(os.path.expanduser("~"), "Downloads")
        else:  # Linux
            return os.path.join(os.path.expanduser("~"), "Downloads")

    def export_to_csv(self, output_file_name: str):
        """Export CSV to Downloads folder."""
        downloads_folder = self.get_downloads_folder()
        
        if not output_file_name.endswith('.csv'):
            output_file_name += '.csv'
        
        output_file_path = os.path.join(downloads_folder, output_file_name)

        with open(output_file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Sub ZIP File', 'Files'])

            for sub_zip, file_name in self.xml_files:
                sub_zip_name = os.path.basename(sub_zip) 
                sub_zip_name_modified = f"{os.path.splitext(sub_zip_name)[0]}_1.zip"  
                csv_writer.writerow([sub_zip_name_modified, file_name])

        print(f"Exported CSV to {output_file_path} successfully.")
