import math

fungsi_str = input("Masukkan fungsi f(x), contoh: x**3 - x - 2 : ")

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

def secant(x0, x1, tol, max_iter):
    print("\n=== METODE SECANT ===")
    print("Iterasi\t x0\t\t x1\t\t x2\t\t f(x2)")

    for i in range(1, max_iter + 1):
        if f(x1) - f(x0) == 0:
            print("Metode gagal: pembagian nol.")
            return None

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        print(f"{i}\t {x0:.6f}\t {x1:.6f}\t {x2:.6f}\t {f(x2):.6f}")

        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            print("\nAkar ditemukan:", x2)
            return x2

        x0, x1 = x1, x2

    print("Tidak konvergen.")
    return None

x0 = float(input("Masukkan x0: "))
x1 = float(input("Masukkan x1: "))
tol = float(input("Masukkan toleransi error, contoh 0.000001: "))
max_iter = int(input("Masukkan maksimum iterasi: "))

secant(x0, x1, tol, max_iter)
