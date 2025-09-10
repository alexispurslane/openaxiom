#!/usr/bin/env python3
# /// script
# dependencies = [
#     "matplotlib",
#     "seaborn",
#     "numpy",
#     "scipy",
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.interpolate import interp1d

# Set up the plot style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Calculate skill progression with 3 story points per session
sessions = []
success_rates = []

# Starting values
current_skill = 10  # Starting skill value after character creation
total_story_points = 0
session_count = 0

# Record initial state
sessions.append(session_count)
# Calculate success rate for skill 10 on average difficulty task (3d6)
count = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i + j + k <= current_skill:
                count += 1
success_rate = (count / 216) * 100
success_rates.append(success_rate)

# Simulate progression until 100% success rate or max sessions
max_sessions = 50  # Set a reasonable upper limit
while session_count < max_sessions and success_rate < 100:
    session_count += 1
    total_story_points += 3  # 3 story points per session
    
    # Spend story points to improve skill
    while total_story_points > 0:
        # Calculate cost to improve skill to next level
        next_level_cost = (current_skill + 1) - 9  # next level cost = new value - 9
        
        if total_story_points >= next_level_cost:
            # We can afford to improve the skill
            total_story_points -= next_level_cost
            current_skill += 1
        else:
            # Can't afford to improve further
            break

    # Update our records after this session (only once per session)
    sessions.append(session_count)
    
    # Calculate success rate for average difficulty task (3d6)
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k <= current_skill:
                    count += 1
    success_rate = (count / 216) * 100
    success_rates.append(success_rate)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create smooth curve using interpolation
if len(sessions) > 1:
    # Create interpolation function for smooth curve
    f = interp1d(sessions, success_rates, kind='cubic')
    
    # Generate more points for smooth curve
    sessions_smooth = np.linspace(min(sessions), max(sessions), 300)
    success_rates_smooth = f(sessions_smooth)
    
    # Plot smooth curve
    ax.plot(sessions_smooth, success_rates_smooth, linewidth=3, color='#2E86AB')
    
    # Plot original data points
    ax.plot(sessions, success_rates, 'o', markersize=8, color='#2E86AB')

# Customize the plot
ax.set_xlabel('Session Number', fontsize=14, fontweight='bold')
ax.set_ylabel('Success Rate (%)', fontsize=14, fontweight='bold')
ax.set_title('Skill Progression: Success Rate Increase Over Time\n(3 Story Points Earned Per Session)', 
             fontsize=16, fontweight='bold', pad=20)

# Add grid
ax.grid(True, alpha=0.3)

# Set axis limits
ax.set_xlim(0, max(sessions))
ax.set_ylim(0, 100)

# Add some styling
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

# Add annotations for start and end points
if success_rates:
    # Initial point (first point) - position it correctly at the first data point
    ax.annotate(f'Start: {success_rates[0]:.1f}%', 
                xy=(sessions[0], success_rates[0]), 
                xytext=(sessions[0]+0.5, success_rates[0]+8),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.1', color='gray'),
                fontsize=10, ha='center')
    
    # Final point (last point)
    ax.annotate(f'End: {success_rates[-1]:.1f}%', 
                xy=(sessions[-1], success_rates[-1]), 
                xytext=(sessions[-1]-0.5, success_rates[-1]-8),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.1', color='gray'),
                fontsize=10, ha='center')

# Save as SVG
plt.tight_layout()
plt.savefig('/Users/alexispurslane/Documents/ttrpg/skill_progression.svg', format='svg', bbox_inches='tight')
print(f"Graph saved as skill_progression.svg")
print(f"Progression completed in {session_count} sessions")