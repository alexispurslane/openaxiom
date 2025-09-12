#!/usr/bin/env python3
# /// script
# dependencies = [
#     "matplotlib",
#     "numpy",
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np

# 3d6 distribution data (roll value, frequency)
roll_data = [
    [3, 1],
    [4, 3],
    [5, 6],
    [6, 10],
    [7, 15],
    [8, 21],
    [9, 25],
    [10, 27],
    [11, 27],
    [12, 25],
    [13, 21],
    [14, 15],
    [15, 10],
    [16, 6],
    [17, 3],
    [18, 1]
]

# Difficulty levels with their modifiers and target numbers (based on skill 9)
difficulty_levels = [
    ("Nearly Impossible", -3, 6),
    ("Very Hard", -2, 7),
    ("Hard", -1, 8),
    ("Medium", 0, 9),
    ("Moderate", 1, 10),
    ("Easy", 2, 11),
    ("Very Easy", 3, 12)
]

# Colors for each difficulty level
colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3']

# Function to calculate probabilities for each degree of success/failure
def calculate_probabilities(target):
    # Initialize counters for each category
    critical_success = 0
    exceptional_success = 0
    standard_success = 0
    marginal_failure = 0
    exceptional_failure = 0
    critical_failure = 0
    
    # Calculate probabilities for each roll
    for roll, frequency in roll_data:
        if roll in [3, 4]:  # Critical Success
            critical_success += frequency
        elif roll <= target - 5:  # Exceptional Success (5 or more below target)
            exceptional_success += frequency
        elif roll <= target:  # Standard Success (equal to target or 1-4 below)
            standard_success += frequency
        elif roll in [17, 18]:  # Critical Failure
            critical_failure += frequency
        elif roll >= target + 5:  # Exceptional Failure (5 or more above target)
            exceptional_failure += frequency
        else:  # Marginal Failure (1-4 above target)
            marginal_failure += frequency
    
    # Convert to percentages
    total = 216  # Total possible outcomes (6^3)
    return {
        'Critical Success': critical_success / total * 100,
        'Exceptional Success': exceptional_success / total * 100,
        'Standard Success': standard_success / total * 100,
        'Marginal Failure': marginal_failure / total * 100,
        'Exceptional Failure': exceptional_failure / total * 100,
        'Critical Failure': critical_failure / total * 100
    }

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Create bar chart for each difficulty level
x = np.arange(len(difficulty_levels))
bar_width = 0.12
categories = ['Critical Success', 'Exceptional Success', 'Standard Success', 
              'Marginal Failure', 'Exceptional Failure', 'Critical Failure']

# Calculate probabilities for each difficulty level
all_probabilities = []
for name, modifier, target in difficulty_levels:
    probs = calculate_probabilities(target)
    all_probabilities.append(probs)

# Plot bars for each category
for i, category in enumerate(categories):
    values = [probs[category] for probs in all_probabilities]
    ax.bar(x + i * bar_width, values, bar_width, label=category)

# Customize the plot
ax.set_xlabel('Difficulty Level', fontsize=14, fontweight='bold')
ax.set_ylabel('Probability (%)', fontsize=14, fontweight='bold')
ax.set_title('Probability of Degrees of Success and Failure\nat Different Difficulty Levels (Skill 9)', 
             fontsize=16, fontweight='bold', pad=20)

# Set x-axis labels
ax.set_xticks(x + bar_width * 2.5)
ax.set_xticklabels([name for name, _, _ in difficulty_levels], rotation=45, ha='right')

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Add grid
ax.grid(True, alpha=0.3, axis='y')

# Set axis limits
ax.set_ylim(0, 100)

# Add some styling
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

# Adjust layout to prevent clipping
plt.tight_layout()

# Save as SVG
plt.savefig('/Users/alexispurslane/Documents/ttrpg/probability_distribution.svg', format='svg', bbox_inches='tight')
print("Graph saved as probability_distribution.svg")