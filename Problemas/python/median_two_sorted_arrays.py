class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_arr = []
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2) :

            if i < len(nums1) and j < len(nums2):
                if nums1[i]< nums2[j]:
                    merged_arr.append(nums1[i])
                    i = i+1
                else:
                    merged_arr.append(nums2[j])
                    j=j+1
                
            elif i >= len(nums1) and j < len(nums2):
                merged_arr.append(nums2[j])
                j=j+1
            else :
                merged_arr.append(nums1[i])
                i=i+1

        if len(merged_arr)%2 == 1:
         
            return float(merged_arr[(int(len(merged_arr)/2) +1)-1])
        else:
            return  (float(merged_arr[int(len(merged_arr)/2)])  + float( merged_arr[int(len(merged_arr)/2)-1 ]))/2 

