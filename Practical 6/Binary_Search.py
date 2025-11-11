"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found
"""

def find_rank(scores, target_score):
    left, right = 0, len(scores) - 1

    while left <= right:
        mid = (left + right) // 2
        if scores[mid] == target_score:
            return len(scores) - mid  # Rank is position from the end
        elif scores[mid] < target_score:
            right = mid - 1  # Look in the left half (higher scores)
        else:
            left = mid + 1  # Look in the right half (lower scores)

    # If the exact score isn't found, return the rank it would have
    return len(scores) - right

# Example usage
scores = [95, 90, 85, 80, 75, 70, 65, 60]  # Sorted in descending order
student_score = 82

rank = find_rank(scores, student_score)
print(f"A student with a score of {student_score} would rank {rank} in the class.")
