with open("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    area_hectares = area_km2 * 100
    print(ward, "is", area_hectares, "hectares")
    