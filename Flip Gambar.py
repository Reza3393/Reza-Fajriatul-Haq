import numpy as np               # library untuk manipulasi array
import imageio                    # library untuk membaca gambar
import matplotlib.pyplot as plt  # library untuk plotting gambar

img = imageio.imread("zee.jpeg")  # membaca gambar dengan nama "zee.jpeg" menggunakan imageio

img_height = img.shape[0]         # mengambil nilai dimensi tinggi gambar
img_width = img.shape[1]          # mengambil nilai dimensi lebar gambar
img_channel = img.shape[2]        # mengambil nilai dimensi channel gambar (RGB)
img_type = img.dtype              # mengambil tipe data gambar (e.g. uint8, float32)

img_flip_horizontal = np.zeros(img.shape, img_type)   # membuat array kosong dengan dimensi yang sama dengan gambar
                                                      # yang digunakan untuk menyimpan gambar hasil flip horizontal
img_flip_vertical = np.zeros(img.shape, img_type)     # membuat array kosong dengan dimensi yang sama dengan gambar
                                                      # yang digunakan untuk menyimpan gambar hasil flip vertical

for y in range(0, img_height):    # melakukan iterasi pada setiap baris gambar
    for x in range(0, img_width): # melakukan iterasi pada setiap kolom gambar
        for c in range(0, img_channel):    # melakukan iterasi pada setiap channel gambar (R, G, B)
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]  # mengambil nilai piksel gambar asli yang terletak 
                                                                     # pada baris y, kolom img_width-1-x, dan channel c 
                                                                     # untuk disimpan pada array img_flip_horizontal yang 
                                                                     # posisinya sudah dibalik (horizontal)
for y in range(0, img_height):    # melakukan iterasi pada setiap baris gambar
    for x in range(0, img_width): # melakukan iterasi pada setiap kolom gambar
        for c in range(0, img_channel):    # melakukan iterasi pada setiap channel gambar (R, G, B)
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]  # Mengambil nilai piksel gambar asli secara terbalik secara vertikal, lalu menetapkannya pada piksel gambar yang akan dibalik secara vertikal

plt.imshow(img_flip_horizontal)  # Menampilkan gambar yang telah dibalik secara horizontal menggunakan plt.imshow()
plt.title("Flip Horizontal")  # Menambahkan judul "Flip Horizontal" pada plot gambar
plt.show()  # Menampilkan plot gambar secara horizontal

plt.imshow(img_flip_vertical)  # Menampilkan gambar yang telah dibalik secara vertikal menggunakan plt.imshow()
plt.title("Flip Vertical")  # Menambahkan judul "Flip Vertical" pada plot gambar
plt.show()  # Menampilkan plot gambar secara vertikal



    

