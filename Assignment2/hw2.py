import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Logistic Curve")

b0 = st.sidebar.slider("b0", -10, 10, 0)
b1 = st.sidebar.slider("b1", -3.00, 3.00, 1.00)

x = np.linspace(-20, 20, 400)
y = (1 + np.exp(-b0 - b1 * x))**(-1)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True)
st.pyplot(fig)