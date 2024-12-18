import os

outcome = "5/5.3/5.3.3/5.3.3.1/5.3.3.1.3/outcome"

# Open the file and read the lines
with open(outcome, 'r') as file:
    lines = file.readlines()

# Check if there are at least five lines
if len(lines) < 1:
    print("5.3.3.1.3 | Ensure password failed attempts lockout includes root account | no")
else:
    # Extract the last word from each line
    last_words = [line.strip().split()[-1] for line in lines[:2]]

    # Expected values
    expected_last_words = ["even_deny_root", "60"]

    # Compare the extracted last words with the expected values
    if last_words == expected_last_words:
        print("5.3.3.1.3 | Ensure password failed attempts lockout includes root account | yes")
    else:
        print("5.3.3.1.3 | Ensure password failed attempts lockout includes root account | no")
