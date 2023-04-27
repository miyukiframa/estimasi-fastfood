import pickle
import streamlit as st

model = pickle.load(open('estimasi_fastfood.sav', 'rb'))

st.title('Estimasi Jumlah Kolesterol Menu Makanan Cepat Saji')

calories = st.number_input('Input Jumlah kalori')
total_carb = st.number_input('Input Total Karbohidrat (g)')
sugar = st.number_input('Input Jumlah Gula (g)')
protein = st.number_input('Input Jumlah Protein (g)')
total_fat = st.number_input('Input Total Lemak (g)')

predict = ''

if st.button('Estimasi Kolesterol'):
    predict = model.predict(
        [[calories, total_carb, sugar, protein, total_fat]]
    )
    st.write ('Estimasi Jumlah Kolesterol Fastfood : ', predict)