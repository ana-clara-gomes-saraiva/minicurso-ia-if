import streamlit as st

st.set_page_config(page_title="Calculadora de Notas", page_icon="🌸")

# CSS personalizado
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

/* Fundo com padrão suave */
.stApp {
    background-color: #fff0f5;
    background-image: radial-gradient(#ffc0cb 1px, transparent 1px);
    background-size: 20px 20px;
}

/* Título */
.titulo {
    font-family: 'Pacifico', cursive;
    font-size: 42px;
    text-align: center;
    color: #d63384;
}

/* Texto padrão */
.texto {
    font-family: 'Quicksand', sans-serif;
    text-align: center;
    font-size: 18px;
    color: #555;
}

/* Caixa resultado */
.card {
    background-color: #ffb6c1;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 22px;
    font-weight: bold;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# Título estilizado
st.markdown('<div class="titulo">🌸 Calculadora de Notas do IF 🎀</div>', unsafe_allow_html=True)

st.markdown('<div class="texto">Insira suas notas (ex: 7.5)</div>', unsafe_allow_html=True)

# Inputs
n1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
n2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)

# Botão
if st.button("Calcular Média 💖"):
    media = (n1 + n2) / 2

    if media >= 7:
        status = "Aprovado 😄"
    elif media >= 5:
        status = "Recuperação 😐"
    else:
        status = "Reprovado 😢"

    # Resultado estilizado
    st.markdown(f"""
    <div class="card">
        🎀 Média: {media:.2f} <br><br>
        {status}
    </div>
    """, unsafe_allow_html=True)
