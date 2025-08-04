# for feet bmi = weight / (((height/3.28))**2)
# bmi < 16: Extremely Underweight  --> Error
# 16 <= bmi < 18.5: Underweight  --> Warning
# 18.5 <= bmi < 25: Healthy  --> Success
# 25 <= bmi < 30: Overweight --> Info
# bmi >= 30: Extremely Overweight --> Error

import streamlit as st

st.title('BMI Calculator')

weight = st.number_input('Enter the weight of the person in kilogram')
height = st.number_input('Enter the height of the person in meter')
if st.button("Calculate BMI"):
    bmi = weight/(height**2)
    st.write(f"Your BMI is: **{bmi:.2f}**")

    if bmi < 16:
        st.error("Extremely Underweight 😟")
    elif 16 <= bmi < 18.5:
        st.warning("Underweight 🙁")
    elif 18.5 <= bmi < 25:
        st.success("Healthy 🙂")
    elif 25 <= bmi < 30:
        st.info("Overweight 😐")
    else:
        st.error("Extremely Overweight 😟")