import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import scipy.optimize as op
#plt.rcParams['figure.figsize'] = (5, 3)
st.set_page_config(page_title="Lab 9 graph",  page_icon="🧊") #, layout="wide"
def linear(x, a, b):
    return a * x + b

def fit_with_curve_fit(x, y):
    popt, err = op.curve_fit(linear, x, y)
    #print("Parameters:", popt)
    #print("Errors:    ", np.sqrt(pconv.diagonal()))
    return popt, np.sqrt(err.diagonal())

#x = st.slider('x') 
#st.write(x, 'squared is', x * x)
x=[None]*5
y=[None]*5
#def capture_x_0(x_0):
#   x[0]=x_0
   #return True
#def capture_y_0():
#   y[0]=y_0
#   #return True
st.write("Введите 5 значений углового ускорения в рад/(с$^{2}$)")
row1 = st.columns(5)
#row1.subheader("X")
for i, col in enumerate(row1):
#on_change=capture_x_0,
    inp_key="x_"+str(i)
    x[i]=col.number_input("", key=inp_key)
st.write("Введите 5 значений момента силы в 10$^{-3}$ Н*м")
row2 = st.columns(5)
for i, col in enumerate(row2):
    inp_key="y_"+str(i)
    y[i]=col.number_input("", key=inp_key)

placeholder = st.empty()
X=np.array(x)
Y=np.array(y)
#st.write(X,Y)
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(X[(X!=0) & (Y!=0)],Y[(X!=0) & (Y!=0)])
ax.set_xlabel("$\epsilon$, А/(м$^{2}$)")
ax.set_ylabel("B, м")
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.tick_params(axis='both',which='both', direction="in", labelsize=10)
ax.xaxis.set_minor_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
placeholder.pyplot(fig)
if (st.button("Аппроксимировать прямой")):
    if (len(X[(X!=0) & (Y!=0)])>2):
        popt, perr=fit_with_curve_fit(X[(X!=0) & (Y!=0)],Y[(X!=0) & (Y!=0)])
        st.write("Результаты обработки с помощью МНК:")
        st.write("I$_{0}$= "+ str(np.round(popt[0],3))+" * 10$^{-3}$ кг*м$^{2}$,") 
        st.write("M$_{тр}$= "+ str(np.round(popt[1],3))+" * 10$^{-3}$ Н*м,")    
        st.write("$\epsilon_{I0}$= "+ str(np.round(perr[0],3))+" * 10$^{-3}$ кг*м$^{2}$")
        st.write("$\epsilon_{Mтр}$= "+ str(np.round(perr[1],3))+" * 10$^{-3}$ Н*м")
        X2=np.linspace(0,max(X),5)
        ax.plot(X2,X2*popt[0]+popt[1], linestyle = '--', color="black")
        placeholder.pyplot(fig)
        st.write("Не забудьте округлить значения величин и их погрешности в соответствии с правилами округления!")
    else:
        st.write("Введите не менее трех значений!")
