import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import os

# Download dataset dari Kaggle
path = kagglehub.dataset_download("heptapod/titanic")

# Lihat isi folder dataset
print(os.listdir(path))

# Tentukan lokasi file yang benar
file = os.path.join(path, 'train_and_test2.csv')

# Baca dataset
data = pd.read_csv(file)

# Tampilkan 5 data pertama
print("\n=== HEAD ===")
print(data.head())

# Tampilkan 5 data terakhir
print("\n=== TAIL ===")
print(data.tail())

# Tampilkan nama kolom
print("\n=== COLUMNS ===")
print(data.columns.tolist())

# Tampilkan ukuran dataset
print("\n=== SHAPE ===")
print(data.shape)

# Tampilkan informasi dataset
print("\n=== INFO ===")
print(data.info())

# Tampilkan statistik
print("\n=== DESCRIBE ===")
print(data.describe())