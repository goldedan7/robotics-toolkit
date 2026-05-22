"""Visualize the two-link arm in a few configurations."""

import numpy as np
import matplotlib.pyplot as plt

from manipulator import TwoLinkArm, plot_arm


def main():
    arm = TwoLinkArm(link1_length=1.0, link2_length=0.8)

    configs = [
        (0.0, 0.0),
        (np.pi / 4, np.pi / 4),
        (np.pi / 2, -np.pi / 3),
        (np.pi, np.pi / 2),
    ]

    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    for ax, (t1, t2) in zip(axes, configs):
        plot_arm(arm, t1, t2, ax=ax)

    plt.tight_layout()
    plt.savefig("examples/arm_configurations.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
