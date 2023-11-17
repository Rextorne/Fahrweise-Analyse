import time
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd



def showVelocityAcceleration(axes):
    df = pd.read_csv('/home/nru/Documents/BMS/IDPA/Auto/Experiment/Messwerte/oekologisch.csv')
    print(df["time"], df["Geschwindigkeit"])
    # change datatype to datetime for time calculations
    df["time"] = pd.to_datetime(df["time"])

    Geschwindigkeit_arr = df[~df['Geschwindigkeit'].isna()].to_numpy()

    Geschwindigkeit_arr = np.delete(Geschwindigkeit_arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 1)

    time_diff = np.diff(Geschwindigkeit_arr[:, 0])
    velo_diff = np.diff(Geschwindigkeit_arr[:, 1])

    for idx, element in enumerate(time_diff):
        time_diff[idx] = element.total_seconds()

    acc = (velo_diff / 3.6) / time_diff

    acc_idx = np.arange(0, len(acc), 1)
    Geschwindigkeit_idx = np.arange(0, len(Geschwindigkeit_arr[:, 0]), 1)

    axes[0,0].plot(Geschwindigkeit_idx, Geschwindigkeit_arr[:, 1])
    axes[1,0].plot(acc_idx, acc)


def showVelocityFuel(axes):
    df = pd.read_csv('/home/nru/Documents/BMS/IDPA/Auto/Experiment/Skripte/out_oekologisch.csv')

    velocity = df["Geschwindigkeit"].to_numpy()
    fuel = df["Zeit-Kraftstoffverbrauch."].to_numpy()

    velo_diff = np.diff(velocity).astype(float)
    velo_diff[velo_diff > 30] = np.nan
    velo_diff[velo_diff < -30] = np.nan
    fuel_diff = np.diff(fuel)
    velo_idx = np.arange(0, len(velo_diff), 1)
    fuel_idx = np.arange(0, len(fuel), 1)

    axes[0,1].plot(fuel_idx,fuel)

    axes[1,1].plot(velo_idx, velo_diff, label='velocity derivation')
    axes[1,1].plot(velo_idx, fuel_diff, label='fuel consumption time derivation')


if __name__ == "__main__":
    fig, axs = plt.subplots(2,2, sharex=True)

    fig.suptitle("Ökologische Fahrweise")

    axs[0,0].set_title("Geschwindigkeit")
    axs[0,1].set_title("Verbrauch")
    axs[1,0].set_title("Beschleunigung")
    axs[1,1].set_title("Ableitung Geschwindigkeit und Verbrauch")

    axs[0,0].set_ylabel("Geschwindigkeit [km/h]")
    axs[0,1].set_ylabel("Verbrauch [l/h]")
    axs[1,0].set_ylabel("Beschleunigung [m/s2]")
    axs[1,1].set_ylabel("Ableitung")






    showVelocityAcceleration(axs)
    showVelocityFuel(axs)
    axs[1,1].legend()
    plt.show()