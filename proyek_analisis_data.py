# streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Proyek Analisis Data: Bike Sharing")

# Load datasets from the local Bike-sharing-dataset folder
st.header("Load Data")
day_df = pd.read_csv('Bike-sharing-dataset/day.csv')
hour_df = pd.read_csv('Bike-sharing-dataset/hour.csv')

# Show the first few rows of the day.csv dataset
st.subheader("Data Harian")
st.write(day_df.head())

# Show the first few rows of the hour.csv dataset
st.subheader("Data Jam")
st.write(hour_df.head())

# Data Wrangling - converting date columns to datetime format
st.header("Data Wrangling")
try:
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    st.success("Kolom dteday berhasil diubah menjadi format datetime.")
except ValueError as e:
    st.error(f"Error converting 'dteday' to datetime: {e}")
    st.write("Unique values in 'dteday' column:", hour_df['dteday'].unique())

# Exploratory Data Analysis (EDA)
st.header("Exploratory Data Analysis (EDA)")

# Plotting the distribution of total bike rentals in the daily dataset
st.subheader("Distribusi Jumlah Peminjaman Sepeda Harian")
fig, ax = plt.subplots()
sns.histplot(day_df['cnt'], kde=True, ax=ax)
ax.set_title('Distribusi Jumlah Peminjaman Sepeda Harian')
ax.set_xlabel('Jumlah Peminjaman')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

# Analyzing the effect of weather on daily bike rentals
st.subheader("Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda Harian")
fig, ax = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=day_df, ax=ax)
ax.set_title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda Harian')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Analyzing hourly rental patterns
st.subheader("Pola Peminjaman Sepeda pada Berbagai Jam dalam Sehari")
hourly_avg = hour_df.groupby('hr').mean(numeric_only=True).reset_index()

fig, ax = plt.subplots()
sns.lineplot(x='hr', y='cnt', data=hourly_avg, ax=ax)
ax.set_title('Pola Peminjaman Sepeda pada Berbagai Jam dalam Sehari')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Jumlah Peminjaman')
st.pyplot(fig)

# Conclusion
st.header("Conclusion")
st.write("""
- **Pengaruh Cuaca:** Kondisi cuaca sangat mempengaruhi jumlah peminjaman sepeda. Cuaca cerah meningkatkan peminjaman, sedangkan cuaca buruk menurunkannya.
- **Pola Jam Sibuk:** Peminjaman sepeda meningkat pada jam-jam sibuk seperti pagi dan sore hari, menunjukkan penggunaan untuk perjalanan kerja atau sekolah.
""")
