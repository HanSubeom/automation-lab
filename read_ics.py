# Day 4: build the assignment list from the calendar file

file_path = "data/icalexport.ics"
prefix = "SUMMARY:"

with open(file_path, encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

assignments = []

for line in lines:
    if line.startswith(prefix):
        title = line[len(prefix):]
        assignments.append(title)

print("My assignments:")
for assignment in assignments:
    print("-", assignment)

print("Total:", len(assignments))