# Morfologi_citra

<p>Nama :Muflih Salda Maulana</p>
<p>Nim :312410527</p>
<p>Kelas : I241E</p>


# Deteksi Sel Darah dengan Morfologi Citra (Python & OpenCV)

Proyek ini bertujuan untuk melakukan segmentasi dan penghitungan jumlah sel darah merah secara otomatis dari citra mikroskopis menggunakan teknik pengolahan citra digital. Proyek ini merupakan bagian dari tugas mata kuliah Pengolahan Citra Digital (PCD).

## Fitur Utama
* **Prapemrosesan Citra**: Konversi Grayscale dan Gaussian Blur untuk reduksi noise.
* **Segmentasi Otomatis**: Menggunakan Thresholding Otsu untuk memisahkan objek sel dari latar belakang.
* **Operasi Morfologi**: Implementasi Opening dan Closing dengan kernel Elips untuk membersihkan noise dan memperbaiki struktur sel.
* **Penghitungan Objek**: Ekstraksi fitur dan penghitungan jumlah sel menggunakan `skimage.measure`.

## Teknologi yang Digunakan
* **Python**: Bahasa pemrograman utama.
* **OpenCV**: Pustaka untuk pengolahan citra digital.
* **Scikit-Image**: Digunakan untuk analisis properti objek (labeling & counting).
* **Matplotlib**: Digunakan untuk visualisasi hasil perbandingan citra.

## Alur Kerja Program
1. **Load Image**: Membaca file citra `sel_darah.jpg`.
2. **Preprocessing**: Mengubah citra ke Grayscale dan menerapkan Gaussian Blur (5x5).
3. **Binarization**: Menerapkan Thresholding Otsu untuk mendapatkan citra biner.
4. **Morphology**: 
   - **Opening**: Menghilangkan noise kecil di luar sel.
   - **Closing**: Menutup celah kecil di dalam sel agar objek lebih solid.
5. **Labeling**: Mengidentifikasi setiap sel yang terpisah berdasarkan konektivitas piksel.
6. **Output**: Menampilkan citra asli bersisian dengan hasil segmentasi dan jumlah sel terdeteksi.

## Hasil Analisis
Hasil akhir menunjukkan bahwa penggunaan kernel elips (7x7) / (3x3) sangat efektif dalam menjaga detail bentuk sel darah merah. Meskipun terdapat beberapa sel yang menempel sehingga terdeteksi sebagai satu objek, sistem secara keseluruhan mampu memberikan visualisasi segmentasi yang bersih dan representatif untuk analisis medis awal.

## Hasil Akhir Gambar : Saya Menggunkan kernel elips (7x7) dengan kernel, iterations=2)

<img width="1202" height="673" alt="image" src="https://github.com/user-attachments/assets/d3c6c15c-2212-424b-9fdb-c5fc85cf60f1" />

### Dan yang ini saya menggunakan kernel elips (3x3) dengan kernel, iterations=1)

<img width="1200" height="671" alt="image" src="https://github.com/user-attachments/assets/c9261c8f-7a3a-4ac1-9e74-94cfbd1d7ce2" />
