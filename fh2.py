import csv

# Data to write
data = [
    ["name", "role", "team"],
    ["Sudhanshu", "Data Analyst", "PPA"],
    ["Aman", "Developer", "Python Team"]
]

# Write CSV
with open("ppa_team.csv", "w", newline='') as f:
    team = csv.writer(f)
    team.writerows(data)

print("CSV file written successfully.")

with open("ppa_team.csv","r") as f:
    team = csv.reader(f)
    for row in team:
        print(row)