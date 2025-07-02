def longest_duplicates(nums):
    max_count = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count = count + 1
            if count > max_count:
                max_count = count
        else:
            count = 1

    return max_count

nums = [1, 3, 3, 7, 8, 8, 8, 20 ,20, 30]
print(longest_duplicates(nums))