import matplotlib.pyplot as plt
import numpy as np


def plot_door(
    distances: list[float], torques: list[float], door_length: float = 0.75
) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot([0, door_length], [0, 0], "saddlebrown", linewidth=10, label="Door")

    # Annotate points of force application and calculate torques
    for i, distance in enumerate(distances):
        ax.plot(distance, 0, "bo", markersize=8)  # Points where force is applied
        ax.annotate(
            f"{torques[i]:.1f} Nm",
            (distance, 0.05),
            ha="center",
            color="blue",
            fontsize=10,
        )
        ax.arrow(
            distance, 0, 0, 0.1, head_width=0.05, head_length=0.05, color="black"
        )  # Force arrows

    # Add curved line for arc of the door's movement
    theta = np.linspace(0, np.pi / 2, 100)
    for dist in distances:
        arc_x = dist * np.cos(theta)
        arc_y = dist * np.sin(theta)
        ax.plot(arc_x, arc_y, "r--", linewidth=1)

    # Add labels and formatting
    ax.set_xlim(-0.1, door_length + 0.1)
    ax.set_ylim(-0.2, door_length + 0.1)
    ax.set_title("Torque on a Door with Force Applied at Different Points")
    ax.set_xlabel("Distance from Hinge (m)")
    ax.get_yaxis().set_visible(False)
    plt.show()
