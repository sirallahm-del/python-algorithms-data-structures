"""
Bubble Sort Algorithm Implementation
===================================

Author: Sirallah
Date: December 2024
Description: Implementation of the bubble sort algorithm with detailed comments
             and complexity analysis.

Time Complexity: O(n²) in worst and average cases, O(n) in best case
Space Complexity: O(1) - in-place sorting algorithm
"""

def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    The bubble sort algorithm works by repeatedly stepping through the list,
    comparing adjacent elements and swapping them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
        
    Examples:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        
        >>> bubble_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if not arr:
        return arr
    
    n = len(arr)
    
    # Make a copy to avoid modifying the original array
    arr_copy = arr.copy()
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize algorithm - if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place (largest elements "bubble up")
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no two elements were swapped in inner loop, array is sorted
        if not swapped:
            break
    
    return arr_copy


def bubble_sort_verbose(arr):
    """
    Bubble sort with step-by-step output for educational purposes.
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    if not arr:
        return arr
    
    n = len(arr)
    arr_copy = arr.copy()
    
    print(f"Original array: {arr_copy}")
    print("-" * 40)
    
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                print(f"  Swapping {arr_copy[j]} and {arr_copy[j + 1]}")
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        print(f"  Array after pass {i + 1}: {arr_copy}")
        
        if not swapped:
            print("  No swaps needed - array is sorted!")
            break
    
    print("-" * 40)
    print(f"Final sorted array: {arr_copy}")
    return arr_copy


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [42],             # Single element
        []                # Empty array
    ]
    
    print("BUBBLE SORT ALGORITHM DEMONSTRATION")
    print("=" * 50)
    
    for i, test_array in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        print(f"Input:  {test_array}")
        sorted_array = bubble_sort(test_array)
        print(f"Output: {sorted_array}")
    
    print("\n" + "=" * 50)
    print("VERBOSE EXAMPLE:")
    print("=" * 50)
    
    # Demonstrate verbose version with a sample array
    sample_array = [64, 34, 25, 12, 22]
    bubble_sort_verbose(sample_array)
