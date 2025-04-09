#!/usr/bin/env python3

"""
A simple script to verify the spelling issue in nested_min_max.py.
"""

import os
import re

def check_spelling_in_file(file_path, word_to_check):
    """Check if a specific misspelled word exists in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r'\b' + re.escape(word_to_check) + r'\b'
        matches = re.findall(pattern, content)
        return len(matches) > 0

if __name__ == "__main__":
    file_path = "pylint/checkers/nested_min_max.py"
    misspelled_word = "redunant"
    
    if os.path.exists(file_path):
        if check_spelling_in_file(file_path, misspelled_word):
            print(f"Found misspelled word '{misspelled_word}' in {file_path}")
            print("Test FAILED")
            exit(1)
        else:
            print(f"No misspelled word '{misspelled_word}' found in {file_path}")
            print("Test PASSED")
            exit(0)
    else:
        print(f"File {file_path} does not exist")
        exit(1)