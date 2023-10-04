# Intuition
The intuition behind this approach is to calculate the product of all elements to the left of each element and the product of all elements to the right of each element separately. By combining these products, we can obtain the product of all elements except the element at the current index.

# Approach
We use two passes through the input array. In the first pass, we calculate the product of all elements to the left of each element and store it in an array called `answer`. In the second pass, we calculate the product of all elements to the right of each element and update `answer` accordingly. This way, each element in `answer` will contain the product of all elements except the element at that index.

# Complexity
- Time complexity: O(n) - We perform two passes through the array, each taking linear time in the length of the input array `nums`.
- Space complexity: O(1) - We use a constant amount of extra space, excluding the output array `answer`, which does not count towards the space complexity.