import streamlit as st

st.set_page_config(page_title="16-Bit ALU Visualizer", layout="wide", page_icon="💻")

st.title("💻 16-Bit ALU Görselleştirici")
st.write("Bu araç, girdilerin ve kontrol bitlerinin ALU içindeki donanım kapılarından geçerken nasıl değiştiğini adım adım gösterir.")

st.markdown("---")

st.sidebar.header("📥 Giriş Değerleri ve Kontrol Bitleri")

x_in = st.sidebar.number_input("X Girdisi (Decimal)", min_value=-32768, max_value=65535, value=10, step=1)
y_in = st.sidebar.number_input("Y Girdisi (Decimal)", min_value=-32768, max_value=65535, value=5, step=1)

MASK = 0xFFFF
x_in &= MASK
y_in &= MASK

st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Kontrol Bitleri")

zx = st.sidebar.checkbox("zx (Zero X)", value=False)
nx = st.sidebar.checkbox("nx (Negate X)", value=False)
zy = st.sidebar.checkbox("zy (Zero Y)", value=False)
ny = st.sidebar.checkbox("ny (Negate Y)", value=False)
f  = st.sidebar.checkbox("f (Function: 1=Add, 0=And)", value=True)
no = st.sidebar.checkbox("no (Negate Out)", value=False)

x_after_zx = 0 if zx else x_in
x_after_nx = (~x_after_zx) & MASK if nx else x_after_zx

y_after_zy = 0 if zy else y_in
y_after_ny = (~y_after_zy) & MASK if ny else y_after_zy

if f:
    f_out = (x_after_nx + y_after_ny) & MASK
    operation_name = f"Toplama (+) İşlemi: {x_after_nx} + {y_after_ny}"
else:
    f_out = (x_after_nx & y_after_ny) & MASK
    operation_name = f"Mantıksal VE (AND) İşlemi: {x_after_nx} & {y_after_ny}"

final_out = (~f_out) & MASK if no else f_out

zr = 1 if final_out == 0 else 0
ng = 1 if (final_out & 0x8000) else 0

def to_signed_dec(val):
    return val if val < 0x8000 else val - 0x10000

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏁 Başlangıç Değerleri")
    st.metric(label="İlk X", value=f"{to_signed_dec(x_in)}", delta=f"{bin(x_in)[2:].zfill(16)} (Binary)")
    st.metric(label="İlk Y", value=f"{to_signed_dec(y_in)}", delta=f"{bin(y_in)[2:].zfill(16)} (Binary)")

with col2:
    st.subheader("🏆 ALU Çıkış Sonuçları")
    st.metric(label="Çıkış (out)", value=f"{to_signed_dec(final_out)}", delta=f"{bin(final_out)[2:].zfill(16)} (Binary)")
    
    f_col1, f_col2 = st.columns(2)
    f_col1.metric(label="zr (Zero Flag)", value=zr)
    f_col2.metric(label="ng (Negative Flag)", value=ng)

st.markdown("---")
st.subheader("🔍 Adım Adım Donanım Kapıları Simülasyonu")

st.info(f"**Aşama 1: X Girdisinin İşlenmesi (Mux16 & Not16)**\n"
        f"* **zx={int(zx)}** -> Mux16 Sonucu: `{bin(x_after_zx)[2:].zfill(16)}` ({x_after_zx})\n"
        f"* **nx={int(nx)}** -> Not16 Sonucu: `{bin(x_after_nx)[2:].zfill(16)}` ({to_signed_dec(x_after_nx)})")

st.info(f"**Aşama 2: Y Girdisinin İşlenmesi (Mux16 & Not16)**\n"
        f"* **zy={int(zy)}** -> Mux16 Sonucu: `{bin(y_after_zy)[2:].zfill(16)}` ({y_after_zy})\n"
        f"* **ny={int(ny)}** -> Not16 Sonucu: `{bin(y_after_ny)[2:].zfill(16)}` ({to_signed_dec(y_after_ny)})")

st.success(f"**Aşama 3: Çekirdek ALU İşlemi (Add16 / And16)**\n"
           f"* **f={int(f)}** -> Seçilen Fonksiyon: **{operation_name}**\n"
           f"* İşlem Sonucu: `{bin(f_out)[2:].zfill(16)}`")

st.warning(f"**Aşama 4: Çıkış Manipülasyonu ve Flag Tespiti (Not16 & Or8Way)**\n"
           f"* **no={int(no)}** -> Son Çıkış (out): `{bin(final_out)[2:].zfill(16)}` ({to_signed_dec(final_out)})\n"
           f"* **zr**: { '1' if zr else '0'} | **ng**: {'1' if ng else '0'}")