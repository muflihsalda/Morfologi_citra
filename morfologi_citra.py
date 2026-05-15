import cv2  
import numpy as np
from skimage import measure
from matplotlib import pyplot as plt

# 1. Baca dan preprocessing
img = cv2.imread('sel_darah.jpg') 

# Cek apakah gambar berhasil dimuat untuk menghindari error !_src.empty()
if img is None:
    print("Error: File 'sel_darah.jpg' tidak ditemukan di folder proyek!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 2. Threshold Otsu (mengubah ke biner)
    # Menggunakan THRESH_BINARY_INV karena sel biasanya lebih gelap dari background
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 3. Elemen penstruktur elips (7x7) sesuai petunjuk tugas
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    # 4. Operasi Morfologi
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1) # Hapus noise kecil
    cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=1) # Tutup celah dalam sel

    # 5. Hitung dan label setiap sel (BAGIAN YANG DITAMBAHKAN)
    labels = measure.label(cleaned)
    regions = measure.regionprops(labels)

    # Menghitung jumlah sel dengan filter luas area (misal > 500 piksel)
    # Ini mendefinisikan variabel 'count' agar tidak error lagi
    count = len([r for r in regions if r.area > 500])

    print(f"Berhasil menghitung {count} sel.")

    # 6. Visualisasi Hasil
    plt.figure(figsize=(12, 6))

    # Menampilkan Gambar Asli
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    # Menampilkan Hasil Akhir Morfologi (Cleaned)
    plt.subplot(1, 2, 2)
    plt.imshow(cleaned, cmap='gray')
    plt.title(f'Hasil Segmentasi\nTerdeteksi: {count} Sel')
    plt.axis('off')

    plt.tight_layout()
    plt.show()