"""Visualize the two-link arm in a few configurations."""

import numpy as np
import matplotlib.pyplot as plt

from manipulator import TwoLinkArm, plot_arm


def main():
    arm = TwoLinkArm(link1_length=1.0, link2_length=0.8)  ###used [main()]function. 1. Reusable 2. Seperating variables 3. Legibility 4. Conventional
### keyword arguments
    configs = [
        (0.0, 0.0),
        (np.pi / 4, np.pi / 4),
        (np.pi / 2, -np.pi / 3),
        (np.pi, np.pi / 2),
    ]

    fig, axes = plt.subplots(1, 4, figsize=(20, 5))  ###numpy array
    for ax, (t1, t2) in zip(axes, configs):
        plot_arm(arm, t1, t2, ax=ax)          ###for loop and zip.
    plt.tight_layout()
    plt.savefig("examples/arm_configurations.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
