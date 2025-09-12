# /// script
# dependencies = [
#     "matplotlib",
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np
import math

# Calculate HP for each body part based on strength skill
def calculate_hp(strength):
    torso = strength
    head = math.ceil(strength / 2)
    arm = math.ceil((2 * strength) / 3)
    leg = math.ceil((2 * strength) / 3)
    total = torso + head + arm * 2 + leg * 2  # Two arms and two legs
    return torso, head, arm, leg, total

# Generate data for strength values 9-18
strengths = list(range(9, 19))
torso_hps = []
head_hps = []
arm_hps = []
leg_hps = []
total_hps = []

for strength in strengths:
    torso, head, arm, leg, total = calculate_hp(strength)
    torso_hps.append(torso)
    head_hps.append(head)
    arm_hps.append(arm)
    leg_hps.append(leg)
    total_hps.append(total)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(strengths, torso_hps, label='Torso', marker='o')
plt.plot(strengths, head_hps, label='Head', marker='s')
plt.plot(strengths, arm_hps, label='Each Arm', marker='^')
plt.plot(strengths, leg_hps, label='Each Leg', marker='v')
plt.plot(strengths, total_hps, label='Total HP', marker='D', linewidth=2)

plt.xlabel('Physical (Strength) Skill')
plt.ylabel('Hit Points')
plt.title('Hit Points by Body Location vs. Physical (Strength) Skill')
plt.legend()
plt.grid(True, alpha=0.3)

# Save as SVG
plt.savefig('health_vs_skill.svg', format='svg', bbox_inches='tight')
plt.close()

print("Graph saved as health_vs_skill.svg")