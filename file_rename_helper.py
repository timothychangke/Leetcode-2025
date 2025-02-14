import os
import re

directory = "Arrays"  
pattern = re.compile(r"^(\d+)\.([EMH])-(.*?)\.py$")

for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        tries = match.group(1) 
        difficulty = match.group(2) 
        name = match.group(3)  

        new_filename = f"{difficulty}.{name}-{tries}.py"  
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

print("✅ Renaming complete!")

