import numpy as np

#Some functions for computing quantities associated with putting
#rename this to putting physics

def compute_final_distance(v0,theta):
    #Compute how far a putted ball will roll on a green given initial speed and green slope
    # Function assumes PGA average green speeds
    # INPUTS:
    # theta: float, slope of green in degrees. Positive indicates putting uphill, negative downhill.
    #        absolute values over 5.36 degrees return errors because the ball never comes to rest
    # v0: postivefloat, initial speed of putt in m/s
    
    if np.abs(theta)>5.36:
        print('Too Steep!')
        return
    if v0<0:
        print('Must Input Positive Speed')
        return
    fric_accel = -5*0.131/7*9.8
    grav_accel = 9.8*np.sin(-np.pi*theta/180)
    a = fric_accel+grav_accel 
    t = v0/(-a) #this works because we force a<0 and v0>0
    return(v0*t+0.5*a*t*t)

def compute_time_to_rest(v0,theta):
    # How long it takes the putted ball to come to rest
    # INPUTS:
    # v0: postive float, initial speed of putt in m/s
    # theta: float, slope of green in degrees. Positive indicates putting uphill, negative downhill.
    a=-5*0.131/7*9.8+9.8*np.sin(-np.pi*theta/180)
    return(v0/-a)
    
    
def compute_cur_pos(v0,theta,t):
    #Compute ball's current location given initial velocity, slope, and time
    # INPUTS:
    # v0: postive float, initial speed of putt in m/s
    # theta: float, slope of green in degrees. Positive indicates putting uphill, negative downhill.
    # t: positive float, time since putt
    if np.abs(theta)>5.36:
        print('Too Steep!')
        return
    if(t>compute_time_to_rest(v0,theta)):
        return(compute_final_distance(v0,theta))
    a=-5*0.131/7*9.8+9.8*np.sin(-np.pi*theta/180)
    return(v0*t+0.5*a*(t**2))

    
def simulate_uniform_speeds(v0,theta,precision,npts):
    #Assuming v0 is the perfect speed to make the putt and the golfer hits within +/- "precision"
    #percent of this speed, return the distribution of sitances the putts will travel. 
    # INPUTS:
    # v0: positive float, average initial speed of putt
    # theta: float, slope of green in degrees. Positive indicates putting uphill, negative downhill.
    #        absolute values over 5 degrees return errors because the ball never comes to rest
    # precision: float in [0,100], max percent error in putting speed rel. v0
    # npts: positive int, number of speeds to compute travel distance for
    if np.abs(theta)>5.36:
        print('Too Steep!')
        return
    if v0<0:
        print('Must Input Positive Speed')
        return
    if precision<0 or precision>100:
        print('Precision must be in [0,100]')
        return
    min_velocity=(1-precision/100)*v0
    max_velocity=(1+precision/100)*v0
    Delta_V = (max_velocity-min_velocity)/(npts+1)
    test_velocities = [i*Delta_V+min_velocity for i in range(npts)]
    distances = [compute_final_distance(test_velocities[i],theta) for i in range(npts)]
    return(distances)

def successful_putt(distance,v0,theta):
    #determines whether a put is made.
    #INPUT:
    #distance: positive float, distance to the hole
    #v0: positive float, the initial velocity of the putt
    #theta: the incline of the green (deg), positive uphill
    
    a=-5*0.131/7*9.8+9.8*np.sin(-np.pi*theta/180)
    #either the putt falls short or it makes it there
    dist_travelled = v0**2/(-2*a)
    if dist_travelled < distance:
        return False
    else:
        #putt makes it there, is it too fast?
        #v^2=v_0^2+2ax
        v_at_cup = np.sqrt(v0**2+2*a*distance)
        #for condition, see http://large.stanford.edu/courses/2007/ph210/kolkowitz2/
        if v_at_cup <1.31:
             return True
        else:
            return False

def succesful_putt_prob_uniform_error(distance,v0,theta,precision,npts):
    #probability of succesfull putt with a uniformly distributed error in putt velo
    # INPUTS
    # distance: positive float, distance to hole
    # v0: positive float, average initial velocity
    # theta: float, incline of green, positive=uphill
    # precision: float in [0,100], max percent error in putting speed rel. v0
    # npts: positive int, number of speeds to compute travel distance for
    min_velocity=(1-precision/100)*v0
    max_velocity=(1+precision/100)*v0
    Delta_V = (max_velocity-min_velocity)/(npts+1)
    test_velocities = [i*Delta_V+min_velocity for i in range(npts)]
    successes= [succesful_putt(distance,test_velocities(i),theta) for i in range(npts)]
    return successes

def perfect_velo(distance,theta):
    #calculate perfect initial velocity to make the putt. Formula v_f^2=v_0^2+2ax.
    #Perfect putt means v_f=0 when x=distance to hole

    # INPUTS
    # distance: positive float, distance to hole
    # theta: float, incline of green, positive=uphill
    a=-5*0.131/7*9.8+9.8*np.sin(-np.pi*theta/180)
    if a>0:
        print('Too Steep!')
        return
    return(np.sqrt(-2*a*distance))  



    
        
