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
print("Physical (Strength) | Torso | Head | Each Arm | Each Leg | Total HP")
print("---------------------|-------|------|----------|----------|----------")

for strength in range(9, 19):
    torso, head, arm, leg, total = calculate_hp(strength)
    print(f"{strength:18} | {torso:5} | {head:4} | {arm:8} | {leg:8} | {total:8}")