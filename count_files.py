import os
import re

parent_folders = [
    "Arrays", "Binary Search", "Graphs", "Heap", "Linked List", "Sliding Window", "Stack", "Trees", "Two Pointers", "2-D Dynamic Programming", "Backtracking"
]

pattern = re.compile(r"^(E|M|H)\.([\w\s]+)-\d+\.py$")

def count_files_in_folder(folder):
    file_count = 0
    unique_problems = set()
    difficulty_counts = {"E": 0, "M": 0, "H": 0}
    unique_difficulty_counts = {"E": set(), "M": set(), "H": set()}

    if os.path.exists(folder):
        for _, _, files in os.walk(folder):
            for file in files:
                file_count += 1
                match = pattern.match(file)
                if match:
                    difficulty, problem_name = match.groups()
                    difficulty_counts[difficulty] += 1
                    unique_problems.add(f"{difficulty}.{problem_name.strip()}-")
                    unique_difficulty_counts[difficulty].add(problem_name.strip())

    return file_count, unique_problems, difficulty_counts, unique_difficulty_counts

if __name__ == "__main__":
    folder_counts = {}
    total_files = 0
    total_unique_problems = set()
    total_difficulty_counts = {"E": 0, "M": 0, "H": 0}
    total_unique_difficulty_counts = {"E": set(), "M": set(), "H": set()}

    for folder in parent_folders:
        file_count, unique_problems, difficulty_counts, unique_difficulty_counts = count_files_in_folder(folder)
        folder_counts[folder] = (file_count, len(unique_problems), difficulty_counts, unique_difficulty_counts)
        total_files += file_count
        total_unique_problems.update(unique_problems)
        
        for diff in ["E", "M", "H"]:
            total_difficulty_counts[diff] += difficulty_counts[diff]
            total_unique_difficulty_counts[diff].update(unique_difficulty_counts[diff])

    with open("statistics.txt", "w") as f:
        for folder, (file_count, unique_count, difficulty_counts, unique_difficulty_counts) in folder_counts.items():
            f.write(f"{folder}: {file_count} problems, {unique_count} unique\n")
            f.write(f"  - Total: {difficulty_counts['E']} Easy, {difficulty_counts['M']} Medium, {difficulty_counts['H']} Hard\n")
            f.write(f"  - Unique: {len(unique_difficulty_counts['E'])} Easy, {len(unique_difficulty_counts['M'])} Medium, {len(unique_difficulty_counts['H'])} Hard\n\n")

        f.write(f"\nTotal number of problems: {total_files}\n")
        f.write(f"Total unique problems: {len(total_unique_problems)}\n")
        f.write(f"\nTotal by difficulty:\n")
        f.write(f"  - Easy: {total_difficulty_counts['E']} problems, {len(total_unique_difficulty_counts['E'])} unique\n")
        f.write(f"  - Medium: {total_difficulty_counts['M']} problems, {len(total_unique_difficulty_counts['M'])} unique\n")
        f.write(f"  - Hard: {total_difficulty_counts['H']} problems, {len(total_unique_difficulty_counts['H'])} unique\n")
    
    for folder, (file_count, unique_count, difficulty_counts, unique_difficulty_counts) in folder_counts.items():
        print(f"{folder}: {file_count} problems, {unique_count} unique problems")
        print(f"  - Easy: {difficulty_counts['E']} problems, {len(unique_difficulty_counts['E'])} unique")
        print(f"  - Medium: {difficulty_counts['M']} problems, {len(unique_difficulty_counts['M'])} unique")
        print(f"  - Hard: {difficulty_counts['H']} problems, {len(unique_difficulty_counts['H'])} unique")
    
    print(f"\nTotal number of files: {total_files}")
    print(f"Total unique problems: {len(total_unique_problems)}")
    print(f"\nTotal by difficulty:")
    print(f"  - Easy: {total_difficulty_counts['E']} problems, {len(total_unique_difficulty_counts['E'])} unique")
    print(f"  - Medium: {total_difficulty_counts['M']} problems, {len(total_unique_difficulty_counts['M'])} unique")
    print(f"  - Hard: {total_difficulty_counts['H']} problems, {len(total_unique_difficulty_counts['H'])} unique")
