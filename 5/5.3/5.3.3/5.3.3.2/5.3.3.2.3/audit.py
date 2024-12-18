import os

outcome = "5/5.3/5.3.3/5.3.3.2/5.3.3.2.3/outcome"

# Open the file and read the lines
with open(outcome, 'r') as file:
    lines = file.readlines()

# Check if there are at least five lines
if len(lines) < 5:
    print("The file does not have enough lines.")
else:
    # Extract the last word from each line
    last_words = [line.strip().split()[-1] for line in lines[:5]]

    # Expected values
    expected_last_words = ["4", "-2", "-2", "-2", "-2"]

    # Compare the extracted last words with the expected values
    if last_words == expected_last_words:
        print("5.3.3.2.3 | Ensure password complexity is configured | yes")
    else:
        print("5.3.3.2.3 | Ensure password complexity is configured | no")
