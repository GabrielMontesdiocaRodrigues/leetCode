def jump(nums: list[int]) -> int:
    number_jumped = 0
    num_jumps = 0
    limit = len(nums) - 1
    while number_jumped != limit:

        if nums[number_jumped] > limit:
            return 1

        if nums[number_jumped] + nums[nums[number_jumped]] >= nums[number_jumped] + nums[number_jumped + 1]:
            jump_numbers = nums[number_jumped]
        else:
            jump_numbers = 1

        number_jumped += jump_numbers
        num_jumps += 1

    return num_jumps


print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))
print(jump([2, 1]))
