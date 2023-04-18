from matplotlib import pyplot as plt
import matplotlib.patches as patches
import numpy as np
import imageio
import putting
import os

def stillframe_short_active(hole_distance,ball_distance,theta,x_limit):
    # plot and save a frame with the ball rolling on an incline towards a hole
    # INPUT:
    # hole_distance: positive float, distance (m)to the hole relative to the origin
    # ball_distance: positive float, location (m) of ball relative to the origin
    # theta: positive float, slope in degrees of incline
    # x_limit: positive float, plotting bound
    
    xs = np.linspace(-1,x_limit,int(10*np.ceil(x_limit)))
    incline_ys = [np.sin(np.pi*theta/180)*x for x in xs]
    last_y=incline_ys[-1]
    #draw incline
    plt.plot(xs,incline_ys,'g',linewidth=2)
    plt.xlim(-1,x_limit)
    plt.ylim(-1,max(1,1+last_y))
    #plt ball and flagpole
    ax = plt.gca()
    ax.add_patch(patches.Circle((ball_distance,np.sin(np.pi*theta/180)*ball_distance+0.06),0.06,facecolor='grey'))
    ax.add_patch(patches.Rectangle((hole_distance+0.05, np.sin(np.pi*theta/180)*hole_distance),0.05,1,facecolor='grey'))
    #flag indices
    corners = np.array([[hole_distance+0.05,1+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.05,0.8+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.45,0.9+np.sin(np.pi*theta/180)*hole_distance]])
    ax.add_patch(patches.Polygon(corners,facecolor='red'))       
    #color sky and ground
    plt.fill_between(xs,incline_ys,max(1,1+last_y) , color='blue', alpha=0.2)
    plt.fill_between(xs,incline_ys,-1 , color='green', alpha=1)
    #hide axis labels
    plt.yticks([]) 
    plt.xticks([])

    
def stillframe_short_missed(hole_distance,ball_distance,theta,x_limit):
    # plot and save a frame with the ball short of hole and MISSED label
    # INPUT:
    # hole_distance: positive float, distance (m)to the hole relative to the origin
    # ball_distance: positive float, location (m) of ball relative to the origin
    # theta: positive float, slope in degrees of incline
    # x_limit: positive float, plotting bound
    
    xs = np.linspace(-1,x_limit,int(10*np.ceil(x_limit)))
    incline_ys = [np.sin(np.pi*theta/180)*x for x in xs]
    last_y=incline_ys[-1]
    #draw incline
    plt.plot(xs,incline_ys,'g',linewidth=2)
    plt.xlim(-1,x_limit)
    plt.ylim(-1,max(1,1+last_y))
    #plt ball and flagpole
    ax = plt.gca()
    ax.add_patch(patches.Circle((ball_distance,np.sin(np.pi*theta/180)*ball_distance+0.06),0.06,facecolor='grey'))
    ax.add_patch(patches.Rectangle((hole_distance+0.05, np.sin(np.pi*theta/180)*hole_distance),0.05,1,facecolor='grey'))
    #flag indices
    corners = np.array([[hole_distance+0.05,1+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.05,0.8+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.45,0.9+np.sin(np.pi*theta/180)*hole_distance]])
    ax.add_patch(patches.Polygon(corners,facecolor='red'))       
    #color sky and ground
    plt.fill_between(xs,incline_ys,max(1,1+last_y) , color='blue', alpha=0.2)
    plt.fill_between(xs,incline_ys,-1 , color='green', alpha=1)
    #hide axis labels
    plt.yticks([]) 
    plt.xticks([])
    #Add "MISSED" Label
    if theta>0:
        plt.text(0.5,1,'MISSED',fontsize=20,color='red')
    else:
        plt.text(0.5,0.8,'MISSED',fontsize=20,color='red')
        
def stillframe_long(hole_distance,ball_distance,theta,x_limit):
    # plot and save a frame with the ball rolling on an incline past the hole
    # INPUT:
    # hole_distance: positive float, distance (m)to the hole relative to the origin
    # ball_distance: positive float, location (m) of ball relative to the origin
    # theta: positive float, slope in degrees of incline
    # x_limit: positive float, plotting bound
    
    xs = np.linspace(-1,x_limit,int(10*np.ceil(x_limit)))
    incline_ys = [np.sin(np.pi*theta/180)*x for x in xs]
    last_y=incline_ys[-1]
    #draw incline
    plt.plot(xs,incline_ys,'g',linewidth=2)
    plt.xlim(-1,x_limit)
    plt.ylim(-1,max(1,1+last_y))
    #plt ball and flagpole
    ax = plt.gca()
    ax.add_patch(patches.Circle((ball_distance,np.sin(np.pi*theta/180)*ball_distance+0.06),0.06,facecolor='grey'))
    ax.add_patch(patches.Rectangle((hole_distance+0.05, np.sin(np.pi*theta/180)*hole_distance),0.05,1,facecolor='grey'))
    #flag indices
    corners = np.array([[hole_distance+0.05,1+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.05,0.8+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.45,0.9+np.sin(np.pi*theta/180)*hole_distance]])
    ax.add_patch(patches.Polygon(corners,facecolor='red'))       
    #color sky and ground
    plt.fill_between(xs,incline_ys,max(1,1+last_y) , color='blue', alpha=0.2)
    plt.fill_between(xs,incline_ys,-1 , color='green', alpha=1)
    #hide axis labels
    plt.yticks([]) 
    plt.xticks([])
    
    #Add "MISSED" Label
    if theta>0:
        plt.text(0.5,1,'MISSED',fontsize=20,color='red')
    else:
        plt.text(0.5,0.8,'MISSED',fontsize=20,color='red')


   
