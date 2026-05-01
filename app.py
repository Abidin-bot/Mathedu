import streamlit as st
import sympy as sp

st.set_page_config(page_title="ODE Homogen Solver", layout="wide")
st.title("🧮 Penyelesaian ODE Homogen Orde Satu")
st.markdown("Metode substitusi **y = v·x** dan pemisahan variabel")

sp.init_printing(use_unicode=True)

# ---------- Fungsi bantu ----------
def cek_homogen(f, x, y):
    t = sp.symbols('t')
    try:
        ft = f.subs({x: t*x, y: t*y})
        return sp.simplify(ft - f) == 0
    except:
        return False

# ---------- Sidebar aturan ----------
with st.sidebar:
    st.header("📝 Aturan Penulisan")
    st.markdown("""
    - Gunakan `x` dan `y`
    - Perkalian wajib `*` : `x*y`
    - Pangkat `**` : `x**2`
    - Fungsi: `exp(x)`, `sin(x)`, `log(x)`, `sqrt(x)`
    - Contoh: `(x**2 + y**2)/(x*y)`
    """)
    st.latex(r"\frac{dy}{dx} = \frac{x+y}{x-y}")

# ---------- Input ----------
input_str = st.text_input("Masukkan f(x,y) dari dy/dx = f(x,y):",
                           value="(x+y)/(x-y)")

if st.button("🔍 Selesaikan"):
    if not input_str.strip():
        st.error("Masukkan ekspresi!")
        st.stop()

    x, y = sp.symbols('x y')
    try:
        f_expr = sp.sympify(input_str)
    except Exception as e:
        st.error(f"Ekspresi tidak valid: {e}")
        st.stop()

    st.subheader("📌 Persamaan")
    st.latex(r"\frac{dy}{dx} = " + sp.latex(f_expr))

    # Homogenitas
    if not cek_homogen(f_expr, x, y):
        st.error("❌ Bukan ODE homogen. Program berhenti.")
        st.stop()
    st.success("✓ Persamaan HOMOGEN")

    try:
        # Langkah 1
        st.subheader("1️⃣ Substitusi y = v·x")
        v = sp.symbols('v')
        f_v = f_expr.subs(y, v*x)
        st.latex(r"v + x\frac{dv}{dx} = " + sp.latex(f_v))

        # Langkah 2
        st.subheader("2️⃣ Pisahkan variabel")
        pen = sp.simplify(f_v - v)
        if pen == 0:
            st.info("Kasus khusus dy/dx = y/x → solusi y = C·x")
            st.latex(r"\boxed{y = C\,x}")
            st.stop()

        lhs = 1/pen
        rhs = 1/x
        st.latex(r"\frac{1}{" + sp.latex(pen) + r"}\,dv = \frac{1}{x}\,dx")

        # Langkah 3
        st.subheader("3️⃣ Integrasi")
        int_lhs = sp.integrate(lhs, v)
        int_rhs = sp.integrate(rhs, x)
        C = sp.Symbol('C')
        st.latex(sp.latex(int_lhs) + r" = " + sp.latex(int_rhs) + r" + C")

        # Langkah 4
        st.subheader("4️⃣ Substitusi balik v = y/x")
        sol = sp.Eq(int_lhs, int_rhs + C).subs(v, y/x)
        sol = sp.simplify(sol)
        st.latex(sp.latex(sol))

        # Solusi akhir
        st.subheader("✅ Solusi Umum")
        st.latex(sp.latex(sol))

        # Coba eksplisit
        try:
            y_sol = sp.solve(sol, y)
            if y_sol:
                st.write("**Bentuk eksplisit (jika mungkin):**")
                for s in y_sol:
                    st.latex(r"y = " + sp.latex(s))
        except:
            pass

        st.balloons()
    except Exception as e:
        st.error(f"Terjadi error: {e}")
        st.exception(e)
