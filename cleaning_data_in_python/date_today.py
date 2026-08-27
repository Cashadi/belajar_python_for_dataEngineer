import pandas as pd
import datetime as dt

# Load data dari folder datasets
ride_sharing = pd.read_csv('datasets/ride_sharing_new.csv')

# Cek nama-nama kolom yang ada
print(ride_sharing.columns)