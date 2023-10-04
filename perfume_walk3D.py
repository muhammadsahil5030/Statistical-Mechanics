import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

# Parameters
num_steps = 1000  # Number of steps in the walk
step_length = 0.5  # Length of each step

# Function to generate random steps
def generate_random_steps(num_steps):
    steps = []
    for _ in range(num_steps):
        theta = random.uniform(0, 2 * np.pi)
        phi = random.uniform(0, np.pi)
        x_step = step_length * np.sin(phi) * np.cos(theta)
        y_step = step_length * np.sin(phi) * np.sin(theta)
        z_step = step_length * np.cos(phi)
        steps.append((x_step, y_step, z_step))
    return steps

# Generate random steps
steps = generate_random_steps(num_steps)

# Function to update the plot for each step
def update(step):
    global x, y, z, x_positions, y_positions, z_positions
    x_step, y_step, z_step = steps[step]
    x += x_step
    y += y_step
    z += z_step
    x_positions.append(x)
    y_positions.append(y)
    z_positions.append(z)
    ax.cla()
    ax.plot(x_positions, y_positions, z_positions, color='blue', linewidth=2)
    ax.scatter(x, y, z, color='red')  # Plot perfume position
    ax.set_xlim(min(x_positions) - 1, max(x_positions) + 1)
    ax.set_ylim(min(y_positions) - 1, max(y_positions) + 1)
    ax.set_zlim(min(z_positions) - 1, max(z_positions) + 1)
    ax.set_title(f'Step {step+1}/{num_steps}')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_zlabel('Z Position')

# Initialize the perfume position and positions arrays
x, y, z = 0, 0, 0
x_positions, y_positions, z_positions = [0], [0], [0]

# Create the animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=100)

# Display the animation
plt.show()

