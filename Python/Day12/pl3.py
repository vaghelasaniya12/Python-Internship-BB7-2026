from pathlib import Path

file_path = Path("data/raw_data.txt")

absolute_path = file_path.resolve()

print("Relative path:", file_path)
print("Absolute path:", absolute_path)