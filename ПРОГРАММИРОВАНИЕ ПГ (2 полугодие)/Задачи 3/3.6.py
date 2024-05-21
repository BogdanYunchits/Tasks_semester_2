import os
import csv

def calculate_directory_statistics(directory):
    statistics = {
        "total_age": 0,
        "count": 0,
        "location_counts": {}
    }

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            with open(os.path.join(directory, filename), newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    age = int(row.get("Age", 0))
                    location = row.get("Location", "Unknown")
                    statistics["total_age"] += age
                    statistics["count"] += 1
                    if location not in statistics["location_counts"]:
                        statistics["location_counts"][location] = 0
                    statistics["location_counts"][location] += 1

    average_age = statistics["total_age"] / statistics["count"] if statistics["count"] != 0 else 0
    print(f"Average Age: {average_age}")
    print("Location Distribution:")
    for location, count in statistics["location_counts"].items():
        print(f"{location}: {count}")

calculate_directory_statistics("data")
