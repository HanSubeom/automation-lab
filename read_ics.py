# Day 2: read the eCampus calender file and print it

file_path = "data/icalexport.ics"

with open(file_path, encoding="utf-8") as file:
    content = file.read()

print(content)
print("Characters:", len(content))