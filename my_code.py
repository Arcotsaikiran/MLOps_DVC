import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create a sample dataframe with columns

data = {
    'Name' :['Alice' , 'sam', 'Charlie'],
    'Age' : [25,23,32],
    'City' : ['New york', 'Bangalore', 'LA']
}

df = pd.DataFrame(data)

# Ensuring data directory exists

data_dir = 'data'
os.makedirs(data_dir,exist_ok= True)


# Define file path

file_path = os.path.join(data_dir,'sample_data.csv')


# Save the dataframe to CSV file, including column names

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")