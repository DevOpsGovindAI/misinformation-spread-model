import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Misinformation Spread Model")

# Inputs
total_users = st.number_input("Total Users", 50, 1000, 100)
initial_believers = st.number_input("Initial Believers", 1, 100, 10)

spread_rate = st.slider("Spread Rate (beta)", 0.1, 1.0, 0.3)
recovery_rate = st.slider("Recovery Rate (gamma)", 0.1, 1.0, 0.1)

time_steps = st.slider("Time", 10, 100, 50)

if st.button("Run Simulation"):

    S = [total_users - initial_believers]
    I = [initial_believers]
    R = [0]

    for i in range(time_steps):
        new_infected = spread_rate * S[-1] * I[-1] / total_users
        new_recovered = recovery_rate * I[-1]

        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)

    st.write("Peak Believers:", int(max(I)))

    fig, ax = plt.subplots()
    ax.plot(S, label="S")
    ax.plot(I, label="I")
    ax.plot(R, label="R")
    ax.legend()

    st.pyplot(fig)