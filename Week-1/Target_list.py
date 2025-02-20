def get_subsets(nums, target):
    n = len(nums)
    result = []
    for i in range(1, 1 << n):  # Loop through all subset combinations
        subset = [nums[j] for j in range(n) if (i & (1 << j)) > 0]
        if sum(subset) == target:
            result.append(subset)
    return result

# Input list and target sum
my_list = [-1, 0, 1, 2, -1, -4]
target = 3

# Get subsets that sum to the target
bitwise_result = get_subsets(my_list, target)

# Print the result
print(bitwise_result)
