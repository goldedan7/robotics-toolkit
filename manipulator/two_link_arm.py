"""
Two-link planar manipulator kinematics.

Convention:
- Base of the arm is at the origin (0, 0).
- theta1 is measured from the positive x-axis (radians).
- theta2 is the joint angle at the elbow, relative to link 1.
- All angles in radians, all lengths in meters.
"""

import numpy as np


class TwoLinkArm: #making class
    """A 2-DOF planar manipulator with two revolute joints."""

    def __init__(self, link1_length: float, link2_length: float):
        if link1_length <= 0 or link2_length <= 0:
            raise ValueError("Link lengths must be positive.")  #making error when the length is negative
        self.L1 = link1_length
        self.L2 = link2_length

    def forward_kinematics(self, theta1: float, theta2: float):
        """
        Compute the (x, y) position of the end-effector.

        Parameters
        ----------
        theta1 : float
            Angle of link 1 from the x-axis, in radians.
        theta2 : float
            Angle of link 2 relative to link 1, in radians.

        Returns
        -------
        (x, y) : tuple of floats
            End-effector position in the world frame.
        """
        x = self.L1 * np.cos(theta1) + self.L2 * np.cos(theta1 + theta2)
        y = self.L1 * np.sin(theta1) + self.L2 * np.sin(theta1 + theta2)
        return float(x), float(y)

    def joint_positions(self, theta1: float, theta2: float):
        """
        Return positions of all joints (base, elbow, end-effector).
        Useful for visualization.
        """
        base = (0.0, 0.0)
        elbow = (
            self.L1 * np.cos(theta1),
            self.L1 * np.sin(theta1),
        )
        end_effector = self.forward_kinematics(theta1, theta2)
        return [base, elbow, end_effector]
