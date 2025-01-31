epa_tuples = [
    ('Arizona', 'Maricopa', 18.0), 
    ('Arizona', 'Maricopa', 9.0),
    ('Arizona', 'Pima', 20.0),
    ('California', 'Alameda', 11.0), 
    ('California', 'Butte', 6.0), 
    ('California', 'Fresno', 11.0), 
    ('California', 'Kern', 7.0), 
    ('California', 'Kern', 3.0), 
    ('California', 'Kern', 7.0), 
    ('California', 'Los Angeles', 13.0), 
    ('California', 'Los Angeles', 18.0), 
    ('California', 'Mono', 5.0), 
    ('California', 'Sacramento', 35.0), 
    ('California', 'San Bernardino', 18.0), 
    ('California', 'San Diego', 23.0), 
    ('California', 'Santa Barbara', 0.0), 
    ('California', 'Shasta', 11.0), 
    ('Colorado', 'El Paso', 9.0), 
    ('Florida', 'Duval', 15.0), 
    ('Florida', 'Duval', 13.0), 
    ('Florida', 'Hillsborough', 19.0), ('Hawaii', 'Honolulu', 10.0), ('Illinois', 'Sangamon', 20.0), ('Indiana', 'Marion', 32.0), ('Kentucky', 'Henderson', 8.0), ('Kentucky', 'Jefferson', 6.0), ('Kentucky', 'McCracken', 13.0), ('Kentucky', 'McCracken', 13.0), ('Louisiana', 'East Baton Rouge', 5.0), ('Maryland', 'Baltimore (City)', 33.0), ('Massachusetts', 'Suffolk', 13.0), ('Michigan', 'Wayne', 19.0), ('Minnesota', 'Saint Louis', 16.0), ('Missouri', 'Saint Louis', 10.0), ('New Jersey', 'Bergen', 41.0), ('New Jersey', 'Middlesex', 17.0), ('New Mexico', 'Bernalillo', 11.0), ('New Mexico', 'San Juan', 6.0), ('New York', 'New York', 13.0), ('New York', 'New York', 24.0), ('New York', 'Niagara', 13.0), ('North Carolina', 'Mecklenburg', 28.0), ('Ohio', 'Franklin', 10.0), ('Ohio', 'Hamilton', 17.0), ('Oklahoma', 'Oklahoma', 14.0), ('Oregon', 'Klamath', 31.0), ('Oregon', 'Multnomah', 28.0), ('Pennsylvania', 'Erie', 7.0), ('Pennsylvania', 'Philadelphia', 13.0), ('Tennessee', 'Shelby', 38.0), ('Texas', 'Bexar', 22.0), ('Utah', 'Salt Lake', 19.0), ('Vermont', 'Chittenden', 18.0), ('Vermont', 'Chittenden', 20.0), ('Virginia', 'Fairfax', 39.0), ('Virginia', 'Norfolk City', 15.0), ('Virginia', 'Richmond City', 17.0), ('Washington', 'King', 55.0), ('Washington', 'King', 22.0), ('Washington', 'Yakima', 35.0), ('Wisconsin', 'Milwaukee', 10.0), ('Arizona', 'Maricopa', 56.0), ('Arizona', 'Pima', 30.0), ('California', 'Humboldt', 30.0), ('California', 'Humboldt', 11.0), ('California', 'Riverside', 18.0), ('California', 'San Bernardino', 11.0), ('California', 'San Bernardino', 22.0), ('California', 'San Bernardino', 11.0), ('California', 'San Diego', 24.0), ('California', 'Santa Barbara', 11.0), ('California', 'Santa Barbara', 7.0), ('California', 'Santa Clara', 11.0), ('California', 'Sonoma', 11.0), ('California', 'Stanislaus', 0.0), ('Colorado', 'Boulder', 28.0), ('Colorado', 'El Paso', 9.0), ('Colorado', 'El Paso', 9.0), ('Hawaii', 'Honolulu', 6.0), ('Illinois', 'Sangamon', 26.0), ('Indiana', 'Marion', 27.0), ('Iowa', 'Polk', 14.0), ('Kansas', 'Sedgwick', 16.0), ('Louisiana', 'Orleans', 5.0), ('Maryland', 'Allegany', 9.0), ('Maryland', 'Montgomery', 24.0), ('Michigan', 'Wayne', 17.0), ('Minnesota', 'Hennepin', 16.0), ('Missouri', 'Clay', 6.0), ('Missouri', 'Jackson', 3.0), ('Montana', 'Missoula', 14.0), ('Nevada', 'Washoe', 52.0), ('Nevada', 'Washoe', 8.0), ('New Jersey', 'Camden', 7.0), ('New Mexico', 'San Juan', 17.0), ('New Mexico', 'San Juan', 14.0), ('New York', 'Monroe', 18.0), ('New York', 'Niagara', 6.0), ('New York', 'Schenectady', 19.0), ('Ohio', 'Franklin', 11.0), ('Ohio', 'Lucas', 13.0), ('Oklahoma', 'Cleveland', 7.0), ('Oklahoma', 'Tulsa', 13.0), ('Oklahoma', 'Tulsa', 16.0), ('Pennsylvania', 'Dauphin', 6.0), ('Pennsylvania', 'Lancaster', 5.0), ('Pennsylvania', 'Philadelphia', 10.0), ('Tennessee', 'Shelby', 74.0), ('Texas', 'Bexar', 6.0), ('Texas', 'Dallas', 2.0), ('Utah', 'Davis', 22.0), ('Utah', 'Salt Lake', 19.0), ('Virginia', 'Fairfax', 15.0), 
              ('Virginia', 'Alexandria City', 13.0)]
aqi_dict = {}
for state,county, aqi in epa_tuples:
    if state not in aqi_dict:
        aqi_dict[state] = []
    aqi_dict[state].append((county,aqi))
print(aqi_dict['Vermont'])