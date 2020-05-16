def two_sum(arr, target):
    """given an arr and a target, return indices of two elements that add up to
    target.

    guaranteed to have a solution."""
    elements_dict = {}

    for x in range(len(arr)):
        elements_dict[arr[x]] = x

    for x in range(len(arr)):
        if target - arr[x] in elements_dict and elements_dict[target-arr[x]] != x:
            return [arr[x], target-arr[x]]

def best_time_to_buy_and_sell_stock(arr):
    """the intuition behind this algorithm is that you want the min element on the left
    hand side and the max element on the right hand side. Such when u subtract,
    you get profit. The apporoach im thinking of is you keep a min variable keeping tracking
    of each new minimum. This is because whenever we find a value lower than our current_min,
    we have the possibility that there might be number to its right that
    gives us a greater profit."""

    min = arr[0]
    max_profit = 0

    for x in range(1, len(arr)):
        if arr[x] < min:
            min = arr[x]

        else:
            if arr[x] - min > max_profit:
                max_profit = arr[x] - min

    return max_profit


def three_sum_equality(arr1, arr2):
    arr1_element_count = {}
    arr_2_element_count = {}
    for x in range(3):
        if arr1[x] in arr1_element_count:
            arr1_element_count[arr1[x]] += 1

        else:
            arr1_element_count[arr1[x]] = 1

        if arr2[x] in arr_2_element_count:
            arr_2_element_count[arr2[x]] += 1

        else:
            arr_2_element_count[arr2[x]] = 1

    return arr1_element_count == arr_2_element_count



def three_sum(arr):
    '''given an arr, return the indices of three indices that sum up to 0.

    the intuition behind this problem is that two sum finds TWO integers that add up to
    a value. 0 = X + Y + Z. If we have x fixed, we can do a check to find if there's
    two values that sum to 0-x.

    x + y + z = 0

    y + z = 0-x.'''
    solutions = []
    for x in range(len(arr)):
        two_sum_result = two_sum(arr[:x] + arr[x+1:], 0-arr[x])

        if two_sum_result:
            list_of_values = [arr[x], two_sum_result[0], two_sum_result[1]]

            unique = True

            for sets in solutions:
                if three_sum_equality(list_of_values, sets):
                    unique = False
            if unique:
                solutions.append(list_of_values)

    return solutions


def product_of_array_except_self(arr):
    """given an array arr, return an output array such that output[i] = product of all
    elements in arr except ar[i].

    The simple O(N) time approach would be to use division.

    """

    total_product = 1
    output = []
    for elements in arr:
        total_product *= elements

    for elements in arr:
        output.append(total_product/elements)

    return output


def product_of_array_without_divison(arr):
    """
    same q as above but try to do it without division.
    This approach calculates the product for each element to its left, and to its right.
    and then calculates the overall product without that element.
    """
    left_products = []
    cur_product = 1
    last_value = 1
    for x in range(len(arr)):
        new_prod = cur_product*last_value
        left_products.append(new_prod)
        last_value = arr[x]
        cur_product = new_prod
    right_products= [0]*len(arr)
    cur_product = 1
    last_value = 1
    for x in range(len(arr)-1,-1,-1):
        new_prod = cur_product*last_value
        right_products[x] = new_prod
        last_value = arr[x]
        cur_product = new_prod

    output = []
    for x in range(len(arr)):
        output.append(left_products[x] * right_products[x])

    return output

def odd_even(arr):
    """partition the arr in such a way such that all even elements come before alll
    the odd elements."""

    curr_even = 0
    last_odd = len(arr)-1

    while curr_even < last_odd:
        if arr[curr_even] % 2 != 0:
            arr[curr_even], arr[last_odd] = arr[last_odd], arr[curr_even]
            last_odd -= 1

        else:
            curr_even += 1

def dutch_partitioning_problem(arr, pivot):
    """partition the array such that all elements less than the pivot appear first, followed
    by elements equaling the pivot and then finally elements greater than pivot.
    """

    # first pass, bring all small elements to front..

    small = 0

    for x in range(len(arr)):
        if arr[x] < pivot:
            arr[x], arr[small] = arr[small],arr[x]
            small += 1

    larger = l
    for x in range(len(arr)-1,-1,-1):
        if arr[x] < pivot:
            break

        elif arr[x] > pivot:
            arr[x], arr[larger] = arr[larger], arr[x]
            larger -=1

def array_partition_1(arr):
    """given an array of 2n elements, find the maximum sum that can found by summing up
    min (a, b) such that a and b are elements of arr."""

    sorted_arr = sorted(arr)
    sum = 0
    for x in range(0, len(arr), 2):
        sum += sorted_arr[x]

    return sum

def majority_element(arr):
    elements_counter = {}

    for elements in arr:
        if elements in elements_counter:
            elements_counter[elements] += 1

        else:
            elements_counter[elements] = 1


    max_key = None
    max_counter = None

    for elements in arr:
        if max_key:
            if elements_counter[elements] > max_counter:
                max_counter = elements_counter[elements]
                max_key = elements

        else:
            max_key = elements
            max_counter = elements_counter[elements]

    return max_key

def plus_one(arr):
    """given an arr of integers, add 1 to it."""

    output_reversed = []
    carried = 1
    for x in range(len(arr)-1,-1,-1):
        sum_number = arr[x] + carried

        if sum_number > 10:
            carried = 1
            output_reversed.append(sum_number % 10)

        else:
            carried = 0
            output_reversed.append(sum_number)
    output = []
    for x in range(len(output_reversed)-1,-1,-1):
        output.append(output_reversed[x])

    return output

def merge_two_sorted_arrays(arr1, arr2):
    arr1_counter = 0
    arr2_counter = 0
    merged = []
    while arr1_counter < len(arr1) and arr2_counter < len(arr2):
        if arr1[arr1_counter] < arr2[arr2_counter]:
            merged.append(arr1[arr1_counter])
            arr1_counter += 1

        else:
            merged.append(arr2[arr2_counter])
            arr2_counter += 1

    return merged + arr1[arr1_counter:] + arr2[arr2_counter:]

print(merge_two_sorted_arrays([7,8,9,10],[1,4,11,12]))