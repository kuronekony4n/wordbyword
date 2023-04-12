import sys
import re

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print("Incorrect argument. Usage: <script_name> <subtitle_file>")
    exit(1)

with open(file_name, "r") as f:
    lines = f.readlines()

print(f"Processing subtitle using wordbyword.. script by: willydev")
for i, line in enumerate(lines):
    if re.match("^\d+\n$", line):
        continue

    if not re.match("^\d{1,2}\s*$", line) and not re.match(
            "^\d{1,2}:\d{2}:\d{2},\d{3} --> \d{1,2}:\d{2}:\d{2},\d{3}\s*$",
            line):
        if len(line.strip().split()) > 1:
            lines[i] = "-\n"
        if line.strip() and not "<font" in line and not re.search("\w+", line):
            lines[i] = "-\n"
        elif "<font" in line:
            word = re.search("<font.*?>(.*?)</font>", line).group(1)
            lines[i] = word + "\n"

new_file_name = file_name.split(".")[0] + "-wordbyword.srt"
with open(new_file_name, "w") as f:
    f.writelines(lines)

print(f"Completed: File saved as {new_file_name}")
