```markdown
# Proyek Analisis Data: Dataset Bike Sharing 🚴‍♂️

Proyek ini bertujuan untuk menganalisis dataset peminjaman sepeda menggunakan Python dan visualisasi untuk menjawab beberapa pertanyaan bisnis terkait pola peminjaman sepeda.

## Detail Proyek
- **Nama:** Aditya Putra Afendi
- **Email:** m200b4ky0113@bangkit.academy
- **ID Dicoding:** aditya_putra_afendi_m200b4ky0113_CveJ
- **Link Streamlit:** [https://adityaputra.streamlit.app/](https://adityaputra.streamlit.app/)

### Pertanyaan Bisnis
1. Pada jam berapa peminjaman sepeda paling banyak terjadi dalam sehari?
2. Apakah terdapat perbedaan pola peminjaman antara hari kerja dan akhir pekan?

## Fitur Utama
- **Visualisasi Pola Peminjaman Sepeda Berdasarkan Jam**: Menggunakan *line plot* untuk menunjukkan rata-rata peminjaman sepeda per jam.
- **Analisis Peminjaman Berdasarkan Hari Kerja vs. Akhir Pekan**: Menggunakan *bar plot* untuk menganalisis peminjaman sepeda berdasarkan status hari (kerja atau akhir pekan).
- **Pembersihan Data**: Deteksi dan penghapusan nilai duplikat dan nilai yang hilang dari dataset.
- **Eksplorasi Data Lanjutan**: Visualisasi korelasi antar variabel menggunakan *heatmap*.

## Setup Environment

### Menggunakan Anaconda
1. Buat environment baru dengan Python 3.9:
   ```bash
   conda create --name proyek_bike_sharing python=3.9
   ```
2. Aktifkan environment:
   ```bash
   conda activate proyek_bike_sharing
   ```
3. Install dependencies yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

### Menggunakan Shell/Terminal
1. Buat folder proyek:
   ```bash
   mkdir proyek_bike_sharing
   cd proyek_bike_sharing
   ```
2. Inisialisasi virtual environment menggunakan venv:
   ```bash
   python -m venv venv
   ```
3. Aktifkan virtual environment:
   - Untuk Unix/macOS:
     ```bash
     source venv/bin/activate
     ```
   - Untuk Windows:
     ```bash
     venv\Scripts\activate
     ```
4. Install dependencies dari file `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi
Setelah semua dependensi terinstal, Anda bisa menjalankan analisis dengan cara berikut:

```bash
streamlit run app.py
```

Hasil visualisasi akan ditampilkan pada jendela output atau dalam grafik yang dihasilkan.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama.
- **Pandas**: Untuk manipulasi dan analisis data.
- **Seaborn & Matplotlib**: Untuk visualisasi data.

## Struktur Direktori
```
proyek_bike_sharing/
│
├── app.py                # File utama untuk analisis dan visualisasi
├── README.md             # File ini
├── requirements.txt      # Daftar dependensi Python
├── day.csv               # Dataset peminjaman sepeda harian
└── hour.csv              # Dataset peminjaman sepeda per jam
```

## Lisensi
Proyek ini tidak memiliki lisensi dan digunakan untuk keperluan edukasi.

