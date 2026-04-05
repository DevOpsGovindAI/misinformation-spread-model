import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Misinformation Simulator", layout="wide")

st.title("📊 Misinformation Spread Simulator")
st.write("This model simulates fake news spread using SIR Model")

# ---------- SIDEBAR ----------
st.sidebar.header("⚙️ Simulation Settings")

N = st.sidebar.slider("Total Users", 50, 500, 100)
initial_I = st.sidebar.slider("Initial Believers", 1, 50, 10)
beta = st.sidebar.slider("Spread Rate (β)", 0.1, 1.0, 0.3)
gamma = st.sidebar.slider("Recovery Rate (γ)", 0.1, 1.0, 0.1)
time_steps = st.sidebar.slider("Time Steps", 10, 100, 50)

# ---------- BUTTON ----------
run = st.sidebar.button("🚀 Run Simulation")

# ---------- MODEL ----------
if run:

    S = [N - initial_I]
    I = [initial_I]
    R = [0]

    data = []

    for t in range(time_steps):
        new_infected = beta * S[-1] * I[-1] / N
        new_recovered = gamma * I[-1]

        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)

        data.append([t, S[-1], I[-1], R[-1]])

    # ---------- DATA TABLE ----------
    st.subheader("📋 Simulation Data")

    df = pd.DataFrame(data, columns=[
        "Time", "Skeptics (S)", "Believers (I)", "Fact-checkers (R)"
    ])

    st.dataframe(df, use_container_width=True)

    # ---------- GRAPH ----------
    st.subheader("📈 Graph Output")

    fig, ax = plt.subplots()
    ax.plot(S, label="Skeptics")
    ax.plot(I, label="Believers")
    ax.plot(R, label="Fact-checkers")
    ax.set_xlabel("Time")
    ax.set_ylabel("Users")
    ax.legend()

    st.pyplot(fig)

    # ---------- PERFORMANCE METRICS ----------
    st.subheader("📊 Performance Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Peak Believers", int(max(I)))
    col2.metric("Final Fact-checkers", int(R[-1]))
    col3.metric("Remaining Skeptics", int(S[-1]))

    # ---------- INSIGHTS ----------
    st.subheader("🧠 Insights")

    if max(I) > N * 0.6:
        st.error("⚠️ High misinformation spread detected!")
    else:
        st.success("✅ Spread is under control")

    if gamma > beta:
        st.info("Fact-checking is strong")
    else:
        st.warning("Fake news spreading faster than correction")