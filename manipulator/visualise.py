"""Visualisation for the Two-Link Arm"""
import matplotlib.pyplot as plt
from .two_link_arm.py import TwoLinkArm


def plot_arm(arm: TwoLinkArm, theta1: float, theta2: float, ax=None):
    """Draw the arm in its current configuration."""
if ax is None:
  fig, ax = plt.subplts(figsize=(6, 6))
  
