import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Misinformation Spread Model (SIR)")

N = st.slider("Total Population", 100, 10000, 1000)
beta = st.slider("Spread Rate (beta)", 0.0, 1.0, 0.3)
gamma = st.slider("Recovery Rate (gamma)", 0.0, 1.0, 0.1)
days = st.slider("Days", 10, 200, 100)

S = [N - 1]
I = [1]
R = [0]

for t in range(days):
    new_S = S[-1] - beta * S[-1] * I[-1] / N
    new_I = I[-1] + beta * S[-1] * I[-1] / N - gamma * I[-1]
    new_R = R[-1] + gamma * I[-1]

    S.append(new_S)
    I.append(new_I)
    R.append(new_R)

plt.figure()
plt.plot(S, label="Skeptics (S)")
plt.plot(I, label="Believers (I)")
plt.plot(R, label="Fact-checkers (R)")
plt.legend()
plt.xlabel("Days")
plt.ylabel("People")

st.pyplot(plt)