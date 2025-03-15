import streamlit as st

st.title('Калькулятор каскадных усилителей')
with st.sidebar:
    st.subheader("Введите исходные данные")
    Ik = st.number_input("Введите изменение тока коллектора")
    Uke = st.number_input("Введите изменение напряжения коллектор-эмиттер")
    Ib = st.number_input("Введите изменение тока базы")
    Ube = st.number_input("Введите изменение напряжения база-эмиттер")

st.markdown("---")

st.header("Y параметры транзистора")

col1, col2 = st.columns(2)

# Расчет параметров y11 и y12
if Ube == 0:
    col1.error("Изменение напряжения база-эмиттер не может быть нулевым")
else:
    y11 = Ib/Ube
    col1.success(f"Параметр y11: {y11: ,.3f}")

if Uke == 0:
    col2.error("Изменение напряжения коллектор-эмиттер не может быть нулевым")
else:
    y12 = Ib/Uke
    col2.success(f"Параметр y12: {y12: ,.3f}")

# Расчет параметров y21 и y22
if Ube == 0:
    col1.error("Изменение напряжения база-эмиттер не может быть нулевым")
else:
    y21 = Ik/Ube
    col1.success(f"Параметр y21: {y21: ,.3f}")
    st.success(f"Крутизна S: {y21: ,.3f}")

if Uke == 0:
    col2.error("Изменение напряжения коллектор-эмиттер не может быть нулевым")
else:
    y22 = Ik/Uke
    col2.success(f"Параметр y22: {y22: ,.3f}")
    st.success(f"Параметр g: {y22: ,.3f}")

st.markdown("---")

col1, col2, col3 = st.columns(3)

st.header("Расчеты для схемы с общим эмиттером")
st.image("src/first_sheme.png", caption="Схема с общим эмиттером")

st.header("Расчеты для схемы с общей базой")
st.image("src/second_sheme.png", caption="Схема с общей базой")

st.header("Расчеты для схемы с общим коллектором")
st.image("src/third_sheme.png", caption="Схема с общим коллектором")