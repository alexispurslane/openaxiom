#!/usr/bin/env python3

# Calculate skill progression with 3 story points per session (no accumulation)
current_skill = 10  # Starting skill value after character creation
print(f"Session 0: Skill = {current_skill}")

# Simulate progression for 10 sessions
for session_count in range(1, 11):
    story_points_this_session = 3  # 3 story points per session
    
    # Spend story points to improve skill (only from this session)
    points_spent_this_session = 0
    while points_spent_this_session < story_points_this_session:
        # Calculate cost to improve skill to next level
        next_level_cost = (current_skill + 1) - 9  # next level cost = new value - 9
        
        if story_points_this_session - points_spent_this_session >= next_level_cost:
            # We can afford to improve the skill with points from this session only
            points_spent_this_session += next_level_cost
            current_skill += 1
        else:
            # Can't afford to improve further with just this session's points
            break

    print(f"Session {session_count}: Skill = {current_skill}, Points spent = {points_spent_this_session}")