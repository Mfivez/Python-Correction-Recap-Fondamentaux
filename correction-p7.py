# region 1.
import json
import csv
from pathlib import Path


file = Path("test.json")


with file.open('w', encoding="utf-8") as f:
    data = {
        "nom": "aze",
        "age": 15
    }

    json.dump(data, f)

with file.open('r', encoding="utf-8") as f:
    print(json.load(f))
# endregion

# region 2
file_csv = Path("test.csv")

with file_csv.open("r", newline="", encoding="utf-8") as f2:
    reader = csv.reader(f2, delimiter=';')

    for line in reader:
        print(line)

with file_csv.open("a", newline="", encoding="utf-8") as f3:
    f3.write("\n")
    
    writer = csv.writer(f3, delimiter=';')
    writer.writerow(["a", "b", "c"])
# endregion