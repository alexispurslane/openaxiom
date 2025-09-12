#!/usr/bin/env python3

# Calculate skill progression with 3 story points per session (with accumulation)
current_skill = 10  # Starting skill value after character creation
total_story_points = 0
session_count = 0

print(f"Initial state: Session {session_count}, Skill = {current_skill}, Points = {total_story_points}")

# Simulate progression for 5 sessions to see the pattern
for i in range(5):
    session_count += 1
    total_story_points += 3  # 3 story points per session
    print(f"Session {session_count}: Earned 3 points, Total = {total_story_points}")
    
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
            print(f"  Improved to skill {current_skill}, Cost = {next_level_cost}, Remaining points = {total_story_points}")
        else:
            # Can't afford to improve further
            break
    
    if points_spent_this_session > 0:
        print(f"  Spent {points_spent_this_session} points this session")
    else:
        print(f"  No improvements made this session")