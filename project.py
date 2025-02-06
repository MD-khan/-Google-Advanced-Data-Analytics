# Import necessary libraries
import pandas as pd

# Create a sample dataset dictionary with the columns provided
data = {
    "Unnamed: 0": [24870114, 35634249, 106203690, 38942136, 30841670, 
                    23345809, 37660487, 69059411, 8433159, 95294817],
    "VendorID": [2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    "tpep_pickup_datetime": [
        "03/25/2017 8:55:43 AM",
        "04/11/2017 2:53:28 PM",
        "12/15/2017 7:26:56 AM",
        "05/07/2017 1:17:59 PM",
        "04/15/2017 11:32:20 PM",
        "03/25/2017 8:34:11 PM",
        "05/03/2017 7:04:09 PM",
        "08/15/2017 5:41:06 PM",
        "02/04/2017 4:17:07 PM",
        "11/10/2017 3:20:29 PM"
    ],
    "tpep_dropoff_datetime": [
        "03/25/2017 9:09:47 AM",
        "04/11/2017 3:19:58 PM",
        "12/15/2017 7:34:08 AM",
        "05/07/2017 1:48:14 PM",
        "04/15/2017 11:49:03 PM",
        "03/25/2017 8:42:11 PM",
        "05/03/2017 8:03:47 PM",
        "08/15/2017 6:03:05 PM",
        "02/04/2017 4:29:14 PM",
        "11/10/2017 3:40:55 PM"
    ],
    "passenger_count": [6, 1, 1, 1, 1, 6, 1, 1, 1, 1],
    "trip_distance": [3.34, 1.80, 1.00, 3.70, 4.37, 2.30, 12.83, 2.98, 1.20, 1.60],
    "RatecodeID": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "store_and_fwd_flag": ['N'] * 10,  # All values are 'N'
    "PULocationID": [100, 186, 262, 188, 4, 161, 79, 237, 234, 239],
    "DOLocationID": [231, 43, 236, 97, 112, 236, 241, 114, 249, 237],
    "payment_type": [1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    "fare_amount": [13.0, 16.0, 6.5, 20.5, 16.5, 9.0, 47.5, 16.0, 9.0, 13.0],
    "extra": [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 1.0, 1.0, 0.0, 0.0],
    "mta_tax": [0.5] * 10,
    "tip_amount": [2.76, 4.00, 1.45, 6.39, 0.00, 2.06, 9.86, 1.78, 0.00, 2.75],
    "tolls_amount": [0.0] * 10,
    "improvement_surcharge": [0.3] * 10,
    "total_amount": [16.56, 20.80, 8.75, 27.69, 17.80, 12.36, 59.16, 19.58, 9.80, 16.55]
}

# Create the DataFrame
df_sample = pd.DataFrame(data)

# Convert the pickup and dropoff datetime columns to datetime objects
df_sample["tpep_pickup_datetime"] = pd.to_datetime(df_sample["tpep_pickup_datetime"])
df_sample["tpep_dropoff_datetime"] = pd.to_datetime(df_sample["tpep_dropoff_datetime"])

# Display the sample DataFrame
print("Sample NYC TLC Data:")
print(df_sample)
