def any7(nums):
    if 7 in nums:
        print('True')
    else: 
        print('False')

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

