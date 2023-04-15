from matplotlib import pyplot as plt
import numpy as np
import imageio

def plot_and_save_still_frame(hole_distance,ball_distance,theta,x_limit,handle):
    # plot and save a frame with the ball rolling on an incline towards a hole
    # INPUT:
    # hole_distance: positive float, distance (m)to the hole relative to the origin
    # ball_distance: positive float, location (m) of ball relative to the origin
    # theta: positive float, slope in degrees of incline
    # x_limit: positive float, limit for plotting 
    
    xs = np.linspace(-1,x_limit+1,int(10*np.ceil(x_limit+2)))
    incline_ys = [np.sin(np.pi*theta/180)*x for x in xs]
    plt.plot(xs,incline_ys,'g','LineWidth',2)
    plt.xlim(-1,x_limit+1)
    plt.ylim(-1,max(incline_ys)+1)