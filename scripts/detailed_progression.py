#!/usr/bin/env python3

# Calculate skill progression with 3 story points per session
current_skill = 10  # Starting skill value after character creation
total_story_points = 0
session_count = 0

print(f"Session {session_count}: Skill = {current_skill}, Points = {total_story_points}")

# Simulate progression until 100% success rate
while session_count < 50:  # Set a reasonable upper limit
    session_count += 1
    total_story_points += 3  # 3 story points per session
    
    # Spend story points to improve skill
    points_spent_this_session = 0
    while total_story_points > 0:
        # Calculate cost to improve skill to next level
        next_level_cost = (current_skill + 1) - 9  # next level cost = new value - 9
        
        if total_story_points >= next_level_cost:
            # We can afford to improve the skill
            total_story_points -= next_level_cost
            points_spent_this_session += next_level_cost
            current_skill += 1
        else:
            # Can't afford to improve further
            break

    # Calculate success rate for average difficulty task (3d6)
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k <= current_skill:
                    count += 1
    success_rate = (count / 216) * 100
    
    print(f"Session {session_count}: Skill = {current_skill}, Points = {total_story_points}, Success Rate = {success_rate:.2f}%")
    
    if success_rate >= 100:
        print(f"100% success rate achieved at session {session_count}")
        break