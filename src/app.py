import streamlit as st
import pandas as pd

def calculadora(altura_cm: float, peso: float) -> float:
    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)

    return imc

def coluna1():

    with col1.form("Calculadora",clear_on_submit=True):

        st.write("Preencha os dados abaixo:")

        altura = st.number_input('Qual a sua altura? (cm)',min_value=0,placeholder='Digite sua altura...',step=1)

        peso = st.number_input('Qual o seu peso? (kg)',min_value=0.0,placeholder='Digite seu peso...',step=0.1)

        idade = st.number_input("Idade",min_value=0, step=1)
        
        enviado = st.form_submit_button("Calcular")
    
        if enviado:
            imc = calculadora(altura,peso)
            st.success(f"Seu IMC é {imc:.2f}")


    col1.divider()

    df_imc = pd.DataFrame({
        'Faixa de IMC':['Abaixo de 18,5','18,5 - 24,9','25 - 29,9','≥ 30'],
        'Classificação':['Abaixo do peso','Peso normal', 'Sobrepeso','Obesidade']
    })

    col1.table(df_imc)

st.set_page_config(layout='wide')

st.title('Calculadora personalizada IMC')

col1,col2 = st.columns(2)

coluna1()


