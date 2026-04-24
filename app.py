import streamlit as st

st.set_page_config(page_title="Calculadora de Notas", page_icon="📊")

st.title("📊 Calculadora de Notas do IF")
st.write("Insira suas notas (ex: 7.5)")

# Inputs
n1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
n2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Calcular Média"):
    media = (n1 + n2) / 2

    # Definir status, cor e emoji
    if media >= 7:
        status = "APROVADO"
        cor = "#4CAF50"  # verde
        emoji = "😄"
    elif media >= 5:
        status = "RECUPERAÇÃO"
        cor = "#FFC107"  # amarelo
        emoji = "😐"
    else:
        status = "REPROVADO"
        cor = "#F44336"  # vermelho
        emoji = "😢"

    # Caixa estilizada
    st.markdown(f"""
    <div style="
        background-color: {cor};
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    ">
        {emoji} <br><br>
        Média: {media:.2f} <br><br>
        {status}
    </div>
    """, unsafe_allow_html=True)
