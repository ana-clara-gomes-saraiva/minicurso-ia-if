import streamlit as st

st.title("Calculadora de Notas do IF")

st.write("Insira notas (podem ser decimais, ex: 7.5)")

# Inputs aceitando decimais
n1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1, format="%.2f")
n2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1, format="%.2f")

if st.button("Calcular Média"):
    media = (n1 + n2) / 2
    st.write(f"A tua média é: {media:.2f}")
