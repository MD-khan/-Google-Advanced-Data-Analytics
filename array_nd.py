import numpy as np

# Example aqi_array (you can replace this with your actual array)
aqi_array = np.array([5.2, 6.1, 3.8, 4.7, 7.0, 2.9, 6.3, 5.0, 4.0])

# 1. Create a Boolean array where True indicates an AQI reading is under 6
boolean_aqi = aqi_array < 6

# 2. Calculate the percentage of AQI readings under 6
#    np.sum(boolean_aqi) counts how many True values there are.
percent_under_6 = np.sum(boolean_aqi) / len(aqi_array) * 100

# Print the result
print("Percentage of AQI readings considered cleanest (under 6):", percent_under_6)
