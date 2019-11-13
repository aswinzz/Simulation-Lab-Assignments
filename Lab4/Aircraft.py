#    Thrust remains constant at T = 1450N balacing the drag force (D)
#    beta is used to calcuate the air density (roh) at height h.

#    UNITS:
#    Thrust: N (Newton)
#    Weight: Kg
#    wing_area: m^2
#    roh0: kg/m^3
#    height: m
#    velocity: m/s^2

#    dt: s
#    dW/dt = -k where k = 0.013
#    L (Lift) = (1/2)*(roh)*(V^2)*(Cl)*S
#    D (Drag) = (1/2)*(roh)*(V^2)*(Cd)*S
#    Cd = cd0 + K*(Cl^2)
#    sigma = exp(height/beta) = roh/roh0 where roh0 is the air density at sea level

import math

weight = 10000.0
wing_area = 6
thrust = 1450
beta = 9296
height = 8000
cd0 = 0.025
K = 0.035
k = 0.013
roh0 = 1.225
dt = 0.01

def roh_calc():
   sigma = math.exp((-height)/float(beta))
   roh = (roh0 * sigma)
   return roh


# Considering P = (1/2)*(roh)*(V^2)*S = (thrust + sqrt((thrust*thrust) - 4*(cd0)*(K*weight*weight)))/(double)(2*cd0)
#   for easier calulations.

def p_cal():
    pval = ( thrust + math.sqrt( (thrust*thrust) - (4*(cd0)*(K*weight*weight)) ))/float(2*cd0)
    return pval

def velocity():
    roh = roh_calc()
    p = p_cal()
    return math.sqrt((2*p)/float(roh*wing_area))

distance = 0.0
# 1 hour = 36000 seconds

for i in range(36000):
    weight -= k
    new_velocity = velocity()
    distance += new_velocity*dt
    print("W = " + str(weight) + "  " + "V = " + str(new_velocity) + " Distance coverd in dt = " + str(new_velocity*dt))
    
print("Total distance (m) = " + str(distance))