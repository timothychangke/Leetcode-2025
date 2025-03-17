import os
import subprocess
import re
from datetime import datetime

today_date = datetime.today().strftime("%Y-%m-%d")

num_to_word = {
    "1": "first",
    "2": "second",
    "3": "third",
    "4": "fourth",
    "5": "fifth",
    "6": "sixth",
    "7": "seventh",
    "8": "eighth",
    "9": "ninth",
    "10": "tenth"
}

pattern = re.compile(r"^(?:.*/)?([EMH])\.(.*?)-(\d+)\.py$")

subprocess.run(["python3", "count_files.py"])

files = subprocess.check_output(["git", "ls-files", "--modified", "--others", "--exclude-standard"]).decode().splitlines()

if not files:
    print("No modified or untracked files to commit.")
else:
    for file in files:
        match = pattern.match(file)
        if match:
            difficulty = match.group(1)  
            name = match.group(2)        
            tries = match.group(3)      

            tries_word = num_to_word.get(tries, f"{tries}th") 
            
            commit_message = f"feat({file}): {tries_word} attempt completed {today_date}"
            
            print(f"Processing: {file}")
            subprocess.run(["git", "add", file])
            subprocess.run(["git", "add", 'statistics.txt'])
            subprocess.run(["git", "commit", "-m", commit_message])
            print(f"Committed: {file} with message: '{commit_message}'")
        else:
            print(f"Skipping {file} (does not match expected pattern)")

    print("✅ All files committed separately!")
