twoSum.py

Problem Description:
The twoSum function solves the problem of finding two numbers in a list that add up to a specific target value. Given an array of integers nums and an integer target, the function returns the indices of the two numbers whose sum equals the target.

Solution Explanation:
The solution employs a hashmap (prevMap) to store each number's index as it iterates through the list (nums). For each number, it calculates the difference needed to reach the target from the current number. If this difference exists in prevMap, it means a pair has been found, and the function returns their indices. If not, the current number and its index are added to prevMap. This approach ensures a time complexity of O(n), where n is the length of the input list nums.
