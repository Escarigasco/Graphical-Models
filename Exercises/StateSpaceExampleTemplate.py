import numpy as np
import math as math
import matplotlib.pyplot as plt
# Mass Spring Damper System
# =========================
#
# --------------------------------
#       |       |
#       /     -----
#       \     |   |
#       / k   |---| d
#       \     | | |
#       |       |
#    ---------------- ---
#    |      m       |  |
#    ----------------  | p
#           |          |
#           | u        v
#           v
#

# Simulation of a first order euler approximation of a mass spring damper system

# System parameters
m = 10.0  # kg     mass
k = 1.0   # N/m    characteristic spring constant
d = 1.0   # N*s/m  characteristic damper constant


# Initial State
# The state of the mass spring damper system is composed of the position and speed of the mass m
# Create an initial state numpy array, at the position 0m and speed 0m/s. Feel free to test any other values later on
A = np.array([[0, 1], [-k/m, -d/m]])
B = np.array([[0, 1.0 / m]])
x0 = np.array([[0, 0]])



def input_u(t):
    """
    System input function
    The system input is the force that acts on the mass m
    Implement the function to return the gravitational force of the mass on the earth. To make the input a little bit
    more interesting invert the force every 100s. Feel free to play around with any other input.
    :param t: time in s
    :return: system input as numpy array
    """
    # TODO
    return None


def system_function(x_last, u, delta_t):
    """
    System function
    The system function computes the next state of the spring mass damper system given the last state, the current
    input and the time step size.
    :param x_last: System state x at previous time step
    :param u: System Input u at current time step
    :param delta_t: time step size
    :return: return next state
    """
    Ad = A.dot(delta_t) + np.identity(2)
    Bd = B.T * delta_t
    x_new = Ad.dot(x_last.T) + Bd.dot(u)
    return x_new


# Create time vector from 0s to 300s in 0.01s steps, to simulate the system
# TODO
t_vec = np.arange(0, 300, 0.1)

# Simulate system and create output vector x with all simulated states corresponding to the time vector t_vec
t_len = len(t_vec)
p = np.zeros(t_len)
p_dot = np.zeros(t_len)
iter = 0


for ti in t_vec:
    if math.floor(ti / 100) % 2 == 0:
        u = 9.81
    else:
        u = -9.81
    x0 = system_function(x0, u, 0.1).T
    p[iter] = x0[0][0]
    p_dot[iter] = x0[0][1]
    iter += 1


# Plot result
# Use two subplots to plot the position and the speed of the mass

fig, ax = plt.subplots()
ax.plot(t_vec, p, color='b', alpha=1.0)
ax.plot(t_vec, p_dot, color='r', alpha=0.5)
plt.title('Position and Speed vs Time')
plt.xlabel('Time')
plt.ylabel('Position & Speed')
plt.legend(('Position', 'Speed'))
plt.savefig('Position_and_speed_vs_time.png')
plt.show()
