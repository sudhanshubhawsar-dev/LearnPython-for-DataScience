# Creating a file and writing content
file = open("ppa_notes.txt", "w")
file.write("Welcome to PPA-Framework Python notes.\n")
file.write("This file is created using Python.\n")
file.close()

print("File created and content written.")

try:
    file = open("ppa_logs.txt", "x")
    file.write("Initial log created.\n")
    file.close()
    print("File created successfully.")
except FileExistsError:
    print("File already exists.")

with open("ppa_summary.txt", "w") as f:
    f.write("Summary report for the automation framework.\n")
    f.write("Generated using Python.\n")
