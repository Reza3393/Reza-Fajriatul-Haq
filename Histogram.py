import numpy as np                                    # Mengimport library NumPy sebagai np
import imageio                                         # Mengimport library imageio
import matplotlib.pyplot as plt                       # Mengimport library matplotlib sebagai plt

img = imageio.imread("zee.jpeg")                        # Membaca gambar 'zee.jpeg' menggunakan imageio dan menyimpan hasilnya pada variable img
plt.imshow(img)                                        # Menampilkan gambar menggunakan imshow() dari matplotlib
plt.axis('off')                                        # Menghilangkan sumbu x dan y pada gambar
plt.show()                                             # Menampilkan gambar

img_height = img.shape[0]                              # Mengambil ukuran tinggi gambar dari img dan menyimpannya pada img_height
img_width = img.shape[1]                               # Mengambil ukuran lebar gambar dari img dan menyimpannya pada img_width
img_channel = img.shape[2]                             # Mengambil jumlah channel gambar dari img dan menyimpannya pada img_channel

img_grayscale = np.zeros(img.shape, dtype=np.uint8)     # Menginisialisasi img_grayscale dengan array nol dengan bentuk yang sama dengan img, dan tipe data uint8 (0-255)

for y in range(0, img_height):                          # Melakukan perulangan untuk setiap nilai y dari 0 hingga img_height
    for x in range(0, img_width):                       # Melakukan perulangan untuk setiap nilai x dari 0 hingga img_width
        red = img[y][x][0]                              # Mengambil nilai warna merah (red) pada koordinat (y, x)
        green = img[y][x][1]                            # Mengambil nilai warna hijau (green) pada koordinat (y, x)
        blue = img[y][x][2]                             # Mengambil nilai warna biru (blue) pada koordinat (y, x)
        gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata nilai dari red, green, dan blue untuk mendapatkan warna grayscale
        img_grayscale[y][x] = (gray, gray, gray)        # Menetapkan nilai grayscale tersebut ke img_grayscale pada koordinat (y, x)

plt.imshow(img_grayscale)                               # Menampilkan gambar grayscale yang telah dihasilkan sebelumnya menggunakan imshow() dari matplotlib
plt.title("Grayscale")                                  # Menambahkan judul pada gambar
plt.show()                                               # Menampilkan gambar

hg = np.zeros((256))                                    # Membuat array nol sebanyak 256 elemen dan menyimpannya pada variable hg

for x in range(0, 256):                                 # Melakukan perulangan untuk setiap nilai x dari 0 hingga 256
    hg[x] = 0                                           # Menetapkan nilai 0 pada indeks ke-x pada array hg

for y in range(0, img_height):                          # Melakukan perulangan untuk setiap nilai y dari 0 hingga img_height
    for x in range(0, img_width):                       # Melakukan perulangan untuk setiap nilai x dari 0 hingga img_width
        gray = img_grayscale[y][x][0]                   # Mengambil nilai grayscale pada koordinat (y, x)
        hg[gray] += 1                                    # Menambahkan nilai 1 pada indeks ke-gray pada array hg

# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100)                         # Membuat array yang berisi 100 nilai yang sama berjarak dari 0

bins = np.linspace(0, 256, 100)  # membuat bins untuk histogram
plt.hist(hg, bins, color="black", alpha=0.5)  # membuat histogram dengan matplotlib
plt.title("Histogram")  # memberikan judul pada histogram
plt.show()  # menampilkan histogram

hgr = np.zeros((256))  # membuat array kosong dengan ukuran 256 untuk histogram warna merah
hgg = np.zeros((256))  # membuat array kosong dengan ukuran 256 untuk histogram warna hijau
hgb = np.zeros((256))  # membuat array kosong dengan ukuran 256 untuk histogram warna biru
hgrgb = np.zeros((768))  # membuat array kosong dengan ukuran 768 untuk histogram gabungan warna RGB

for x in range(0, 256):  # mengisi array kosong dengan nilai 0
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):  # mengisi array kosong dengan nilai 0
    hgrgb[x] = 0

for y in range(0, img.shape[0]):  # loop untuk setiap pixel pada gambar
    for x in range(0, img.shape[1]):
        red = int(img[y][x][0])  # mengambil nilai R dari pixel tersebut
        green = int(img[y][x][1])  # mengambil nilai G dari pixel tersebut
        blue = int(img[y][x][2])  # mengambil nilai B dari pixel tersebut
        green = green + 256  # menambahkan 256 ke nilai G
        blue = blue + 512  # menambahkan 512 ke nilai B
        hgrgb[red] += 1  # menambahkan 1 ke histogram merah
        hgrgb[green] += 1  # menambahkan 1 ke histogram hijau
        hgrgb[blue] += 1  # menambahkan 1 ke histogram biru

