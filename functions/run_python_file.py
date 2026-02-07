import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        #print("DEBUG", working_dir_abs, target_path)
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]
        if args != None:
            command.extend(args)
        stuff = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        return_string = ""
        if stuff.returncode != 0:
            return_string += f"Process exited with code {stuff.returncode}"
        if not stuff.stdout.strip() and not stuff.stderr.strip():
            return_string += "No output produced"
        if stuff.stdout != "":
            return_string += f"STDOUT: {stuff.stdout}"
        if stuff.stderr != "":
            return_string += f"STDERR: {stuff.stderr}"
        
        return return_string
        

    except Exception as e:
        return f"Error: executing Python file: {e}" 