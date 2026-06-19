    import numpy as np
    from sympy import sympify, lambdify, symbols
    
    def romberg_integration(f, a, b, max_level):
        R = np.zeros((max_level, max_level))
        for i in range(max_level):
            n = 2 ** i
            h = (b - a) / n
    
            total = 0.5 * (f(a) + f(b))
            for k in range(1, n):
                total += f(a + k * h)
            
            R[i, 0] = h * total
            
            for j in range(1, i + 1):
                factor = 4 ** j
                R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (factor - 1)            
        return R
    
    def print_header():
        print("=" * 60)
        print("      PROGRAM INTEGRASI ROMBERG - KOMPUTASI NUMERIK      ")
        print("=" * 60)
        print("Fitur: ")
        print(" - Input fungsi matematika fleksibel (cth: x**2, sin(x), exp(-x))")
        print(" - Menampilkan proses konvergensi matriks segitiga Romberg")
        print("-" * 60)
    
    def main():
        print_header()
        try:
            expr_str = input("Masukkan fungsi f(x)           : ")
            a = float(input("Masukkan batas bawah (a)       : "))
            b = float(input("Masukkan batas atas (b)        : "))
            level = int(input("Masukkan tingkat Romberg (O(h^(2k))): "))
            
            if level <= 0:
                print("\n[Error] Tingkat Romberg harus bilangan bulat positif (>= 1).")
                return
                
            x = symbols('x')
            expr = sympify(expr_str)
            f = lambdify(x, expr, 'numpy')
            
        except Exception as e:
            print(f"\n[Error Input] Terjadi kesalahan pembacaan input: {e}")
            print("Pastikan format fungsi menggunakan sintaks Python (misal: x**2 bukan x^2).")
            return
    
        print("\n[Processing] Menghitung matriks Romberg...")
        R_matrix = romberg_integration(f, a, b, level)
        
        print("\n" + "=" * 25 + " TABEL ROMBERG " + "=" * 25)
        
        header_cols = " ".join([f"  Kolom O(h^{2*j+2})" for j in range(level)])
        print(f"i \\ j | {header_cols}")
        print("-" * (10 + level * 15))
        
        for i in range(level):
            row_str = f"Row {i:d} | "
            for j in range(i + 1):
                row_str += f"{R_matrix[i, j]:14.8f} "
            print(row_str)
            
        print("-" * (10 + level * 15))
        
        best_estimate = R_matrix[level-1, level-1]
        trapezoid_base = R_matrix[level-1, 0]
        
        print(f"\nHasil Integrasi Terbaik (Romberg)  : {best_estimate:.10f}")
        print(f"Hasil Perbandingan (Trapezoid biasa): {trapezoid_base:.10f}")
        print(f"Catatan: Perhatikan bagaimana nilai semakin konvergen ke kanan bawah!")
        print("=" * 60)
    
    if __name__ == "__main__":
        main()
