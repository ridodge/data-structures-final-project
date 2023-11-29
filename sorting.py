
def convert_linked_to_array(node):
    """Convert a linked list to an array."""
    arr = []
    arr.append(node)
    while node.next_student is not None:
        node = node.next_student
        arr.append(node)
    return arr


def selection_sort(array):
    """Sort array of students"""
    size = len(array)
    for index in range(size):
        min_student = index
        for student in range(index + 1, size):
            # select the minimum element in every iteration
            if array[student].overall_grade < array[min_student].overall_grade:
                min_student = student
        # swapping the elements to sort the array
        (array[index], array[min_student]) = (array[min_student], array[index])
    return array

