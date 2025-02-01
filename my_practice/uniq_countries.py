#Write a function unique_counties(data) 
# that returns the number of unique counties in the dataset.
data = [
    ('Arizona', 'Maricopa', 18.0),
    ('Arizona', 'Pima', 20.0),
    ('California', 'Los Angeles', 13.0),
    ('California', 'Alameda', 11.0),
    ('Texas', 'Harris', 14.0),
    ('Texas', 'Dallas', 10.0),
    ('California', 'Los Angeles', 15.0)
]

def unique_counties(data):
    unique_county_set = set()
    for state,county, aqi in data:
        unique_county_set.add(county)
    #print(unique_county_set)
    return len(unique_county_set)
       
print(unique_counties(data))