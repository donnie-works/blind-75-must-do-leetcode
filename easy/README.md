# Easy LeetCode Challenges

This folder contains solutions to easy LeetCode challenges. Each problem includes a title, description, relevant constraints, and an explanation of the solution.

## Index of Problems
1. Two Sum
217. Contains Duplicate

---

## Problem 1: Two Sum

### Description
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

### Solution Explanation
To solve the Two Sum problem, we can use a hash map to keep track of the numbers we have seen and their corresponding indices. As we iterate through the list, we calculate the difference between the target and the current number. If this difference is already in our hash map, it means we have found the two numbers that add up to the target. We then return their indices. If not, we add the current number and its index to the hash map and continue. This approach ensures a time complexity of O(n) since we only pass through the list once.

---

## Problem 217: Contains Duplicate

### Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Solution Explanation
To determine if the array contains any duplicates, we can use a set to keep track of the elements we have seen so far. As we iterate through the array, we check if the current number is already in the set. If it is, we return `true` because we have found a duplicate. If not, we add the number to the set and continue. If we finish iterating through the array without finding any duplicates, we return `false`. This method ensures a time complexity of O(n) since checking and adding elements in a set both have an average time complexity of O(1).

---

## How to Run the Solutions
1. Clone the repository.
2. Navigate to the `easy` subfolder.
3. Run the Python files using a Python interpreter.
   ```sh
   python3 Contains_Duplicate.py

