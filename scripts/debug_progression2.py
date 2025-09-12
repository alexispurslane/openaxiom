#!/usr/bin/env python3

# Calculate skill progression with 3 story points per session (with accumulation)
sessions = []
current_skill = 10  # Starting skill value after character creation
total_story_points = 0

# Record initial state
sessions.append(0)
print(f"Point 0: Session 0, Skill = {current_skill}")

# Simulate progression for 5 sessions to see the pattern
for session_count in range(1, 6):
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
    print(f"Point {session_count}: Session {session_count}, Skill = {current_skill}")

print(f"Total data points: {len(sessions)}")