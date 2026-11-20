#Day3: print only the assignment title lines

file_path = "data/icalexport.ics"

with open(file_path, encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()
print("Total lines:", len(lines))

count = 0

for line in lines:
    if line.startswith("SUMMARY:"):
        print(line)
        count = count + 1

print("Assignments:", count)