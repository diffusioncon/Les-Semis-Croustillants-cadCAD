import matplotlib.pyplot as plt
import numpy as np


def plot_results(results, plot_distance=200000):
    df = np.asarray(results)
    df = {k: [dic[k] for dic in df] for k in df[0]}
    plt.plot(df['timestep'][0: plot_distance], df['production'][0: plot_distance], label='Production')
    plt.plot(df['timestep'][0: plot_distance], df['villagers_consumption'][0: plot_distance],
             label='Villagers Consumption')
    plt.plot(df['timestep'][0: plot_distance], df['businesses_consumption'][0: plot_distance],
             label='Businesses Consumption')
    plt.plot(df['timestep'][0: plot_distance], df['hospital_consumption'][0: plot_distance],
             label='Hospital Consumption')
    plt.title("Production/Consumption")
    plt.legend()
    plt.show()

    plt.plot(df['timestep'][0: plot_distance], df['grids'][0: plot_distance],
             label='Solar panels + Storages')
    for b in range(len(df['bank'])):
        df['bank'][b] = df['bank'][b]/1000
    plt.plot(df['timestep'][0: plot_distance], df['bank'][0: plot_distance],
             label='Bank (1000 units)')
    plt.title("Panels/Bank")
    plt.legend()
    plt.show()

    plt.plot(df['timestep'][0: plot_distance], df['ask'][0: plot_distance],
             label='Ask')
    for b in range(len(df['bank'])):
        df['bank'][b] = df['bank'][b]/1000
    plt.plot(df['timestep'][0: plot_distance], df['bid'][0: plot_distance],
             label='Bid')
    plt.plot(df['timestep'][0: plot_distance], df['price'][0: plot_distance],
             label='Price')
    plt.title("Market")
    plt.legend()
    plt.show()
