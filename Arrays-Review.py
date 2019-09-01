
## Question: find a pair in array whose sum is equal to a given number
'''
For exaple: <1,2,4,9,3,10> , target = 13

Naive: O(n^2)

Other would be to sort the number
< 1, 2, 3, 4, 9> and binary search the number: so nlgn worst time

Other would be to use pointer in the array one from start and other from the end

Finally, it would be to use a hashtable and look for it in the set if its present or not.

'''

## Question: given a sorted array of size n, find an element which occurs more than n/2 times

'''
For example: <1, 3, 3, 3, 3, 3, 5, 6>

naive method: check each element; O(N^2) not using sorting
using sorting: uses O(N) starts at first; then moves second pointer until there is a match; records the value and max count
once mismatch, resets the i to be the mismatch and j as one after i.
Loop stops when j >= length

Time: O(n)

Constant time algo:
    Look at middle element in a sorted array; and just return that
'''

## Question: Find maximum difference between an array such that larger element appears after the smaller

'''
for example: < 3, 30, 300, 290, 1200, 1, 20>
O(n) approach; same as stock question
'''

## Question: Find the element appearing odd number of times in an array, given exactly one element does so

'''
Naive approach: sort, done in O(nlgn)
Hash set approach: O(n) time, O(n) space

or 
- insert if element is found, delete if its found again, insert if found

return any element from the set.

 given exactly one element does so; we can create sum
 5,5,5,5,2
 22



'''