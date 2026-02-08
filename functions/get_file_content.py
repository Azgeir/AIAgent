import os
from config import MAX_CHARS
from google import genai
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_path) as file:
            content = file.read(MAX_CHARS)
            if file.read(1) != "":
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content


    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the first up to 10000 characters in a given file, and returns it as a string. Additionally, if the file is longer than 10000 characters, it ends the string stating when it was truncated'",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path to read from, relative to the working directory (default is the working directory itself)",
            ),
        },
        required=["file_path"]
    ),
)
        