# ODE Homogen Solver

Aplikasi web untuk menyelesaikan Persamaan Diferensial Biasa (ODE) orde satu homogen menggunakan metode substitusi `y = v*x` dan pemisahan variabel. Dibangun dengan [Streamlit](https://streamlit.io) dan [SymPy](https://www.sympy.org).

## Cara menggunakan

1. Masukkan ekspresi `f(x,y)` dari persamaan `dy/dx = f(x,y)`.
2. Pastikan persamaan homogen (program akan memeriksa).
3. Klik tombol **Selesaikan**.
4. Lihat langkah-langkah penyelesaian dan solusi umum.

## Aturan penulisan

- Gunakan `x` dan `y` sebagai variabel.
- Perkalian harus dengan `*`, contoh: `x*y`.
- Pangkat dengan `**`, contoh: `x**2`.
- Fungsi-fungsi yang didukung: `exp`, `sin`, `cos`, `tan`, `log`, `sqrt`, dan lain-lain.

Contoh input valid:
- `(x+y)/(x-y)`
- `(x**2 + y**2)/(x*y)`
- `exp(x/y)`

## Deploy

Aplikasi ini siap di-deploy ke Streamlit Community Cloud, Hugging Face Spaces, atau Render (gratis). Pastikan file `requirements.txt` dan `packages.txt` ikut di-upload.
