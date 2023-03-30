import sys
import re

if len(sys.argv) > 1 and sys.argv[1] == "-i" and len(sys.argv) > 2:
    file_name = sys.argv[2]
else:
    sys.exit()

with open(file_name, "r") as f:
    lines = f.readlines()

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

    print(f"Processing line {i+1}")

new_file_name = file_name.split(".")[0] + "-wordbyword.srt"

with open(new_file_name, "w") as f:
    f.writelines(lines)

print(f"New subtitle file saved as {new_file_name}")