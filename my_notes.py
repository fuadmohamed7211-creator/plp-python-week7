# my_notes.py

predefined_notes = [
    "First note: Python file handling is essential.\n",
    "Second note: Always use context managers ('with' statement).\n",
    "Third note: Close files properly or let context managers handle it.\n"
]

with open("notes.txt", "w") as f:
    f.writelines(predefined_notes)

with open("notes.txt", "a") as f:
    f.write("Fourth note: Appending data works seamlessly.\n")

line_count = 0
print("Reading notes from 'notes.txt':")
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())
        line_count += 1

print(f"\nTotal line count: {line_count}")
