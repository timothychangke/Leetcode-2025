import os
import subprocess

files = subprocess.check_output(["git", "ls-files", "--modified", "--others", "--exclude-standard"]).decode().splitlines()

if not files:
    print("No modified or untracked files to commit.")
else:
    for file in files:
        print(f"Processing: {file}")

        subprocess.run(["git", "add", file])

        commit_message = f"fix({file}): file rename"
        subprocess.run(["git", "commit", "-m", commit_message])

        print(f"Committed: {file}")

    print("All files committed separately!")
