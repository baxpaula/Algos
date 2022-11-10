# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Example
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
def moveZeros(nums):
    newList = []
    secondList = []
    for i in range(len(nums)):
        if nums[i] == 0:
            newList.append(nums[i])
        elif nums[i] != 0:
            secondList.append(nums[i])
    res = secondList + newList
    return res
print(moveZeros([0,1,0,3,0,12]))

# Given an array of integers, find the sum of its elements.
# For example, if the array = [1,2,3] returns 6

def listSum(listInput):
    sum = 0
    for i in range(len(listInput)):
        sum += listInput[i]
    return sum
print(listSum([1,2,3]))

#reverse an array
# Example [1,2,3,4] returns [4,3,2,1]

def reverseList(listInput):
    for i in range(len(listInput)//2):
        temp = listInput[i]
        listInput[i] = listInput[-1-i]
        listInput[-1-i] = temp
    return listInput
print(reverseList([4,3,2,1]))