binsrgb = np.linspace(0, 768, 100)  # membuat bins untuk histogram RGB
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)  # membuat histogram RGB dengan matplotlib
plt.title("Histogram Red Green Blue")  # memberikan judul pada histogram
plt.show()  # menampilkan histogram

for y in range(0, img_height):  # loop untuk setiap pixel pada gambar grayscale
    for x in range(0, img_width):
        red = img[y][x][0]  # mengambil nilai R dari pixel tersebut
        green = img[y][x][1]  # mengambil nilai G dari pixel tersebut
        blue = img[y][x][2]  # mengambil nilai B dari pixel tersebut
        hgr[red] += 1  # menambahkan 1 ke histogram merah
        hgg[green] += 1 # menambahkan 1 ke histogram hijau
        hgb[blue] += 1 # menambahkan 1 ke histogram biru

bins = np.linspace(0, 256, 100) # membuat bins untuk histogram
plt.hist(hgr, bins, color="red", alpha=0.5) # membuat histogram merah dengan matplotlib
plt.title("Histogram Red") # memberikan judul pada histogram
plt.show() # menampilkan histogram

plt.hist(hgg, bins, color="green", alpha=0.5) # membuat histogram hijau dengan matplotlib
plt.title("Histogram Green") # memberikan judul pada histogram
plt.show() # menampilkan histogram

plt.hist(hgb, bins, color="blue", alpha=0.5) # membuat histogram biru dengan matplotlib
plt.title("Histogram Blue") # memberikan judul pada histogram
plt.show() # menampilkan histogram

hgk = np.zeros((256)) # membuat array kosong dengan ukuran 256 untuk histogram grayscale
c = np.zeros((256)) # membuat array kosong dengan ukuran 256 untuk kumulatif histogram

for x in range(0, 256): # mengisi array kosong dengan nilai 0
      hgk[x] = 0
c[x] = 0

for y in range(0, img_height): # loop untuk setiap pixel pada gambar grayscale
    for x in range(0, img_width):
      gray = img_grayscale[y][x][0] # mengambil nilai grayscale dari pixel tersebut
hgk[gray] += 1 # menambahkan 1 ke histogram grayscale
                
c[0] = hgk[0] # inisialisasi nilai awal untuk kumulatif histogram
for x in range(1, 256): # menghitung kumulatif histogram
     c[x] = c[x-1] + hgk[x]

hmaxk = c[255] # nilai maksimum kumulatif histogram

for x in range(0, 256): # normalisasi nilai kumulatif histogram
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5) # membuat histogram kumulatif grayscale dengan matplotlib
plt.title("Histogram Grayscale Kumulatif") # memberikan judul pada histogram
plt.show() # menampilkan histogram

hgh = np.zeros((256)) # membuat array kosong dengan ukuran 256 untuk histogram hasil equalisasi
h = np.zeros((256)) # membuat array kosong dengan ukuran 256 untuk distribusi probabilitas
c = np.zeros((256)) # membuat array kosong dengan ukuran 256 untuk kumulatif histogram

for x in range(0, 256): # mengisi array kosong dengan nilai 0
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

for y in range(0, img_height): # loop untuk setiap pixel pada gambar grayscale
      for x in range(0, img_width):
          gray = img_grayscale[y][x][0] # mengambil nilai grayscale dari pixel tersebut
          hgh[gray] += 1 # menambahkan 1 ke histogram grayscale
                
h[0] = hgh[0] # inisialisasi nilai awal untuk distribusi probabilit
# Menghitung kumulatif histogram
for x in range(1, 256):
    h[x] = h[x-1] + hgh[x]

# Normalisasi histogram
for x in range(0, 256):
    h[x] = h[x] / img_height / img_width

# Mengatur ulang nilai histogram grayscale
for x in range(0, 256):
    hgh[x] = 0

# Menghitung histogram setelah ekualisasi
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

# Menghitung kumulatif histogram setelah ekualisasi
c[0] = hgh[0]
for x in range(1, 256):
    c[x] = c[x-1] + hgh[x]

# Normalisasi kumulatif histogram
hmaxk = c[255]
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

# Menampilkan histogram hasil ekualisasi
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")
plt.show()



        




