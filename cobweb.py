import numpy as np
import matplotlib.pyplot as plt


#define your map
def mapp(r, x):
    return  r * np.cos(x)


def coweb(r, x0, n, ax=None):
    
    # Plot the function and the y=x diagonal line.
    t = np.linspace(-10, 10,100)
 
    ax.plot(t, mapp(r, t), 'red', lw=2)
    ax.plot([-2, 2], [-2, 2], 'k', lw=2)

    # Recursively apply y=f(x) and plot two lines:

    x = x0
    for i in range(n):
        y = mapp(r, x)
        
        # Add arrow to indicate direction
        ax.annotate('', xy=(x, y), xytext=(x, x),
                    arrowprops=dict(arrowstyle="->", color="black", lw=0.8))
        ax.annotate('', xy=(y, y), xytext=(x, y),
                    arrowprops=dict(arrowstyle="->", color="black", lw=0.8))

        # Plot the points.
        ax.plot([x], [y], '.', color="k")
        
        x = y

    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 2)
    ax.axhline(y=0, color='grey', linestyle='--', linewidth=1)
    ax.axvline(x=0, color='grey', linestyle='--', linewidth=1)
    ax.set_xlabel(r"$x_n$")
    ax.set_ylabel(r"$x_{n+1}$")
    ax.set_title(f"$r={r:.1f}, \, x_0={x0:.1f}$")

x = np.linspace(0, 1)

fig, ax1 = plt.subplots(figsize=(8, 8))
coweb(1, -2, 10, ax=ax1)
plt.show()

#%% Plot the time series 

# Number of iterations
num_iterations = 20

# Create arrays to store the results
x_values = np.zeros(num_iterations)
iteration_values = np.arange(num_iterations)

# Generate logistic map data for each value of r

#ics and parameter

x = 0.6
r = 1

for j in range(num_iterations):
    x_values[j] = x
    x = mapp(r, x)

plt.rcParams.update({'font.size': 22}) 
# Increase the size of the subplots
plt.figure(figsize=(10, 6))


plt.plot(iteration_values[0:], x_values[0:], linewidth=1.5)
plt.xlabel('n')
plt.ylabel('$x_n$')
plt.grid(True)

plt.subplots_adjust(wspace=0.28)  
plt.show()

print(x_values[-1])
