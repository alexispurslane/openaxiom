#!/usr/bin/env python3

# Calculate when skill reaches 100% success rate
for skill in range(10, 20):
    # Calculate success rate for average difficulty task (3d6)
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k <= skill:
                    count += 1
    success_rate = (count / 216) * 100
    print(f"Skill {skill}: {success_rate:.2f}% success rate")
    
    if success_rate >= 100:
        print(f"100% success rate achieved at skill level {skill}")
        break