def maxSubArraySum(a,size): 
    # Set max_so_far and curr_max to first element of the array
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far, curr_max) 
          
    return max_so_far 
  
# Testing maxSubArraySum:
a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print("Maximum contiguous sum is:" , maxSubArraySum(a,len(a))) 
