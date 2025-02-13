import os
import zipfile
import csv

class FileHandler:
    def __init__(self, zip_file_path):
        self.zip_file_path = zip_file_path
        self.sub_zip_files = []
        self.xml_files = []

    def find_sub_zip_files(self):
        with zipfile.ZipFile(self.zip_file_path, 'r') as main_zip:
            for item in main_zip.namelist():
                if item.endswith('.zip'):
                    self.sub_zip_files.append(item)
                    print(f"Found ZIP file: {item}")

    def access_sub_zip_files(self, sub_zip_path):
        """ Access files in the given sub ZIP file. """
        if not os.path.exists(sub_zip_path):
            print(f"File not found: {sub_zip_path}")
            return  

        print(f"Accessing {sub_zip_path}...")
        
        with zipfile.ZipFile(sub_zip_path, 'r') as nested_zip:
            print(f"Files in {sub_zip_path}:")
            for file in nested_zip.namelist():
                print(f" - {file}")
                self.xml_files.append((sub_zip_path, file))  
