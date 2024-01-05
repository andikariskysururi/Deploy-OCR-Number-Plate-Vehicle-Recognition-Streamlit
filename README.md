# Deployment Number Plate Vehicle Recognition with YOLOv5

## Deskripsi
Proyek ini adalah implementasi pengenalan plat nomor kendaraan menggunakan YOLOv5, Streamlit, dan beberapa paket lainnya. YOLOv5 merupakan model deteksi objek yang efisien dan tepat, sedangkan Streamlit digunakan untuk membuat antarmuka pengguna yang interaktif.

## Penggunaan
1. Instal semua paket yang diperlukan dengan menjalankan perintah berikut:
    ```bash
    pip install streamlit pandas ultralytics
    ```

2. Pastikan untuk memiliki gambar kendaraan dengan plat nomor yang ingin diidentifikasi.

3. Jalankan aplikasi dengan menjalankan perintah berikut di terminal:
    ```bash
    streamlit run app.py
    ```

4. Buka browser dan akses URL yang ditampilkan pada terminal setelah menjalankan perintah di langkah sebelumnya.

## Package 
Berikut adalah package yang digunakan dalam aplikasi Streamlit:

```python
import streamlit as st
from PIL import Image
import pandas as pd
from ultralytics import YOLO
import io

