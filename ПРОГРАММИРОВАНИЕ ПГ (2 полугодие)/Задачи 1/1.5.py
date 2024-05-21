import csv

def calculate_column_averages(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        columns = []
        for row in reader:
            if not columns:
                columns = [[] for _ in row]
            for i, value in enumerate(row):
                columns[i].append(float(value))

        averages = [sum(col) / len(col) for col in columns]
        for i, average in enumerate(averages):
            print(f"Average of column {i + 1}: {average}")

filename = input("Enter the name of the CSV file: ")
calculate_column_averages(filename)
