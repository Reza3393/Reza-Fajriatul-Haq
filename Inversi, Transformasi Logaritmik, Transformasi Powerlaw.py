import numpy as np
import imageio
import matplotlib.pyplot as plt

img = imageio.imread("Ronaldo.jpeg")

img_height = img.shape[0]  # Mengambil dimensi tinggi (jumlah baris) citra dan menyimpannya dalam variabel img_height
img_width = img.shape[1]   # Mengambil dimensi lebar (jumlah kolom) citra dan menyimpannya dalam variabel img_width
img_channel = img.shape[2] # Mengambil jumlah channel citra dan menyimpannya dalam variabel img_channel

img_inversi = np.zeros(img.shape, dtype=np.uint8)  # Membuat matriks nol dengan ukuran yang sama dengan citra dan tipe data uint8
def inversi_grayscale(nilai):
    for y in range(0, img_height):  # Loop melalui setiap baris di citra
        for x in range(0, img_width):  # Loop melalui setiap kolom di citra
            red = img[y][x][0]  # Ambil nilai merah pada pixel saat ini
            green = img[y][x][1]  # Ambil nilai hijau pada pixel saat ini
            blue = img[y][x][2]  # Ambil nilai biru pada pixel saat ini
            gray = (int(red) + int(green) + int(blue)) / 3  # Hitung nilai rata-rata dari tiga channel warna
            gray = nilai - gray  # Hitung nilai negatif dari nilai rata-rata
            img_inversi[y][x] = (gray, gray, gray)  # Assign nilai pixel yang baru ke citra inversi

def inversi_rgb(nilai):
    for y in range(0, img_height):  # Loop melalui setiap baris di citra
        for x in range(0, img_width):  # Loop melalui setiap kolom di citra
            red = img[y][x][0]  # Ambil nilai merah pada pixel saat ini
            red = nilai - red  # Hitung nilai negatif dari nilai merah
            green = img[y][x][1]  # Ambil nilai hijau pada pixel saat ini
            green = nilai - green  # Hitung nilai negatif dari nilai hijau
            blue = img[y][x][2]  # Ambil nilai biru pada pixel saat ini
            blue = nilai - blue  # Hitung nilai negatif dari nilai biru
            img_inversi[y][x] = (red, green, blue)  # Assign nilai pixel yang baru ke citra inversi

inversi_grayscale(255)  # Memanggil fungsi inversi_grayscale dengan nilai 255
plt.imshow(img_inversi)  # Menampilkan citra inversi grayscale
plt.title("Inversi Grayscale")  # Menambahkan judul pada plot
plt.show()  # Menampilkan plot

inversi_rgb(255)  # Memanggil fungsi inversi_rgb dengan nilai 255
plt.imshow(img_inversi)  # Menampilkan citra inversi RGB
plt.title("Inversi RGB")  # Menambahkan judul pada plot
plt.show()  # Menampilkan plot

img_log = np.zeros(img.shape, dtype=np.uint8)  # Membuat matriks kosong dengan tipe data unsigned integer 8-bit

def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]  # Memperoleh nilai komponen merah
            green = img[y][x][1]  # Memperoleh nilai komponen hijau
            blue = img[y][x][2]  # Memperoleh nilai komponen biru
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata intensitas RGB sebagai grayscale
            gray = int(c * np.log(gray + 1))  # Melakukan transformasi logaritmik pada grayscale
            if gray > 255:  # Memastikan nilai grayscale tidak melebihi 255
                gray = 255
            if gray < 0:  # Memastikan nilai grayscale tidak kurang dari 0
                gray = 0
            img_log[y][x] = (gray, gray, gray)  # Menyimpan nilai grayscale pada matriks img_log

log(30)  # Memanggil fungsi log dengan konstanta c = 50
plt.imshow(img_log)  # Menampilkan citra logaritmik
plt.title("log")  # Menambahkan judul pada plot
plt.show()  # Menampilkan plot

img_inlog = np.zeros(img.shape, dtype=np.uint8)  # Membuat matriks kosong dengan tipe data unsigned integer 8-bit

def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]  # Memperoleh nilai komponen merah
            green = img[y][x][1]  # Memperoleh nilai komponen hijau
            blue = img[y][x][2]  # Memperoleh nilai komponen biru
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata intensitas RGB sebagai grayscale
            gray = int(c * np.log(255 - gray + 1))  # Melakukan transformasi logaritmik terbalik pada grayscale
            if gray > 255:  # Memastikan nilai grayscale tidak melebihi 255
                gray = 255
            if gray < 0:  # Memastikan nilai grayscale tidak kurang dari 0
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)  # Menyimpan nilai grayscale pada matriks img_inlog

inlog(30)  # Memanggil fungsi inlog dengan konstanta c = 50
plt.imshow(img_inlog)  # Menampilkan citra inversi logaritmik
plt.title("Inversi & Log")  # Menambahkan judul pada plot
plt.show()  # Menampilkan plot

img_nthpower = np.zeros(img.shape, dtype=np.uint8)  # Membuat matriks kosong dengan tipe data unsigned integer 8-bit

def nthpower(c, y):
    thc = c / 100  # Mengkonversi konstanta c menjadi persentase
    thy = y / 100  # Mengkonversi nilai pangkat y menjadi persentase
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]  # Memperoleh nilai komponen merah
            green = img[y][x][1]  # Memperoleh nilai komponen hijau
            blue = img[y][x][2]  # Memperoleh nilai komponen biru
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata intensitas RGB sebagai grayscale
            gray = int(thc * pow(gray, thy))  # Melakukan transformasi pangkat N pada grayscale
            if gray > 255:  # Memastikan nilai grayscale tidak melebihi 255
                gray = 255
            if gray < 0:  # Memastikan nilai grayscale tidak kurang dari 0
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)  # Menyimpan nilai grayscale pada matriks img_nthpower

nthpower(50, 100)  # Memanggil fungsi nthpower dengan konstanta c = 50 dan pangkat y = 100
plt.imshow(img_nthpower)  # Menampilkan citra hasil transformasi pangkat N
plt.title("Nth Power")  # Menambahkan judul pada plot
plt.show()  # Menampilkan plot

img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)  # Membuat matriks kosong dengan tipe data unsigned integer 8-bit

def nthrootpower(c, y):
    thc = c / 100  # Mengkonversi konstanta c menjadi persentase
    thy = y / 100  # Mengkonversi nilai pangkat y menjadi persentase
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]  # Memperoleh nilai komponen merah
            green = img[y][x][1]  # Memperoleh nilai komponen hijau
            blue = img[y][x][2]  # Memperoleh nilai komponen biru
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata intensitas RGB sebagai grayscale
            gray = int(thc * pow(gray, 1./thy))  # Melakukan transformasi akar pangkat N pada grayscale
            if gray > 255:  # Memastikan nilai grayscale tidak melebihi 255
                gray = 255
            if gray < 0:  # Memastikan nilai grayscale tidak kurang dari 0
                gray = 0
            img_nthrootpower[y][x] = (gray, gray, gray)  # Menyimpan nilai grayscale pada matriks img_nthrootpower

nthrootpower(100, 100)  # Memanggil fungsi nthrootpower dengan konstanta c = 50 dan pangkat y = 100
plt.imshow(img_nthrootpower)  # Menampilkan citra hasil transformasi akar pangkat N
plt.title("Nth Root Power")  # Menambahkan judul pada plot
plt.show()  # Menampilkan plot

