with open("ppa_notes.txt","r") as f:
    print(f.read())

with open("ppa_notes.txt", "r") as f:
    for line in f:
        print(line.strip())  # .strip() removes \n

with open("ppa_notes.txt","r") as f:
    first_line = f.readline()
    print(first_line)


with open("ppa_logs.txt", "a") as f:
    f.write("Again Adding a new log entry...\n")
