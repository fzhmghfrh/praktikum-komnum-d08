import matplotlib.pyplot as plt
import numpy as np

# Input fungsi dari user
fungsi_input = input("Masukkan fungsi f(x), gunakan 'x' sebagai variabel (contoh: x**3 - x - 2): ")
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
tol = float(input("Masukkan toleransi error (misal: 1e-5): "))

# Membuat fungsi f(x) dari input string
def f(x):
    return eval(fungsi_input)

# Implementasi metode Regula Falsi
def regula_falsi(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Metode gagal: f(a) dan f(b) harus berlainan tanda.")
        return None

    print(f"{'Iter':<5}{'a':<10}{'b':<10}{'x':<10}{'f(x)':<15}{'Error':<10}")
    print("-" * 60)

    for i in range(1, max_iter+1):
        x = b - (f(b) * (a - b)) / (f(a) - f(b))
        fx = f(x)
        error = abs(fx)

        print(f"{i:<5}{a:<10.5f}{b:<10.5f}{x:<10.5f}{fx:<15.8f}{error:<10.5f}")

        if error < tol:
            print("\nAkar ditemukan:", x)
            return x

        if f(a) * fx < 0:
            b = x
        else:
            a = x

    print("\nTidak konvergen dalam iterasi maksimum.")
    return None

# Jalankan metode
akar = regula_falsi(a, b, tol)

# Plot fungsi dan akar
x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
if akar is not None:
    plt.plot(akar, f(akar), 'ro', label=f'Akar aproksimasi ≈ {akar:.5f}')
plt.title('Metode Regula Falsi')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
