# Day 5: pair each assignment title with its due date

file_path = "data/icalexport.ics"

with open(file_path, encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()

assignments = []
title = ""

for line in lines:
    if line.startswith("SUMMARY:"):
        title = line[len("SUMMARY:"):]
    if line.startswith("DTSTART"):
        date_text = line.split(":")[1]
        due = date_text[:8]
        assignment = {"title": title, "due": due}
        assignments.append(assignment)

for assignment in assignments:
    due = assignment["due"]
    short_date = due[4:6] + "/" + due[6:8]
    print(short_date, "-", assignment["title"])

print("Total:", len(assignments))