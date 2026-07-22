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

# Tampilkan 5 baris pertama
print(data.head())

# Plot Age dalam histogram
data['Age'].hist()

plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()