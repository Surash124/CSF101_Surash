"""def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

# Example usage
my_array = [5, 2, 9, 1, 7, 6, 3]
result = linear_search(my_array, 7)
print(f"Element found at index: {result}")"""

def find_student(student_ids, target_id):
    for i, student_id in enumerate(student_ids, start=1):
        if student_id == target_id:
            return f"Student with ID {target_id} is present at position {i}."
    return f"Student with ID {target_id} is not present in the class."

# Example usage
class_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
target_student = 1005

result = find_student(class_ids, target_student)
print(result)

# Test with a student not in the class
missing_student = 1010
result = find_student(class_ids, missing_student)
print(result)

