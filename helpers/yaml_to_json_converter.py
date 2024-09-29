import os
import yaml
import json
from typing import List

def convert_yaml_to_json(input_folder: str = "../models", output_folder: str = "../models-json") -> List[str]:
    """
    Convert YAML files in the input folder to JSON files in the output folder.

    Args:
        input_folder (str): Path to the folder containing YAML files. Defaults to "models".
        output_folder (str): Path to the folder where JSON files will be saved. Defaults to "models-json".

    Returns:
        List[str]: A list of successfully converted file names.

    Raises:
        FileNotFoundError: If the input folder does not exist.
        PermissionError: If there are permission issues with reading input files or writing output files.
        yaml.YAMLError: If there's an error parsing the YAML file.
        json.JSONDecodeError: If there's an error converting YAML to JSON.
    """
    converted_files = []

    # Check if input folder exists
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' does not exist.")

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.yaml', '.yml')):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.json'
            output_path = os.path.join(output_folder, output_filename)

            try:
                # Read YAML file
                with open(input_path, 'r') as yaml_file:
                    yaml_content = yaml.safe_load(yaml_file)

                # Convert YAML to JSON and write to output file
                with open(output_path, 'w') as json_file:
                    json.dump(yaml_content, json_file, indent=2)

                converted_files.append(filename)
                print(f"Converted {filename} to {output_filename}")

            except yaml.YAMLError as yaml_error:
                print(f"Error parsing YAML file {filename}: {yaml_error}")
            except json.JSONDecodeError as json_error:
                print(f"Error converting YAML to JSON for file {filename}: {json_error}")
            except PermissionError as perm_error:
                print(f"Permission error while processing file {filename}: {perm_error}")
            except Exception as e:
                print(f"Unexpected error while processing file {filename}: {e}")

    return converted_files

# Example usage
try:
    converted = convert_yaml_to_json()
    print(f"Successfully converted {len(converted)} files.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
