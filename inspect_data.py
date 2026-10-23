import csv

def inspect_column(filename, column):
    with open("oyo_state_health_facilities.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values), 
        "largest": max(values),
        "count": len(values),
    }

latitude_result = inspect_column("oyo_state_health_facilities.csv", "latitude")
longitude_result = inspect_column("oyo_state_health_facilities.csv", "longitude")

print("Latitude:", latitude_result)
print("Longitude:", longitude_result)