
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np

def plotInterception(x, f, g):
    """ first we find the values of each function in each of the points on the x axies, then we try to solve  
    """
    x_vals = list(x);cross_y= []
    lst_f = [f(i) for i in x_vals ]
    lst_g = [g(i) for i in x_vals ]
    [cross_y.append(round(x,3)) for x in [fsolve(lambda x : f(x) - g(x),x)[0] for x in x_vals] if round(x,3) not in cross_y]
    fig = plt.figure()

    #ploting
    plt.plot(x_vals,lst_f,'g')
    plt.plot(x_vals,lst_g,'b')
    for x in cross_y:
        if round(f(round(x,3)),3) == round(g(round(x,3)),3):
            plt.plot(x,round(f(x),3),"ro")
    plt.show()

if __name__ == "__main__":
    plotInterception(np.linspace(-10,10,1000), lambda x: np.sin(x), lambda x: 0.2*x)