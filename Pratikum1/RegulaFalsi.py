import numpy as np
import matplotlib.pyplot as plt
import math

fungsi_str = input("Masukkan fungsi f(x), contoh: exp(-x) - x : ")

def f(x):
    return eval(fungsi_str, {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "abs": abs
    })

def regula_falsi(xl, xu, tol, max_iter):
    print("\n=== METODE REGULA FALSI ===")

    if f(xl) * f(xu) > 0:
        print("Interval tidak valid. f(xl) dan f(xu) harus beda tanda.")
        return None

    print("Iterasi\t xl\t\t xu\t\t xr\t\t f(xr)")
    xr_old = xl

    for i in range(1, max_iter + 1):
        xr = (xu * f(xl) - xl * f(xu)) / (f(xl) - f(xu))

        print(f"{i}\t {xl:.6f}\t {xu:.6f}\t {xr:.6f}\t {f(xr):.6f}")

        if abs(xr - xr_old) < tol or abs(f(xr)) < tol:
            print("\nAkar ditemukan:", xr)
            return xr

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        xr_old = xr

    print("Tidak konvergen.")
    return None

def tampilkan_grafik(root, a, b):
    x = np.linspace(a - 2, b + 2, 400)
    y = [f(i) for i in x]

    plt.axhline(0)
    plt.axvline(0)
    plt.plot(x, y, label="f(x)")

    if root is not None:
        plt.scatter(root, f(root), label=f"Akar = {root:.6f}")

    plt.title("Grafik Fungsi Regula Falsi")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.legend()
    plt.show()

xl = float(input("Masukkan batas bawah xl: "))
xu = float(input("Masukkan batas atas xu: "))
tol = float(input("Masukkan toleransi error, contoh 0.000001: "))
max_iter = int(input("Masukkan maksimum iterasi: "))

root = regula_falsi(xl, xu, tol, max_iter)
tampilkan_grafik(root, xl, xu)
