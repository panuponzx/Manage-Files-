import os
from file_handler import FileHandler
from csv_exporter import CSVExporter 
from open_terminal_and_run_script import check_if_running_in_vscode_terminal, open_terminal_and_run_script

def main():
    zip_file_path = input(r"Enter the path to the main ZIP file (or 'c' to cancel): ")

    if zip_file_path.lower() == 'c':
        print("Exiting the program.")
        return  

    if check_if_running_in_vscode_terminal():
        print("Running in VS Code terminal, opening external terminal...")
        open_terminal_and_run_script(zip_file_path)
        return

    if not os.path.isfile(zip_file_path) or not zip_file_path.endswith('.zip'):
        print("Invalid file path. Please provide a valid ZIP file.")
        return

    file_handler = FileHandler(zip_file_path)
    file_handler.find_sub_zip_files() 

    print(f"Total sub ZIP files found: {len(file_handler.sub_zip_files)}")
    for sub_zip in file_handler.sub_zip_files:  
        print(f"Sub ZIP: {sub_zip}")

    while True:
        sub_zip_path = input("Enter the path to the sub ZIP file (or 'c' to cancel): ")
        
        if sub_zip_path.lower() == 'c':
            print("Exiting the program.")
            break  # Exit the loop if user chooses to cancel

        # Access files in the sub ZIP
        file_handler.access_sub_zip_files(sub_zip_path)  

        # Check if xml_files have been populated before exporting
        if not file_handler.xml_files:
            print("No XML files found in the selected sub ZIP. Please select another one.")
            continue  # Skip to the next iteration of the loop

        output_file_name = input("Enter the output CSV file name (without .csv extension): ")
        output_file_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{output_file_name}.csv")
        
        csv_exporter = CSVExporter(file_handler.xml_files) 
        csv_exporter.export_to_csv(output_file_path) 
        
        print(f"Exported to {output_file_path} successfully.")

if __name__ == "__main__":
    main()
