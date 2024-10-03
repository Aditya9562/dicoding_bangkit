# app.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul aplikasi
st.title("Proyek Analisis Data Peminjaman Sepeda")

# Menentukan pertanyaan bisnis
st.header("Pertanyaan Bisnis")
st.write("""
- Apa faktor yang paling memengaruhi jumlah peminjaman sepeda harian?
- Bagaimana pola penggunaan sepeda dipengaruhi oleh musim atau cuaca tertentu?
""")

# Mengumpulkan data
try:
    df = pd.read_csv('day.csv')
    st.write("Data yang dimuat:")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"Error loading data: {e}")

# Menghitung dan menampilkan informasi dasar tentang dataset
st.write("Informasi dasar tentang dataset:")
buffer = df.info()
st.text(buffer)

# Memeriksa missing values
missing_values = df.isnull().sum()
st.write("Jumlah missing values per kolom:")
st.write(missing_values)

# Descriptive statistics
st.write("Statistik deskriptif:")
st.write(df.describe())

# Membersihkan data
df_cleaned = df.drop(columns=['instant'], errors='ignore')  # Using errors='ignore' to avoid errors if column is not found
st.write("Data setelah dibersihkan:")
st.dataframe(df_cleaned.head())

# Visualisasi: Scatter plot antara suhu dan jumlah peminjaman sepeda
st.subheader("Visualisasi: Suhu vs Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=df_cleaned, ax=ax)
ax.set_title('Temperature vs Bike Rentals')
ax.set_xlabel('Temperature')
ax.set_ylabel('Number of Bike Rentals')
st.pyplot(fig)

# Korelasi antara fitur
st.subheader("Korelasi Antara Fitur")
df_numeric = df_cleaned.select_dtypes(include=[np.number])
plt.figure(figsize=(10, 6))
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Features')
st.pyplot(plt)

# Visualisasi: Boxplot untuk musim
st.subheader("Visualisasi: Peminjaman Sepeda berdasarkan Musim")
fig2, ax2 = plt.subplots()
sns.boxplot(x='season', y='cnt', data=df_cleaned, ax=ax2)
ax2.set_title('Bike Rentals Across Seasons')
ax2.set_xlabel('Season')
ax2.set_ylabel('Number of Bike Rentals')
st.pyplot(fig2)

# Kesimpulan
st.header("Kesimpulan")
conclusion_text = """
- Jumlah peminjaman sepeda total (cnt) sangat berkorelasi positif dengan pengguna terdaftar (0.95) dan suhu (0.63).
- Terdapat korelasi positif sedang antara peminjaman dengan musim (0.41) dan tahun (0.57).
- Kecepatan angin (-0.23) dan kelembaban (-0.1) berkorelasi negatif dengan jumlah peminjaman.
- Jumlah peminjaman sepeda lebih tinggi di musim 2 dan 3, sementara peminjaman lebih sedikit di musim 1 dan 4.
"""
st.write(conclusion_text)
