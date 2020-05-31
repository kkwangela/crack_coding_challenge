#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:57:06 2020

@author: kewang
"""

def search(nums, target):
    #直接二分法
    #mid == target,返回mid
    #mid != target:
    #1. nums[l] <= nums[mid]:左半边递增，说明旋转点在右侧
    #    1.1 target在递增部分
    #    1.2 target不在递增部分
    #2. 右半边递增，说明旋转点在左侧
    #    2.1 target 在递增部分
    #    2.2 target不在递增部分
    
    if len(nums) == 0: return -1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r)//2
        
        if nums[mid] == target:
            return mid
        elif nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return l if nums[l] == target else -1
              
if __name__ == "__main__":
    nums = [3,5,1,2,2]
    print(search(nums,2))
                          
        
    