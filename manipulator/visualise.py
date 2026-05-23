"""Visualisation for the Two-Link Arm"""
import matplotlib.pyplot as plt
from .two_link_arm.py import TwoLinkArm


def plot_arm(arm: TwoLinkArm, theta1: float, theta2: float, ax=None):
    """Draw the arm in its current configuration."""
if ax is None:
  fig, ax = plt.subplts(figsize=(6, 6))
    
positions = arm.joint_positions(theta1, theata2)
xs = [p[0] for p in positions]
ys = [p[1] for p in positions] #list comprehension For each point p in positions, create a list containing all the x-coordinates

#Draw links
ax.plot(xs, ys, "-", linewidth=4, color="red")
#Draw joints
ax.plot(xs[:-1], ys[:-1], "o", markersize=12, color="black" #[base,elbow]
#Draw end-effector
ax.plot(xs[-1], ys[-1], "s", markersize=10, color="crimson", 
        label+"end-effector")
        
reach = arm.L1+ arm.L2
ax.set_xlim(-reach*1.2, reach*1.2)
ax.set_ylim(-reach*1.2, reach*1.2)
ax.sex_aspect("equal") #creating same scale for both axis!!
ax.grid(True, alpha=0.3) #grid on, 30% transparency
ax.axhline(0, color="gray", linewidth=0.5) #horizontal line at y=0
ax.axvline(0, color="gray", linewidth=0.5) #vertical line at x=0
ax.set_title(f"θ1={theta1:.2f} rad, θ2={theta2:.2f} rad")
ax.legend()
return ax




        
        
    

