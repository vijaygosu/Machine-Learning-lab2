from collections import Counter
import numpy as np

def manhattan_distance(point1, point2):
    # Calculate the Manhattan distance between two points
    return np.sum(np.abs(point1 - point2))

def knn_classifier_manhattan(training_data, labels, new_point, k):
    # k-Nearest Neighbors classifier using Manhattan distance
    distances = []
    for i, point in enumerate(training_data):
        # Calculate the Manhattan distance between the new point and each point in the training data
        distance = manhattan_distance(point, new_point)
        # Store the distance along with the corresponding label
        distances.append((distance, labels[i]))
    
    # Sort the distances in ascending order
    distances.sort()
    
    # Select the k nearest neighbors
    k_nearest_neighbors = distances[:k]
    
    # Count the occurrences of each label among the k nearest neighbors
    nearest_labels = [label for (_, label) in k_nearest_neighbors]
    label_counts = Counter(nearest_labels)
    
    # Return the label with the highest count
    return max(label_counts, key=label_counts.get)

# Example usage
training_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
labels = ['A', 'A', 'A', 'B', 'B']
new_point = np.array([3.5, 4.5])
k = 2

predicted_label = knn_classifier_manhattan(training_data, labels, new_point, k)
print("Predicted label for the new point using Manhattan distance:", predicted_label)
