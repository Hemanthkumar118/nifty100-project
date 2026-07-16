import matplotlib.pyplot as plt
import numpy as np
import os

def generate_radar(company, metrics, values):

    os.makedirs("reports/radar_charts", exist_ok=True)

    labels = np.array(metrics)
    stats = np.array(values)

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)

    ax.plot(angles, stats, linewidth=2)
    ax.fill(angles, stats, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(company)

    filename = f"reports/radar_charts/{company}_radar.png"

    plt.savefig(filename)
    plt.close()

    print("Saved:", filename)