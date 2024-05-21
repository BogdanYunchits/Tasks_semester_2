import csv

def generate_csv_file():
    with open("data.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Age"])
        writer.writerow(["John", "Doe", 30])
        writer.writerow(["Jane", "Smith", 25])
        writer.writerow(["Peter", "Jones", 40])

generate_csv_file()

def read_csv_file(filename):
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))

read_csv_file("data.csv")
