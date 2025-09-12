# Calculate the total story points needed to advance from skill 10 to 18
total_points = 0
for skill_level in range(11, 19):  # From 11 to 18
    cost = skill_level - 9
    total_points += cost
    print(f"Skill {skill_level}: Cost = {cost}, Total = {total_points}")

print(f"\nTotal story points needed: {total_points}")