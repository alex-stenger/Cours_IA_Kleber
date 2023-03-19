import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from sklearn import datasets
import pandas
from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import *

init_notebook_mode(connected=True)         # initiate notebook for offline plot

import plotly.graph_objects as go
import numpy as np

def show_points(x,y) :
    plt.scatter(x,y, label="individu")
    plt.legend()
    plt.xlabel("ancienneté")
    plt.ylabel("salaire annuel en k€")
    plt.show()
    


def moindre_carre(x,y) :
    E_x = np.mean(x)
    E_y = np.mean(y)

    S1, S2 = 0, 0

    for i in range(len(x)) :
        S1 += (x[i] - E_x)*(y[i] - E_y)
        S2 += (x[i] - E_x)**2

    a = S1/S2
    b = E_y - a*E_x

    print("a =", a, "\nb =", b)

    plt.scatter(x,y, label="individu")
    plt.plot(x, np.asarray(a)*x+b, color='red', label="correlation ancienneté-salaire")
    plt.xlabel("ancienneté")
    plt.ylabel("salaire annuel en k€")
    plt.legend()
    plt.show()

    
def compute_error(a,b,x,y) :
    totalError = 0
    for i in range(0, len(x)):
        totalError += (y[i] - (a * x[i] + b)) ** 2
    return totalError / float(len(x))


def grad_desc_b_fix(x, y, lr, epochs, xlim, ylim) :
    #Initialisation
    a = -20
    b = 0

    n = float(len(x)) 
    Da_list = []
    a_list = []
    err_list = []

    # Performing Gradient Descent 
    for i in range(epochs): 
        Y_pred = np.asarray(a)*x + b  # The current predicted value of Y
        D_a = (2/n) * sum(x * (Y_pred - y))  # Derivative wrt a
        #D_b = (-2/n) * sum(y - Y_pred)  # Derivative wrt b
        a = a - lr * D_a  # Update m
        a_list.append(a)
        Da_list.append(D_a)
        err_list.append(compute_error(a,b,x,y))
        #c = c - L * D_c  # Update c

    print ("coeff a par la descente de gradient :", a)
    print ("coeff b (fixé au début) :", b)
    print("")


    plt.scatter(a_list, err_list)
    plt.title("Valeurs de a, prises chaque itération de la descente de gradient")
    plt.xlabel("Coefficient a")
    plt.ylabel("Fonction d'erreur C(a)")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()

    plt.scatter(x,y, label="individu")
    plt.plot(x, np.asarray(a)*x+b, color='red', label="correlation age-salaire")
    plt.xlabel("ancienneté")
    plt.ylabel("salaire annuel en k€")
    plt.legend()
    plt.show()
    
    
def plot_erreur_2D(x,y) :

    a_visu, b_visu = np.meshgrid(np.arange(-2,8,0.1), np.arange(-10,10,0.1))
    x_tmp = x
    y_tmp = y
    error = compute_error(a_visu, b_visu, x_tmp, y_tmp)


    print(a_visu.shape, b_visu.shape, error.shape)

    fig = go.Figure(data=[go.Surface(x=a_visu, y=b_visu, z=error)])
    fig.update_layout(title='Erreur en fonction des coefficients a et b : C(a,b) (Descente de gradient sur Régression linéaire à 2 paramètres', autosize=False,
                      width=700, height=700,
                      margin=dict(l=65, r=50, b=65, t=90))
    fig.update_layout(
        scene = dict(
            xaxis = dict(nticks=4, range=[-2,8],),
            yaxis = dict(nticks=4, range=[-10,10],),
            zaxis = dict(nticks=4, range=[0,15000],),))
    fig.update_scenes(xaxis_title_text='a',  
                      yaxis_title_text='b',  
                      zaxis_title_text='C(a,b) = erreur')

    fig.show()
    
    
    