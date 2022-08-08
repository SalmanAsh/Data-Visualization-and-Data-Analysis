import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]
plt.style.use("seaborn")

fig, ax = plt.subplots()
ax.plot(input_values, square, linewidth=3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of value", fontsize=14)

# set size of tick labals
ax.tick_params(axis='both', labelsize=14)

plt.show()
