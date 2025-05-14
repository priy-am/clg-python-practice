#  44 WAP to find second largest element in a list without using inbuilt function
def find_second_largest(lst):
    largest = second_largest = float('-inf')
    if len(lst) < 2:
        return "List must contain at least two elements."
    
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return "There is no second largest element (all elements are same)."
    
    return second_largest



numbers = [10, 20, 4, 45, 99, 99]
print("Second largest element is:", find_second_largest(numbers))