import os
import sys

def open_terminal_and_run_script(zip_file_path):
    if os.name == 'nt':  # Windows
        command = f'start cmd /k "python {sys.argv[0]} {zip_file_path}"'
        os.system(command)
    else:  # macOS/Linux
        command = f'open -a Terminal "{sys.argv[0]} {zip_file_path}"'
        os.system(command)
