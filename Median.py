class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        
        # Ensure nums1 is the smaller array or equal if m == n
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        # Binary search bounds for nums1
        low, high = 0, m
        total_length = (m + n + 1) // 2  # total number of elements in the left half
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = total_length - partition1
            
            # edge values (to handle empty partitions)
            nums1_left_max = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            nums1_right_min = float('inf') if partition1 == m else nums1[partition1]
            
            nums2_left_max = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            nums2_right_min = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partitioning
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Found the correct partitioning
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
                else:
                    return float(max(nums1_left_max, nums2_left_max))
            elif nums1_left_max > nums2_right_min:
                # We are too far on the right side of nums1, decrease partition1
                high = partition1 - 1
            else:
                # We are too far on the left side of nums1, increase partition1
                low = partition1 + 1
                
        # If we reach here, input arrays were not sorted
        raise ValueError("Input arrays are not sorted.")

# Example usage:
nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))  # Output: 2.5
