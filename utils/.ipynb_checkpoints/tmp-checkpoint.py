from matplotlib import cm

a_test = np.arange(-10,10,1)
b_test = np.arange(-100,100,1)

a_visu, b_visu = np.meshgrid(a_test, b_test)

a_visu = a_visu.flatten()
b_visu = b_visu.flatten()

def test(a, b, nb_points) :
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(15, 5))
    
    x_tmp = x[:nb_points]
    y_tmp = y[:nb_points]
    line_list = np.asarray(a)*x_tmp + b
    
    axes.scatter(x_tmp,y_tmp, label="individu")
    axes.plot(x_tmp, np.asarray(a)*x_tmp+b, color='red', label="correlation age-salaire")
    
    axes.vlines(x_tmp, ymin=y_tmp, ymax=line_list, linestyles="dashed", colors="orange", label="distance à la droite")
    axes.set_xlabel("âge")
    axes.set_ylabel("salaire annuel en k€")
    axes.set_xlim([-5,50])
    axes.set_ylim([-5,140])
    axes.legend()
    
    plt.show()
    
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    
    ax.scatter(a, b,compute_error(a,b,x_tmp,y_tmp), marker="+", color ="green", s=1000)
    surf = ax.plot_trisurf(a_visu, b_visu,compute_error(a_visu, b_visu, x_tmp, y_tmp), 
                         cmap=cm.coolwarm,
                         linewidth=0, 
                         antialiased=False)
    
    #axes[1].set_xlabel("coefficeint a")
    #axes[1].set_ylabel("fonction d'erreur")
    #axes[1].set_xlim([0.8,2.6])
    #axes[1].set_ylim([50,1200])

    plt.show()
    
    print(compute_error(a,b,x_tmp,y_tmp))
    
interact(test, a=(-8,8,0.01), b=(-30,30,1), nb_points=(10,100));



import plotly.graph_objects as go
import numpy as np
  
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
  
# transpose
y = x.copy().T
z = np.cos(x ** 2 + y ** 2)


print(x.shape, y.shape, z.shape)
  
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))
  
fig.show()

import plotly.graph_objects as go
import pandas as pd
import numpy as np
# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
z = z_data.values

print(z.shape)

sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))
fig.show()