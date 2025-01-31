state_names = ['Arizona', 'California', 'California', 'Kentucky','Louisiana']
county_names = ['Maricopa', 'Alameda', 'Sacramento','Jefferson','East Baton Rouge']

state_county_tuples = list(zip(state_names, county_names))

print(state_county_tuples)

### YOUR CODE HERE ###
ca_counties = [ county for state,county in state_county_tuples if state == "California" ]
print(ca_counties)