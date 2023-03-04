class Solution:
    def maximumCount(self, nums: List[int]) -> int:
            if nums[0] > 0 or nums[-1] < 0:
                return len(nums)

            p, n = 0, 0
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] < 0:
                    if nums[mid+1] > 0:
                        p, n = len(nums[mid+1:]), len(nums[:mid+1])
                        return max(p, n)
                    else:
                        start = mid + 1
                elif nums[mid] > 0:
                    if nums[mid-1]<0:
                        p, n = len(nums[mid:]), len(nums[:mid])
                        return max(p, n)
                    else:
                        end = mid - 1
                else:
                    left, right = mid, mid
                    while nums[left] == 0:
                            left -= 1

                    while nums[right] == 0:
                            right += 1

                    p, n = len(nums[right:]), len(nums[:left+1])
                    return max(p, n)

            return max(p, n)
