"""
Quick Sort Algorithm Implementation
==================================

Author: Sirallah
Date: December 2024
Description: Implementation of the quick sort algorithm using divide and conquer
             approach with detailed comments and examples.

Time Complexity: O(n log n) average case, O(n²) worst case
Space Complexity: O(log n) due to recursion stack
"""

def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.
    
    Quick sort uses divide-and-conquer approach:
    1. Choose a pivot element
    2. Partition array so elements < pivot are left, elements > pivot are right
    3. Recursively sort left and right subarrays
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
        
    Examples:
        >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        
        >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
    """
    if not arr or len(arr) <= 1:
        return arr
    
    # Make a copy to avoid modifying the original array
    arr_copy = arr.copy()
    _quick_sort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def _quick_sort_helper(arr, low, high):
    """
    Helper function that performs the recursive quick sort.
    
    Args:
        arr (list): Array to sort (modified in place)
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = _partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        _quick_sort_helper(arr, low, pivot_index - 1)    # Left subarray
        _quick_sort_helper(arr, pivot_index + 1, high)   # Right subarray


def _partition(arr, low, high):
    """
    Partitions the array around a pivot element.
    
    Uses the last element as pivot. Rearranges the array so that
    all elements smaller than pivot are on the left, and all elements
    greater than pivot are on the right.
    
    Args:
        arr (list): Array to partition
        low (int): Starting index
        high (int): Ending index
        
    Returns:
        int: Final position of the pivot element
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element (indicates right position of pivot)
    i = low - 1
    
    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1    # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]    # Swap elements
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_verbose(arr):
    """
    Quick sort with step-by-step output for educational purposes.
    
    Args:
        arr (list): List of elements to sort
        
    Returns:
        list: Sorted list with printed steps
    """
    if not arr:
        print("Empty array - nothing to sort")
        return []
    
    print(f"Starting Quick Sort on: {arr}")
    print("=" * 40)
    
    result = arr.copy()
    _quick_sort_verbose_helper(result, 0, len(result) - 1, 0)
    
    print("=" * 40)
    print(f"Final sorted array: {result}")
    return result


def _quick_sort_verbose_helper(arr, low, high, depth):
    """Helper function for verbose quick sort with indentation based on recursion depth."""
    indent = "  " * depth
    
    if low < high:
        print(f"{indent}Sorting subarray from index {low} to {high}: {arr[low:high+1]}")
        
        # Partition and get pivot
        pivot_index = _partition_verbose(arr, low, high, depth)
        pivot_value = arr[pivot_index]
        
        print(f"{indent}Pivot {pivot_value} is now at index {pivot_index}")
        print(f"{indent}Left subarray: {arr[low:pivot_index] if pivot_index > low else '[]'}")
        print(f"{indent}Right subarray: {arr[pivot_index+1:high+1] if pivot_index < high else '[]'}")
        print()
        
        # Recursive calls
        _quick_sort_verbose_helper(arr, low, pivot_index - 1, depth + 1)
        _quick_sort_verbose_helper(arr, pivot_index + 1, high, depth + 1)


def _partition_verbose(arr, low, high, depth):
    """Partition function with verbose output."""
    indent = "  " * depth
    pivot = arr[high]
    
    print(f"{indent}Partitioning with pivot: {pivot}")
    
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                print(f"{indent}  Swapping {arr[i]} and {arr[j]}")
                arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"{indent}  Placing pivot {pivot} at index {i + 1}")
    
    return i + 1


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [3, 6, 8, 10, 1, 2, 1],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [42],             # Single element
        [],               # Empty array
        [1, 1, 1, 1]      # All same elements
    ]
    
    print("QUICK SORT ALGORITHM DEMONSTRATION")
    print("=" * 50)
    
    for i, test_array in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        print(f"Input:  {test_array}")
        sorted_array = quick_sort(test_array)
        print(f"Output: {sorted_array}")
    
    print("\n" + "=" * 50)
    print("VERBOSE EXAMPLE:")
    print("=" * 50)
    
    # Demonstrate verbose version with a sample array
    sample_array = [64, 34, 25, 12, 22]
    quick_sort_verbose(sample_array)
