def in_range(nums, lowest, highest):

    # YOUR CODE HERE
  for num in nums:
    if num in range(lowest,highest+1):
      print(f'{num} fits')

in_range([10, 20, 30, 40, 50], 15, 30)            
