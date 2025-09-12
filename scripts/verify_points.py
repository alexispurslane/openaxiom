#!/usr/bin/env python3

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

print(f"First point - Session: {sessions[0]}, Success Rate: {success_rates[0]:.1f}%")

# Simulate one session to see the second point
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

print(f"Second point - Session: {sessions[1]}, Success Rate: {success_rates[1]:.1f}%")