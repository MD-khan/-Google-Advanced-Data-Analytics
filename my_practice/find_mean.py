
#Write a function mean_aqi_by_state(data) 
# that calculates the mean AQI (average AQI) for each state.
def mean_aqi_by_state(data):
    # need to find counties which are associate with a state
    # sum the counties and store it in a variavle
    # sum aqi for these counties
    # devide total aqi by the total counties
    state_aqi = {}
    state_count = {}
    for state,county,aqi in data:
        #Sum AQI values per state
        state_aqi[state] = state_aqi.get(state,0) + aqi
        # Count AQI requre per state
        state_count[state] = state_count.get(state,0) + 1
    # Calculate mean AQI for each state
    mean_aqi = {state: state_aqi[state] / state_count[state] for state in state_aqi }
    return mean_aqi

data = [
    ('Arizona', 'Maricopa', 18.0),
    ('Arizona', 'Pima', 20.0),
    ('California', 'Los Angeles', 13.0),
    ('California', 'Alameda', 11.0),
    ('Texas', 'Harris', 14.0),
    ('Texas', 'Dallas', 10.0),
    ('California', 'Los Angeles', 15.0)
]

print(mean_aqi_by_state(data))

