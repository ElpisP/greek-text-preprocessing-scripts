import Levenshtein
import os

def calculate_cer(reference, hypothesis):
    return Levenshtein.distance(reference, hypothesis) / len(reference)

def save_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def replace_text_lines(input_file, contamination_file, target_cer, output_folder):
    with open(input_file, 'r') as f:
        original_text = f.read()

    with open(contamination_file, 'r') as f:
        contamination_text = f.read()

    # Calculate initial_cer for the contamination file
    initial_cer = calculate_cer(original_text, contamination_text)
    print(f"Initial CER for contamination file: {initial_cer}")

    updated_cer = initial_cer

    if initial_cer <= target_cer:
        message = f"No character replacements are needed for CER {target_cer}. Initial CER is already within or below the target.\nInitial CER: {initial_cer}"
        input_file_name = os.path.splitext(os.path.basename(input_file))[0]  # Define input_file_name
        output_file = os.path.join(output_folder, f"{input_file_name}_CER{target_cer}.txt")
        save_to_file(output_file, message)
    else:
        updated_text = original_text

        for i in range(len(original_text)):
            # Check if the index is within the valid range of the string
            if i < len(contamination_text):
                updated_text = updated_text[:i] + contamination_text[i] + updated_text[i+1:]
                updated_cer = calculate_cer(updated_text, contamination_text)

                if updated_cer <= target_cer:
                    break
            else:
                # Reuse the contamination_text by looping back to the beginning
                contamination_text = contamination_text + contamination_text[i % len(contamination_text)]

        input_file_name = os.path.splitext(os.path.basename(input_file))[0]  # Define input_file_name
        output_file = os.path.join(output_folder, f"{input_file_name}_CER{target_cer}.txt")

        with open(output_file, 'w') as f:
            f.write(updated_text)

        # Print updated_cer after each output file is created
        print(f"Updated CER for the output file (CER {target_cer}): {updated_cer}")

# Specify the file paths for input and contamination
input_file = 'D-5-GT.txt'
contamination_file = 'D-5-HTR.txt'

# Specify the target CER thresholds as a list
target_cers = [0.2, 0.15, 0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]

# Specify the output folder
output_folder = 'CER_contaminations'

# Replace lines based on the CER thresholds and save corresponding output files
for target_cer in target_cers:
    replace_text_lines(input_file, contamination_file, target_cer, output_folder)

# Final completion message
print("Character replacement process completed for all target CER thresholds.")