def stillframe_made_putt(hole_distance,theta,x_limit):
    # plot and save a frame with the ball rolling on an incline past the hole
    # INPUT:
    # hole_distance: positive float, distance (m)to the hole relative to the origin
    # ball_distance: positive float, location (m) of ball relative to the origin
    # theta: positive float, slope in degrees of incline
    # x_limit: positive float, plotting bound
    
    xs = np.linspace(-1,x_limit,int(10*np.ceil(x_limit)))
    incline_ys = [np.sin(np.pi*theta/180)*x for x in xs]
    last_y=incline_ys[-1]
    #draw incline
    plt.plot(xs,incline_ys,'g',linewidth=2)
    plt.xlim(-1,x_limit)
    plt.ylim(-1,max(1,1+last_y))
    #plt ball and flagpole
    ax = plt.gca()
    ax.add_patch(patches.Rectangle((hole_distance+0.05, np.sin(np.pi*theta/180)*hole_distance),0.05,1,facecolor='grey'))
    #flag indices
    corners = np.array([[hole_distance+0.05,1+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.05,0.8+np.sin(np.pi*theta/180)*hole_distance],[hole_distance+0.45,0.9+np.sin(np.pi*theta/180)*hole_distance]])
    ax.add_patch(patches.Polygon(corners,facecolor='red'))       
    #color sky and ground
    plt.fill_between(xs,incline_ys,max(1,1+last_y) , color='blue', alpha=0.2)
    plt.fill_between(xs,incline_ys,-1 , color='green', alpha=1)
    #hide axis labels
    plt.yticks([]) 
    plt.xticks([])
    
    #Add "MADE" Label
    if theta>0:
        plt.text(0.5,1,'MADE',fontsize=20,color='green')
    else:
        plt.text(0.5,0.8,'MADE',fontsize=20,color='green')
    
def make_gif(hole_distance,v0,theta,handle):
    # plot and save a frame with the ball rolling on an incline towards a hole
    # INPUT:
    # hole_distance: positive float, distance (m)to the hole relative to the origin
    # theta: positive float, slope in degrees of incline
    # v0: positive float, initial ball speed
    # handle: save location rel current directory
    max_d = max(putting.compute_final_distance(v0,theta),hole_distance) #for plotting limits
    rest_t = putting.compute_time_to_rest(v0,theta)
    max_t=rest_t+2 #2 seconds stationary at end
    num_frames = int(10*np.ceil(max_t))
    t = np.linspace(-1,max_t,num_frames) #draw plot every 10ms
    for i in range(num_frames):
        #create and save each frame
        save_handle = handle+str(i)+".png"
        pos=putting.compute_cur_pos(v0,theta,max(t[i],0))
        #if ball is moving and left of hole, no label
        plt.figure(figsize=(9,6),dpi=100)
        if pos<hole_distance:
            if t[i]<rest_t:
                #ball is left of hole, still rolling
                stillframe_short_active(hole_distance,pos,theta,max_d+1)
            else: 
                #ball is left of hole, at rest, MISSED
                stillframe_short_missed(hole_distance,pos,theta,max_d+1)
        else:
            #ball made it to hole
            make = putting.successful_putt(hole_distance,v0,theta) #bool, was putt made
            if make:
                #putt made
                stillframe_made_putt(hole_distance,theta,max_d+1)
            else:
                #putt missed
                stillframe_long(hole_distance,pos,theta,max_d+1)
        #save image
        plt.savefig(save_handle)
        plt.close()
    
    #now, reopen all the images and combine to gif
    with imageio.get_writer(handle+".gif", mode='I') as writer:
        for i in range(num_frames):
            cur_handle = handle+str(i)+".png"
            image = imageio.imread(cur_handle)
            writer.append_data(image)   
            #finally, delete all the .png files
            os.remove(cur_handle)
            
def plot_allowable_initial_speeds(min_distance,max_distance,theta=0,ylimit=[0,7]):
    #plot the upper and lower bounds for the allowable speeds to make the putt 
    #given the distance to the hole
    xs = np.linspace(min_distance,max_distance,100)
    a=0.9+np.sin(9.8*np.pi*theta/180)
    upper = [np.sqrt(1.31**2+2*a*xs[i]) for i in range(100)]
    lower = [np.sqrt(2*a*xs[i]) for i in range(100)]
    plt.fill_between(xs,lower,upper,color='green')
    plt.ylim(ylimit[0],ylimit[1])
    plt.xlabel('Length of Putt')
    plt.ylabel('Velocity')
    plt.title('Initial Velocity for Made Putt, '+str(theta)+' Degree Grade')
    
    
                 
                    
            
        
    
        
    
            

