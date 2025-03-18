import streamlit as st

st.title('Калькулятор каскадных усилителей')
with st.sidebar:
    st.subheader("Введите исходные данные")

    transistor_type = st.text_input("Тип используемого транзистора", "КТ315 №2")
    supply_voltage = st.number_input("Eк (В):", min_value=0)

    st.text("Параметры рабочей точки транзистора")
    col1, col2 = st.columns(2)

    Ik0 = col1.number_input("Ik0 (мА):", min_value=0)
    Ik0_2 = Ik0 * 10 ** (-3)
    if Ik0_2 == 0:
        st.error("Введите значение Ik0 != 0: ")

    Ib0 = col2.number_input("Ib0 (мкА):", min_value=0)
    Ib0_2 = Ib0 * 10 ** (-6)

    source_resistance = st.number_input("Rг (кОм):", min_value=0)
    source_resistance_2 = source_resistance * 10 ** (3)

    load_resistance = st.number_input("Rн (кОм):", min_value=0)
    load_resistance_2 = load_resistance * 10 ** (3)

    load_capacity = st.number_input("Cн (пФ):", min_value=0)
    load_capacity_2 = load_capacity * 10 ** (-12)

    lower_frequency = st.number_input("fн (Гц):", min_value=0)

    current_ratio = st.number_input("IR1/Ib0: ", min_value=0)
    st.markdown("---")

    Ik = st.number_input("Введите изменение тока коллектора (мА):")
    Ik_2 = Ik * 10 ** (-3)
    Uke = st.number_input("Введите изменение напряжения коллектор-эмиттер (В):")
    Ib = st.number_input("Введите изменение тока базы (мкА):")
    Ib_2 = Ib * 10 ** (-6)
    Ube = st.number_input("Введите изменение напряжения база-эмиттер (В):")
    Ube0 = st.number_input("Введите значение Ube0 (В):")

st.markdown("---")

st.header("Y параметры транзистора")

col1, col2 = st.columns(2)
y11 = 0
y12 = 0
y21 = 0
y22 = 0

# Расчет y параметров
if Ube == 0:
    col1.error("Изменение напряжения база-эмиттер не может быть нулевым")
else:
    y11 = Ib_2 / Ube
    col1.success(f"Параметр y11: {y11: ,.3f}")

if Uke == 0:
    col2.error("Изменение напряжения коллектор-эмиттер не может быть нулевым")
else:
    y12 = Ib_2 / Uke
    col2.success(f"Параметр y12: {y12: ,.3f}")

# Расчет параметров y21 и y22
if Ube == 0:
    col1.error("Изменение напряжения база-эмиттер не может быть нулевым")
else:
    y21 = Ik_2 / Ube
    col1.success(f"Параметр y21: {y21: ,.3f}")
    st.success(f"Крутизна S: {y21: ,.3f}")

if Uke == 0:
    col2.error("Изменение напряжения коллектор-эмиттер не может быть нулевым")
else:
    y22 = Ik_2 / Uke
    col2.success(f"Параметр y22: {y22: ,.3f}")
    st.success(f"Параметр g: {y22: ,.3f}")
if y11 != 0 and y12 != 0 and y21 != 0 and y22 != 0:
    Y_matrix_determinant = (y11 * y22) - (y21 * y12)
    st.success(f"Определитель матрицы Y параметров: {Y_matrix_determinant}")
else:
    st.error(f"Для расчета определителя матрицы Y параметров необходимо сначала рассчитать Y параметры. Введите исходные данные для расчета")
st.markdown("---")

# Схема с общим эмиттером
st.header("Расчеты для схемы с общим эмиттером")
col1, col2 = st.columns(2)
col2.image("src/first_sheme.png", caption="Схема с общим эмиттером")
Rem_out = supply_voltage/(2*Ik0_2*9)
Rem = col1.success(f"Rem: {Rem_out:,.3f}")
Rk_out = Rem_out*8
Rk = col1.success(f"Rk: {Rk_out:,.3f}")
Uem_out = Rem_out*Ik0_2
Uem = col1.success(f"Uem: {Uem_out:,.3f}")
U_base_out = Uem_out + Ube0
U_base = col1.success(f"Ub: {U_base_out:,.3f}")
R2_out = (U_base_out/(current_ratio * Ib0_2))
R2 = st.success(f"R2: {R2_out:,.3f}")
R1_out = (supply_voltage/(current_ratio * Ib0_2)) - R2_out
if R1_out >= 0:
    R1 = st. success(f"R1: {R1_out:,.3f}")
else:
    st.error("Проверьте корректность введенных данных")
Y_load_hatch_out = 1 / Rk_out + 1 / load_resistance
Y_load_hatch = st.success(f"Yн: {Y_load_hatch_out: ,.3f}")
Y_gen_hatch_out = 1 / source_resistance + 1 / R1_out + 1 / R2_out
Y_gen_hatch = st.success(f"Yг: {Y_gen_hatch_out: ,.3f}")
Y_input = st.success(f"Yвх: {(Y_matrix_determinant + y11 * Y_load_hatch_out) / (y22 + Y_load_hatch_out): ,.3f}")
Y_output = st.success(f"Yвых: {(Y_matrix_determinant + y22 * Y_gen_hatch_out) / (y11 + Y_gen_hatch_out): ,.3f}")
st.markdown("---")

# Схема с общей базой
st.header("Расчеты для схемы с общей базой")
col1, col2 = st.columns(2)
col2.image("src/second_sheme.png", caption="Схема с общей базой")
st.markdown("---")

# Схема с общим коллектором
st.header("Расчеты для схемы с общим коллектором")
col1, col2 = st.columns(2)
col2.image("src/third_sheme.png", caption="Схема с общим коллектором")
st.markdown("---")
