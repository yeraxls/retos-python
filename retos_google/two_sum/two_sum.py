##Example 1:
nums1 = [2,7,11,15]
target1 = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:
nums2 = [3,2,4]
target2 = 6
#Output: [1,2]

#Example 3:
nums3 = [3,3]
target3 = 6
#Output: [0,1]

#Example 4:
nums4 = [3,3,6]
target4 = 15
#Output: result didnt found

def two_sum(numbers: list[int], target: int):
    result = "result didnt found"
    for i in range(len(numbers)):
        j_index = [j for j in range(i+1,len(numbers)) if numbers[i] + numbers[j] == target]
        if len(j_index) > 0:
            result = f"{i} - {j_index[0]}"
            break
    print(result)

if __name__ == "__main__":
    two_sum(nums1, target1)
    two_sum(nums2, target2)
    two_sum(nums3, target3)
    two_sum(nums4, target4)