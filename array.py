class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Sorts the array using merge sort algorithm.
        """
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            result, i, j = [], 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)


# Example test
if _name_ == "_main_":
    print(Solution().sortArray([5,2,3,1]))  # [1,2,3,5]
    print(Solution().sortArray([5,1,1,2,0,0]))  # [0,0,1,1,2,5]