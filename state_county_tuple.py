# 1. ### YOUR CODE HERE ###
state_names = ['Arizona', 'California', 'California', 'Kentucky','Louisiana']

# 2. ### YOUR CODE HERE ###
county_names = ['Maricopa', 'Alameda', 'Sacramento','Jefferson','East Baton Rouge']
state_county_tuples = []

for i in range(min(len(state_names), len(county_names))):
    state_county_tuples.append((state_names[i],county_names[i]))
print(state_county_tuples)


