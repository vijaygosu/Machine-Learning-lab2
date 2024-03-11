def ED(v1, v2):
    ED = 0  # Initialize Euclidean distance
    for i in range(len(v1)):
        ED += (v1[i] - v2[i])**2  # Add squared difference between corresponding elements
    return ED**0.5  # Return square root of sum of squared differences

def MD(v1, v2):
    MD = 0  # Initialize Manhattan distance
    for i in range(len(v1)):
        MD += v1[i] - v2[i]  # Add absolute difference between corresponding elements
    return MD  # Return Manhattan distance

v1 = [1, 2]
v2 = [1, 3]

# Calculate Euclidean distance and Manhattan distance
ed = ED(v1, v2)
md = MD(v1, v2)

# Print the results
print("euclidean distance:", ed)
print("manhattan distance:", md)
