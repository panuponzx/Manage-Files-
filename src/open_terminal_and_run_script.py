import os
import sys

def check_if_running_in_vscode_terminal():
   
    return 'VSCODE_PID' in os.environ

def open_terminal_and_run_script(zip_file_path):
    if os.name == 'nt':  # Windows
        command = f'start cmd /k "cd /d {os.path.dirname(sys.argv[0])} && python {sys.argv[0]} {zip_file_path}"'
        os.system(command)
    elif sys.platform == 'darwin':  # macOS
        command = f'open -a Terminal "cd {os.path.dirname(sys.argv[0])} && python3 {sys.argv[0]} {zip_file_path}"'
        os.system(command)
    elif sys.platform.startswith('linux'):  # Linux
        command = f'gnome-terminal -- bash -c "cd {os.path.dirname(sys.argv[0])} && python3 {sys.argv[0]} {zip_file_path}; exec bash"'
        os.system(command)
    else:
        print("Unsupported OS")
        sys.exit(1)
