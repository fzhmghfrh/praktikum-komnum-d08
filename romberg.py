import numpy as np

def f(x):
    return 1 / (1 + x**2)  # Fungsi yang akan diintegrasi

def romberg_integration(f, a, b, max_level=5):
    R = np.zeros((max_level, max_level))
    h = b - a

    # R[0][0] menggunakan aturan trapezoidal dasar
    R[0, 0] = (h / 2) * (f(a) + f(b))

    for i in range(1, max_level):
        h /= 2

        # Hitung jumlah titik tengah baru
        sum_middle = sum(f(a + (2*k - 1)*h) for k in range(1, 2**(i-1) + 1))
        R[i, 0] = 0.5 * R[i-1, 0] + h * sum_middle

        # Ekstrapolasi Richardson
        for j in range(1, i + 1):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    return R

# Pengujian
a = 0
b = 1
romberg_result = romberg_integration(f, a, b, max_level=5)

# Tampilkan hasil
print("Tabel Romberg Integration:")
for i in range(5):
    print("Level", i, ":", romberg_result[i, :i+1])

print("\nHasil mendekati pi/4:", romberg_result[4, 4])
print("Nilai pi/4 yang sesungguhnya:", np.pi / 4)
