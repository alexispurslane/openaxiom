#!/usr/bin/env python3

# Data: roll value, frequency, cumulative frequency
data = [
    [3, 1, 1],
    [4, 3, 4],
    [5, 6, 10],
    [6, 10, 20],
    [7, 15, 35],
    [8, 21, 56],
    [9, 25, 81],
    [10, 27, 108],
    [11, 27, 135],
    [12, 25, 160],
    [13, 21, 181],
    [14, 15, 196],
    [15, 10, 206],
    [16, 6, 212],
    [17, 3, 215],
    [18, 1, 216]
]

# Calculate cumulative probabilities (cumulative frequency / 216)
print("Roll\tFreq\tCumFreq\tCumProb")
print("----\t----\t-------\t-------")
for row in data:
    roll, freq, cum_freq = row
    cum_prob = cum_freq / 216 * 100  # Percentage
    print(f"{roll}\t{freq}\t{cum_freq}\t{cum_prob:.2f}%")