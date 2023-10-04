#---------------------------------Start--------------------------------

import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

#-------------------------------Parameters----------------------------

num_molecules = 10  # Number of molecules
num_steps = 100  # Number of steps per molecule in the walk
step_length = 0.5  # Length of each step

#---------------Function to generate random steps for each molecule----

def generate_random_steps(num_molecules, num_steps):
    steps_per_molecule = []
    for i in range(num_molecules):
        steps = []
        for j in range(num_steps):
            angle = random.uniform(0, 2 * np.pi)
            x_step = step_length * np.cos(angle)
            y_step = step_length * np.sin(angle)
            steps.append((x_step, y_step))
        steps_per_molecule.append(steps)
    return steps_per_molecule

#--------------Generate random steps for each molecule------------------

steps_per_molecule = generate_random_steps(num_molecules, num_steps)

#-------------Function to update the plot for each step-----------------

def update(step):
    ax.cla()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title(f'Step {step+1}/{num_steps}')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    
    for i in range(num_molecules):
        global x_positions, y_positions
        x_step, y_step = steps_per_molecule[i][step]
        x_positions[i].append(x_positions[i][-1] + x_step)
        y_positions[i].append(y_positions[i][-1] + y_step)
        ax.plot(x_positions[i], y_positions[i])

#-----------Initialize the positions for each molecule------------------

x_positions = [[0] for _ in range(num_molecules)]
y_positions = [[0] for _ in range(num_molecules)]

#-----------------------Create the animation-----------------------------

fig = plt.figure()
ax = fig.add_subplot(111)
ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=100)

#----------------------Display the animation-----------------------------
plt.show()
#------------------------------End---------------------------------------
