import matplotlib.pyplot as plt
import numpy as np


def plot_results(results, plot_distance=100):
    df = np.asarray(results)
    df = {k: [dic[k] for dic in df] for k in df[0]}
    plt.plot(df['timestep'][0: plot_distance], df['production'][0: plot_distance], label='Production')
    plt.plot(df['timestep'][0: plot_distance], df['villagers_consumption'][0: plot_distance],
             label='Villagers Consumption')
    plt.plot(df['timestep'][0: plot_distance], df['businesses_consumption'][0: plot_distance],
             label='Businesses Consumption')
    plt.plot(df['timestep'][0: plot_distance], df['hospital_consumption'][0: plot_distance],
             label='Hospital Consumption')
    plt.legend()
    plt.show()
