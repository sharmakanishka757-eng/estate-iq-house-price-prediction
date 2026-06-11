import pandas as pd
import random

# Core list of 52 synchronized Bangalore localities
localities = [
    "Indiranagar", "Koramangala", "Malleswaram", "Jayanagar", "Frazer Town", 
    "Domlur", "Old Airport Road", "Basavanagudi", "Rajajinagar", "Sadashivanagar",
    "Whitefield", "HSR Layout", "Bellandur", "Marathahalli", "Sarjapur Road", 
    "Outer Ring Road", "Panathur", "Varthur", "Kadugodi", "KR Puram", 
    "Mahadevapura", "Brookefield", "Hoodi", "Hebbal", "Yelahanka", 
    "Devanahalli", "Hennur Road", "Thanisandra", "Banaswadi", "Jakkar", 
    "RT Nagar", "Sahakara Nagar", "JP Nagar", "Bannerghatta Road", "BTM Layout", 
    "Kanakapura Road", "Hosur Road", "Uttarahalli", "Padmanabhanagar", "Anjanapura", 
    "Begur", "Nagarbhavi", "Vijayanagar", "Tumkur Road", "Kengeri", 
    "Yeshwanthpur", "Magadi Road", "Rayan Circle", "Electronic City Phase 1", 
    "Electronic City Phase 2", "Bommasandra", "Chandapura", "Electronic City", "CV Raman Nagar"
]

property_types = ["Apartment", "Independent House", "Villa", "Penthouse"]
furnishing_statuses = ["Unfurnished", "Semi-Furnished", "Fully-Furnished"]

# Base 2026 Estimated Market Rates per Sq Ft
loc_rates = {
    "Sadashivanagar": 22000, "Indiranagar": 17500, "Koramangala": 17000, "Malleswaram": 16500,
    "Jayanagar": 15500, "Frazer Town": 15000, "Basavanagudi": 14800, "Domlur": 14500,
    "Rajajinagar": 14000, "Old Airport Road": 13800, "HSR Layout": 13500, "Bellandur": 13000,
    "Outer Ring Road": 12800, "Brookefield": 12200, "Hebbal": 12000, "Whitefield": 11500,
    "Mahadevapura": 11200, "Hoodi": 10800, "Sahakara Nagar": 10500, "RT Nagar": 10200,
    "JP Nagar": 11000, "Hennur Road": 10500, "Thanisandra": 10200, "Sarjapur Road": 10000,
    "Panathur": 9900, "Varthur": 9800, "Marathahalli": 9800, "Kanakapura Road": 9600,
    "Yelahanka": 9500, "Jakkar": 9400, "KR Puram": 9200, "Kadugodi": 9100,
    "Banaswadi": 9000, "Vijayanagar": 9500, "Nagarbhavi": 9200, "Bannerghatta Road": 9400,
    "Yeshwanthpur": 9800, "Padmanabhanagar": 9000, "Uttarahalli": 8500, "Hosur Road": 8400,
    "Begur": 8000, "Kengeri": 7800, "Devanahalli": 7500, "Tumkur Road": 7200,
    "Magadi Road": 7400, "Electronic City Phase 1": 7200, "Electronic City Phase 2": 6800,
    "Bommasandra": 6200, "Chandapura": 5500, "Anjanapura": 7000, "Rayan Circle": 11000,
    "BTM Layout": 11200, "Electronic City": 7200, "CV Raman Nagar": 9600
}

data = []
random.seed(42)

for _ in range(4000):
    loc = random.choice(localities)
    prop_type = random.choice(property_types)
    bhk = random.choice([1, 2, 3, 4])
    bathrooms = bhk if bhk == 1 else bhk + random.choice([-1, 0, 1])
    bathrooms = max(1, min(bathrooms, 5))
    
    floor_num = random.randint(0, 15)
    total_floors = random.randint(floor_num, 20)
    age = random.choice([0, 2, 5, 10, 15])
    furnishing = random.choice(furnishing_statuses)
    parking = random.choice([0, 1, 2])
    
    if bhk == 1: area = random.randint(500, 850)
    elif bhk == 2: area = random.randint(900, 1400)
    elif bhk == 3: area = random.randint(1450, 2200)
    else: area = random.randint(2300, 4500)
        
    amenities = {
        'near_metro': random.choice([0, 1]), 'gated': random.choice([0, 1]), 'near_school': random.choice([0, 1]),
        'near_it_park': random.choice([0, 1]), 'pool': random.choice([0, 1]), 'gym': random.choice([0, 1]),
        'security': random.choice([0, 1]), 'garden': random.choice([0, 1]), 'clubhouse': random.choice([0, 1]),
        'play_area': random.choice([0, 1]), 'backup': random.choice([0, 1]), 'rainwater': random.choice([0, 1]),
        'ev_charging': random.choice([0, 1]), 'cctv': random.choice([0, 1]), 'intercom': random.choice([0, 1]),
        'rooftop': random.choice([0, 1])
    }

    # Math Logic Generation Model Core
    price = area * loc_rates[loc]
    if prop_type == "Villa": price *= 1.45
    if prop_type == "Penthouse": price *= 1.35
    price += (bathrooms * 175000) - (age * 65000) + (parking * 300000)
    if furnishing == "Fully-Furnished": price += 500000
    if furnishing == "Semi-Furnished": price += 200000
    price += (sum(amenities.values()) * 95000)
    price += random.randint(-200000, 200000)
    
    row = [loc, prop_type, area, bhk, bathrooms, floor_num, total_floors, age, furnishing, parking] + list(amenities.values()) + [int(price)]
    data.append(row)

cols = ['location', 'property_type', 'area', 'rooms', 'bathrooms', 'floor_number', 'total_floors', 'age_of_property', 'furnishing_status', 'parking_spaces'] + list(amenities.keys()) + ['price']
df = pd.DataFrame(data, columns=cols)
df.to_csv('data.csv', index=False)
print("✅ Successfully generated unified data.csv.")