import Levenshtein

# Function to calculate CER for a file
def calculate_cer_for_file(reference_file, hypothesis_file):
    # Read the reference and hypothesis texts from the files
    with open(reference_file, 'r') as ref_file:
        reference = ref_file.read()

    with open(hypothesis_file, 'r') as hyp_file:
        hypothesis = hyp_file.read()

    # Calculate the CER
    cer = Levenshtein.distance(reference, hypothesis) / len(reference)

    return cer

# Specify the file paths for the reference and hypothesis texts
reference_file = 'reference.txt'
hypothesis_file = 'hypothesis.txt'

# Calculate the CER
cer = calculate_cer_for_file(reference_file, hypothesis_file)

# Print the CER
print(f"Character Error Rate (CER): {cer}")
