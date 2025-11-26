import streamlit as st

st.header('Jogando uma moeda')

# Controle deslizante: número de tentativas
number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)

# Botão para iniciar
start_button = st.button('Executar')

# Quando o botão é clicado
if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')

st.write('Ainda não é um aplicativo funcional. Em construção.')
