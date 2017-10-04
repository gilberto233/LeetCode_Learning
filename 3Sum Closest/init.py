class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        for index in range(nums.__len__() - 2):
            startpoint, endpoint = index + 1, nums.__len__() - 1
            if index > 0 and (nums[index] == nums[index - 1]):
                continue

            while startpoint < endpoint:
                num_sum = nums[index] + nums[startpoint] + nums[endpoint]
                dis = num_sum - target

                if dis > 0:
                    endpoint -= 1
                elif dis < 0:
                    startpoint += 1
                else: return num_sum

                try:
                    if abs( dis ) < min_dis:
                        if dis > 0:
                            sign = 1
                        else:
                            sign = -1
                        min_dis = abs( dis )
                except:
                    min_dis = abs( dis )
                    if dis > 0:
                        sign = 1
                    else:
                        sign = -1

        return ( min_dis * sign + target )
