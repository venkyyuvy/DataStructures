
Arrays and strings
1. Isunique:
# array
Use a 26 length array to store the presence of each character. when we see a character which is already populated with true in our array, return false
Time: O(n)
space: O(1) - we take up only 26 characters irrespective of the input size.

# hash set
store the visited character and return false if we encounter an array which was already visited.

# bit 
Reduces the space complexity by a factor of 8. using single int as a bit vector.

if the number of character is less than 126, we use single int for it. Each bit representing a character. 
checker =0
for <ch in string >:
val = ord(ch)
if (checker & 1 << val) > 0:
return False
checker |= 1 << val

# no extra space:
sort (N logN) and then compare each character with its previous character. 

2. check permutation:
# Sorting approach
sort both the strings and then compare each character in both strings

# counts approach
Take count of each characters in both the string, if the counts match, then they are valid palindromes.

madam - m: 2, a:2, d:1
maadm - m: 2, a:2, d:1

more optimization:
take the count for the first string.
iterate through the second string. Decrement the counter when we see the corresponding character. 
whenever any count goes negative, we can return False.

3.URLify:
count the number of spaces, output string length will be equal to the true string length + 2 * number of space. [ one space = 3 characters]

start from the end of the true string and copy the character if it's not a space, add '02%' if its a space.

4. Palindrome permutation:
a binary for each character (set to False initially), when see a character flips its corresponding binary	variable. True represent odd number of counts.

keep a var for tracking a odd count reached. if one more odd count is reached at the end of the string, we return True, if odd counts is <=1.

bit operation:

check_exactly_one_bit_set
Condition to check only one in a bit vector:
subtract 1 and then adding with the original number should return zero.
00010000 - 1 = 00001111
00010000 & 00001111 = 0
(bitVector & (bitVector - 1)) == 0;

toggle bit vector for a given index:

mask = 1 << index

if bit_vector & mask == 0:
bit_vector |= mask
else:
bit_vector &= ~mask

return true if bit_vector ==0 | check_exactly_one_bit_set(bit_vector)
5.One away

Addition and Deletion are the same. It is the just the way, we look the order of the two given strings

keep the larger string as s1 and smaller string as s2.

iterate through the both the strings as long as they are having same characters.
when a char mismatch occurs, move the pointer in the long string and set the missing_ele as True. 
when we see another mismatch, return False.

Alteration:
Both strings have to be in the same length.
iterate through both the strings with two pointers. when mismatch occurs, check if the pointers are at the same index in both the string, if so continue otherwise return False. 
if we are able to complete the parsing, return True. 

6. String compression:

Iterate from the second char of the string, set the counter as 1.
if the current char is the same as previous char, increase the counter.
else, add the previous_char + str(counter) to the output. set the counter to 1.
whenever the size the of the output gets larger than the input string, return the original string.
add the final non repeating char to the output

7. rotate matrix:
there are n//2 layer, for each layer
first= layer;
last= n - 1 - layer;
for i in range(first, last)

swap 

temp <- top
top <-left (matrix[layer][i] = matrix[-i - 1][layer])
left <- bottom (matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1])
bottom <- right
right  <- temp





8 zero matrix:
iterate through each element in the given matrix ( M *N). if an element's value is zero, add the corresponding row and column to the tracker that we maintain. 

time: O(m*n)
space: O (m +n)

9 substring:
s1 = original string (waterbottle)
s2 = rotated string (terbottlewa)
isSubstring(slsl, s2)

waterbottlewaterbottle
    —------------

if substring can search in O(A+ B) if strings are of size A and B. 

then, Time is O(N), space is O(1).

10 container with maximum water:
brute force:

compute area for all the pairs and compute the max

two pointer:
start both the pointers at the extremes and count the max
make both the pointers walk towards center;
move left if left is less than the right pointer's value
else move the right pointer.

PROOF
 encode and decode list of strings

1. non ascii character 
	after utf-8 encoding, delimiter with ord(256) 
return ord(256) if input is []
2. 4 bytes to denote the size of the string and then append the string.

Linkedlist
1. Remove Dup:

Having a hash table and check if the value is already present in the hash table.

# with no buffer

O(n^2) and constant space.
Outer loop: current node
Inner loop: copy current node to runner; look FORWARD (.next)and drop them if they are equal to current value

2. return k to last:
	when n > K, 
		Two pointers: one is last element of our parser and other is k elements before it.

# with recursion
O(n)
call the next node till you reach the tail 
Have a non-local counter and increase it by one. If counter is equal to k, return the node.

3. Delete the middle node, given access to that node only.
copy the value of next node and overwrite it to the current node.
point the node, which is next to next node as the next node for current node.

4. Partition
	if the val of current node is less than x, leave it
else, cpy that to a new ll. 
Finally merge both the ll. 

Identify the tail node. 
if the val of current node is less than x, then move it to the head.
else, move it to the tail. 

5. sum two ll
set overflow as 0
add each corresponding node ( or the ll value that has a value) and take the remainder as the value for the result ll. Carry the quotient to the next iteration. 
 If there are no digits to parse and overflow is non zero, then add a new node with overflow value.

# followup - when the vals are in forward order

we need to align the digits by adding zeros in the front.

6. Palindrome
# with additional memory 

using stack,

use runner technique to find the middle and last node. Push all the nodes upto to middle node in a stack. if the len of the ll is odd, then drop the middle node. 

Then iteratively compare the next node of middle with the items in the stack 
# with space O(1)
for constant space:
find the middle element,
chop it into left and right
reverse right
compare left and right


7. Intersection
find the length of both the list and last element
if the last element is not same, then return False
on the longer ll, advance the pointer by the difference of the length
Now traverse, both the linked list until the pointers are the same

8. loop/ cycle:
Floyd's tortoise and hare pointer solution
find the intersection, if there are any
then have two pointers, one from the start of the linked list and other from the intersection point. Where the two pointers meet is the start of the loop
 

2. Stack/queue
1. three in one
split the available space into three ( one for each stack). 
Have a counter for each stack, on many values are present in each stack
Return corresponding error for wrong stack ids or stack full.

2. stack min 
have an additional stack called stack_min while instantiating the stack
whenever we add a new element, we update the min var.  

3. stack of plates
individual stacks will have a max size. 
when we add a new value, if the current stack is full , add a new one.
when poping, take the last value from the last stack. if  the last stack is empty, remove it.
4. Queue via stacks:
Basic difference is the LIFO - LILO. Use two stacks.
keep adding the elements into the newest stack, when we get a push request. When we need to pop, unpack all items to the oldest stack. Then we can use the oldest stack for peek and pop until it becomes empty. 
When it becomes empty, again do the unpacking activity from newest to oldest stack.
5. sort stack
use a temp stack to unload the higher values items. Insert the particular item into the appropriate place and then put the items from the temp stack.
6. animal shelter:
Have  a linked list to connect between each animal (cat and dog). Each animal is a stack separately. 

Tree and graphs

Binary search tree
All left descendents <= n < all right descendents.This must be true for each node n.

Balanced trees doesn't mean that the trees are perfectly balanced. They are balanced enough to give logN complexity for searching and insertion. Example for balanced trees are AVL and Red-black trees.

Complete Binary Trees
A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last level. To the extent that the last level is filled, it is filled left to right.
Full Binary Trees
A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have only one child.
Perfect Binary Trees
A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes.

Binary Heaps ( Min heap and Max heap)

In a min heap, each node's value would be less than its descendants. Hence, root is the minimum value element in the tree.

log N time for insertion and pop the minimum value. 

Insert the value into the bottom right most  and then keep swapping the element with its parent when its is lower than its parent. 
after pop the top/ root element, take a val from the right bottom most one and put it in the root. Then swap it with a child whose value is less than our item value. 

Trie:

n-ary tree. Used for prefix /word validation.* represents complete words. A node in trie could have upto alphabets_size +1 number of children.
gives O(k) time complexity to check whether a given string is a valid prefix.

Graphs:
representing a graph
adjacency list
adjacency matrix

In a graph, there is no guarantee that we will be able to reach every node from other nodes.

Searching:

DFS:

we go to the depth first and then breadth. We finish one branch and then go to the other.

BFS:
we go to wide before going deep. We visit all the children before visiting their children.

For shortest path finding, BFS is generally a better approach than DFS. Eventually both will find the solution.

Bi-directional search:

we start from both the source and destination node. When there is a intersection, we found the path. Requires O(d/2) complexity if the path distance is d.


1. Routes between nodes:
BFS and keep track of visited node to avoid cycles.
2. Minimal tree:
Given a sorted array, the function finds the midpoint element and set it as root and call recursively the same function on the left and right side points separately. Each would return a tree. Those tree would be the left and right children of our main tree.

3. List of depth:
BFS.
list of linked of list where one ll for each depth.
if new depth is seen/ higher than current level, create a new linked list and add it to our output list

4. Check balanced:
Inefficient solution:
call depth calculation function on left and right children. If they differ only by one value then return True. We need to ensure that the children are also balanced on their own. so call is_balanced on left and right again. 
If we check the height and is_balanced condition sequentially, O ( N log N).


Efficient solution:
return both the isBalanced_condition and height of the node
Boundary conditions:
if left and right are None, return True, -1;
if either one is None, return False, 0
if both one is present, return  abs (left.height - right.height) < 1,  max from left and right tree size + 1.

To simplify from returning two values, we can use -inf as the value for false condition. 

Both time and space complexity is O(n).

5. Valid BST:
Every node on the left has to be less than the current node's value. Hence simply checking left.values < val < right.
recursive function
Get the min, max values from left and right side node.
return True if  node's value is greater than max of left node  and min of the right node.

Boundary condition:
if left node is None, check for the right node alone and vice versa.

6. Successor:
next node in the in-order successor

if n has right subtree
	return leftmost child of right subtree
else
	while n is a right child of n.parent
		n= n.parent
	return n.parent // this n is a left child of n.parent, hence has not been traversed.
7. Build order:
Topological sort

8. First common Ancestor:

9. BST sequence:

weave: 
all possible sequences without violating the order of the individual sequences.  
a = 1,2 ; b= 3, 4
weaved = [1,2,3,4], [1,3,2,4], [1.3, 4,2,],
	    [3,1,2,4], [3,1,4,2], [3,4,,1,2]
10. check subtree:
not space optimized: 
merkle encoding: hash the inorder traversal of the tree. O (n+m) space 

simpler alternate:
try to match with the right


11. Random node:
store the size of the tree in the class,
pick a random number between 0 and size of tree.

get the ith node by picking searching in the root.left if size of left is > i.
return node if i == size(root.left)
else search in the root.right for the index (i - size(root,left)

logN for balanced trees and log(depth of the tree) for unbalanced trees.
12. Path with sum
brute force:
computing all paths and theirs sums. increment the counter if the sum is equal to the target sum.

Optimized solution:

keep a running sum and increment it by node.value when we move forward
look up for runningsum - targetSum in the hash table. The value there indicates the total number. set totalPaths to this value
if runningSum = targetsum, then there's one additional path that starts at the root. increment totalPaths
add runningSum to the hash table (incre. if it is already there)
recurse left and right
decrement the value of runningSum in the hash table. 
return totalPaths

 
13. valid tree:
# basic graph theory approach
all nodes have to be connected. 
no cycles in the graph.
for every undirected edge in the input, add two edges in our adjacency matrix a-b and b-a. 

Do a DFS with a parent map.
if a neighbour is the parent of the current node, then skip (continue) it. 
if the neighbour is still present in the parent map; as a child of different node, then return False. <there shouldn't be two parents for a node>
check whether parent map size is n and return True.



# advanced graph theory based approach
If the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!
for every undirected edge in the input, add two edges in our adjacency matrix a-b and b-a. 

Do a DFS with a visited set. if encountered a visited node, simply skip it. 

After finishing dfs, size of the visited set has to be n. 
# Union find approach:
when we are trying to union two nodes which are already connected, there is a cycle. < parent of both nodes are same before we apply the union operation >

O(n. alpha(n)) ~= O(N)
alpha(n) will never go above 4. 

14. Alien dictionary:
look at each pair of words
move forward until there is not matching character (c!= d:
increment the in_degree of `d`
adj_list[c].add(d)
move to the next pair of words


populate the queue with nodes with zero in_degree. 
while queue:
node = queue.popleft() # BFS
output.append(node)
reduce the in_degree of all the neighbors
if the in_degree is zero, add it to the queue.

if length of the output is not equal to the in_degree then return ""
otherise, return the output as a single string.

time: O(c); c is the number of characters in all the words given.
BFS: O(V+ E)
A node is visited once, when all of its edges are visited.
Typically it is O(V) for BFS, because we visit a node if we visit one of it's edge.

If there are U nodes, lower bound on the number of edges is N-1 (where N is the number of words in the input) and upper bound is U^2.

hence, the complexity becomes O(U + min(U^2, N))






 
Sorting and searching

1. Merge sorted arrays:
pointer (p1) at the end of the actual nums1 and second read pointer (p2) at the end of the nums2

Write pointer (p) is at the end of the nums1.

Start writing the max value (by comparing the p1 and p2 and check p1 > 0 - by then all the nums1 values are moved) to the p pointer's place. decrement the corresponding read pointer p1 or p2. 


Once p2 reaches zero, stop. because rest of the nums1 values are already sorted / in-place

time: O(n+m)
space: O(1)


2. Group anagrams:

sort each of the strings. keep a hash table with a key as the sorted string and values a list of anagrams.
time: O(N K log K) ; k is the size of the string and N is the number of strings in the array.
space: O(NK)

Optimized solution:

create the char count for each string (takes O(K) ; linear time complexity). then key keep the tuple of counts as the key and the values as list of anagrams.

time and space: O(NK)


3. Search in a rotated array:

find the inflection point by binary search and then search the target in the appropriate section of the splitted array.

Finding inflection point
    while left <= right
find the middle point 
check whether the next point is greater than the middle, return middle.
else
if left is less than middle
left = middle +1
else
right = middle -1




optimized solution:

Find the which half of the solution is sorted, then decide whether that half would contain the target value or not. search in the appropriate half (recrusive call).

Itervative optimized solution:
find the middle value,
    if middle == target:
        return middle_index
    if middle is less than left
        if target is greater than left and less than middle 
             right = middle - 1
        else:
             left = middle + 1
    else:
         if target is greater than middle and less than right
             left = middle + 1
         else:
             right = middle + 1 
        
return -1



if one half of the array is same; example: 2,2,2,3,4,2


4. Sorted search, no size:

find the size of the array, by doubling the index each time till we get a value greater than target as the result. we can find this index of the array in log N.

then binary search in index/2, index 
	if (middle > value I I middle == -1), search in the right, else search in the left
7.Missing number:
1. sorting
then checking if first and last digit is 0 and n respectively.  search linearly to check whether the val and index are same or not. 

2. hash table
put all the values in the hash, then check vals from 0 to n to be present in the hash set or not.

3. XoR
Xor of index and the value for all the elements in the array.

4. Gauss:
compare expected (n(n+1)/2) and actual sum
return the difference.
8. Find duplicates:
9. sorted matrix search
10. Kth largest element in a stream:

heapify the given nums, then trim  the heap to size of k
when a new element is added, add it to the heap, then if heap size is greater than k, trim it back to size k. 
return the first element in our heap.

O(N log N) + m log K

k can be 1, so N elements needs to be removed and each can take log N time. 
M element can be added in the stream. each take 2logK ( one to add and other to remove the smaller one).

space O(N)
initial heap was created with array of size N.
11. peak and valley or wiggle sort

1. Sort the elements and then swap the pairs from  1 to n-1.
2. Have a sliding window of size 2, compare the two elements, if they are not in order then swap. keep altering the less condition for every step. 

less, not less, less, not less, etc..


Dynamic programming
1. Triple step:
countWays(n-1) + countWays(n-2) + countWays(n-3)

when n==0, countWays =1
hash table / memorization

2. Robot in a Grid:

return 0 if the start node has an obstacle.
set the number of ways to reach the start node as 1.
For the left and top borders, look at the current node and previous node to decide whether it can be used or not. 

for the rest of the cells (double `for` loop), starting from cell (1,1)
if val is not 0, 
	add the previous row and previous col value from the same table.
else set the value as 0 (since it a block, we can't reach this cell at all)

return the value of the right bottom most cell value > 0.

# recrusive solution

start from bottom right corner. look at the previous row and column, where there is a path exist or not. 
Use memoization for the paths to return whether the path exist or not. 
keep track of failed points too. 

inputs for is_path_memoized(maze, row, col-1, path, failed_points)

return true if we reached origin or left or above node has a valid path.

3. Magic Index:
Element where index is equal to the element value in an array, which is sorted.

check the middle element. for example if it is ix = 5 and val is 3. Then the magic index has to be on the right. Because when we go to the left, both the index and val has to be reduced because the values are distinct. 

# # condition is index > val, then search in the right side. recurse # #

if duplicates are allowed in the array:
The general pattern is that we compare midIndex and midValue for equality first. Then, if they are not equal, we recursively search the left and right sides as follows:
* Left side: search indices start through Math. min(midlndex - 1, midValue).
* Right side: search indices Math. max(midlndex + 1, midValue) through end.

4. Power set:
generate_from_base(element, base):
return [base] + [element]+ [set.append(element) for set in base]


combinatorics:
bit (ref)
n_th_bit = 1 << n gives 1000 (for 8)
bin (i | n_th_bit)[3:]
gives 000, 001, 010, etc.

or
for i in range(2**n, 2**(n + 1)):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i)[3:]

based on bit mask, generate subset
`[nums[j] for j in range(n) if bitmask[j] == '1']`

complexity : O (N * 2^N)

<backtracking based solution>
5. Recursive multiply:
a*b  = adding a,  b times. 
set a as the bigger number and b as the smaller number
we can a, b/2 times and then double it. recursively do it. For dividing (b/2), let us use bit shifting b >> 1.

for odd numbers finally add the bigger number again.

6. Towers of Hanio:
7. permutation without duplicates:

8. Permutation with duplicates:

9. Generate parentheses:

1. brute force:
generate all 2^N methods.
remove the invalide parenthesis.

2. backtracking:
generate a solution when it is valid.
validity condition: left < n, add '(' | right < left add ')'

n - catalan  number : 1/ n+1 * 2N C N = 4^N / n sqrt(n) 

time: 4^N /  sqrt(n) 
space: 4^N /  sqrt(n) 

3. closure number:
for c in range (n):
	for left in param_sequ(c):
for right in param_sequence(N-1-c):
ans.append(f('({}){}'.format(left , right))


10. Flood fill:

DFS, if cell's val is equal to old color, replace it with the new color. otherwise return false

11. Coin change:
set dp for all amount values as 0.
        	combination for 0 type of coins and 0 amount value is 1
        then, for every coin and every amount value from coin to amount.
dp[x] += dp[x - coin]

12. N-Queens:

All cells in  a diagonal will have the same row-col value.
Similarly, each cell in an anti-diagonal will have the same value row + column.
backtracking:

if row = n, build the solution and exit. 
placing the queens row by row and having a set for tracking the already occupied column, diagonal and anti-diagonal. diagonal = row-col, anti-diagonal = row+col.

iter through each column 
If column is not present in the three sets that we track. add it to the current solution (mark it as Q) and then do backtracking with row +1, updated state (with Q marking), updated three sets. 
Revert the changes to the sets, mark this column as '.' and then go on with the next iteration.
For rest of invalid columns simply go on with the next iteration. 

time (N!)
N * (N-2) * (N-4) ~= N!
for each solution, we need N^2 time to build the solution. 
space (N^2)
three sets that we manage are linear space with the respect to size of the N- queen problem
N^2 is used to track the board state.
13. stack of boxes
Sort the boxes dimensions internally and then all the boxes externally.
14. Boolean evaluation
Catalian number


15. Palindromic substrings:
single characters are palidromes 
double char strings are Palindrome if they are same.

dp (i, j) = true if dp(i+1, j-1) is True and s_i == s_j
false otherwise


time and space complexity O(N^2) ( N C 2 = N(N-1)/2)

# better space complexity solution:

* for odd length palindromes
choose every location as the centre of the palindrome, then expand outside until it satisfies the palindrome condn explained above.

* for even length palindromes
choose every pair. 

N - single char centers and N-1 -> consecutive character pair as centers.
Each center can expand upto the length of the string - which can take order N.

time: N * (2N -1) = O(N^2)

16. Word Break:

Brute force solution:
For every location
return True - if the characters parsed so far are in the dictionary and recursion output for rest of the string. 

Time: 2^ N
space: O(n) - recrusion

## Using memoization:
lru_cache - O(n^3)

## BFS:
search for a word by moving forward til the end and then add the index to the queue. 
if index is already visited `continue`.
if index == end, return True.

## Dp

i in range (n + 1)
j in range (i)
if dp[j] and s[j:i] in word_set:
dp[i] = True
break
return dp[len(s)]

17. Number of decodings:
with lru_cache

        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

Time and space complexity: O(n)

18. Jump game

bad and good nodes. 
Last node is a good node.

Intervals:
1. Meeting rooms:

Overlap condition: Max of starting time is less than the minimum of the end timing.

# brute force 
compare all pairs of intervals from the given list
# optimal
sort the intervals and then check whether current meeting ends before the next meeting starts.

2. Meeting rooms II:

sort the intervals using the start time.
min heap to track the earliest time the existing meetings will finish. heap contains the end times. 

if min end time in the heap is less than the new meeting start time, then pop that element from the heap.

return heap size.

# chronological order:

keep two sorted list seperately - one for start time and other for end time.
two pointers - one for the start list and another for end list

remove a used_room if the start pointer is less than the end pointer.

always, add one to used_room and increment the start pointer.

return the number of used_rooms

3. Merge meetings:

first for the intervals
If output is empty or current_end is less than the new interval - append it to the output.
else update the current_end, which max (current_end, new interval end).

Time O(NlogN)
Space (logN) for in-place sorting or O(N) for storing the sort output in new variable.

2. graph:

create a graph and connect two components if they have a overlap
overlap ( a start before b ends or b starts before a ends)

start with a random node and iterate through all the nodes. keep a track of visited nodes.
for each node do a dfs and create a list of connected components

Merge the connected components - start is min of all interval starts and end is max of all interval end timing.



Assorted:

Place an image:

canvas has 1/0 representing that the cell is free or not. Image is of size w, h.

identify the location at which the image can be placed and return the left top location of the image in the canvas.

start from the right, compute the wide cells as 1/0 and move towards the right. Keep track of how many empty cells have been seen so far.  same way  for long cells. 



Hard:
1. Add without plus:
  while b !=0:
sum_ = a ^ b; add without carry 
carry = a& b << 1 # add only the carry 
# & does the bit wise addition; not binary addition

a = sum_
b = carry 
    return a
2. shuffle array:
walk through the elements of an array. Randomly swap with rand(0, i) th element.

3. Random set:
copy m elements from the initial array of size n.
for i in range(n):
k = rand(0,i)
if k <m, swap k with i
4. Missing number:
if a number is represent in its binary form, the size of the bit would be equal to log n.
Hence the guass solution would N logN.

say, there are n numbers in the list
In the least significant bit, 
count the number of 1s and 0s.
if n is odd, count of 1 is greater than 0s by 1,
if n is even, count of 1 should be 0s by 1, 

If n is odd, missing number is odd; then count of 0s is greater than 1 because a 1 is removed. 
similary 3 more conditions/alternatives like this.


5. Letter and numbers:
     a 1 a a a 1 I a 1 1 a 1 a 
#a 1 1 2 3 4 4 I 5 5 5 6 6 7
#1 0 1 1 1 1 2 I 2 3 4 4 5 5
4-2 is equal to 7-5
Difference is equal.
task is to find the same value in the difference/delta array which is farthest apart.
Use hash and keep track of the max diff seen so far (i, j index for the max distance). 

6. Count number of 2s:
if x[d] > 2: count2slnRangeAtDigit(x, d)= 
let y = round up to nearest 10^d+i
 return y / 10

7. Baby names
create a Union find DS with the pairs provided

for every name in original list of names:
find name's  parent
result[parent] += count(name)

8. circus tower:
9. Kth multiple:
10. Majority element:
11. word distance
12. binode to doubly linked list
13. Respace
14. Smallest k
15. Longest Word
16. Masseuse
17. Multi search
18. Shortest supersequence
19. missing two numbers - use products
20. continuous median / Find median from data stream:

Two Heaps:
one to hold smaller half of the numbers
other to hold the larger half of the numbers

Complexity Analysis
Time :O(5⋅log⁡n)+O(1)≈O(logn)
At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about O(log⁡n) time. Finding the median takes constant 
Space: O(n)
Linear space to hold input in containers.
21. Volume of histogram:
Tallest bar split the water into left and right. It has no impact on the volume of the water that can be filled.

can pre-compute the compute the max from left and right. 

our algorithm now runs in a few simple steps:
1. Sweep left to right,tracking the max height you've seen and setting left max.
2. Sweep right to left,tracking the maxheight you've seen and setting right max.
3. Sweep across the histogram,computing the minimum of the left max and right max for each index.
4. Sweep across the histogram, computing the delta between each minimum and the bar. Sum these deltas.

22. Word Transformer
23. Max square matrix:
24. Max submatrix
25. Word rectangle
26. sparse similarity
2. LFU cache:

capacity

use_counter: 

put(
—--------------------------------------------------------------

Moderate

1. swap two numbers without temp. variable:


A = A + B

B = A - B 

A = A - B
—---------------
x = x^y
y = x^y
x=x^y
—
2. Word Frequencies:
 Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?

O(N); counter

dictionary / hash table
> sorting + binary search 
3. Intersection: 
Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any.


—--------------------------

Only way to find if two line intersect or not is to find out if these two lines are parallel.

X1,y1, x2,y2

A1,b1,a2,b2

Let point of intersection = x,y

Y2 - y1/ x2-x1 = y2-y/x2-x

b2 - b1/ a2-a1 = b2-y/a2-x
4 Tic Tac Win:
 Design an algorithm to figure out if someone has won a game of tic-tac-toe.

check for  each column, row; diagonal and anti-diagonal. 

5. Factorial Zeros:
When the number has  a factor of  10 (5*2), then there will be zero in the output of factorial.

counts_of_5, by recursively dividing it by 5 and increasing a counter every time.
5-> 1, 25 -> 5

agg the counts from counts_of_5(range(2, n+1))

or directly count the number of 5s goes into each number

for (i =5, num/i >0, i*5)
count += num/ i 

6.smallest difference
a - m elemnts
b - n elements
Brute force:
compute the difference for every pair and then return min difference 
complexity (m*n)
 
optimized solution:

sort both the arrays
two pointers at the start of both the array

while p1 < m and p2 <n:
min_ = min(min_, abs(arr1[p1] - arr2[p2]))
if arr1[p1] <arr2[p2]:
p1 ++
else:
p2 ++

return min_

7. English int
Thrres = [Billiions, millions, thousands, reset]

while n > 0
sub_n %1000
 n //= 1000

8. Operations

9.Living people:


Optimal
sort both the birth and death arrays

have two pointers
if val at birth index is less than or equal to death index:
increment current_alive
update the max_alive and max_alive_year
move the birth index
else
 decrement the current_alive
move the death_index

time: (P logP ) - P is the number of people.

More optimal (may be)
have a hash map or array for the population_deltas
iterate through each people:
   update the corresponding year counter.
   increment on the birth year 
  decrement on the death year + 1

loop through the population_deltas
currently_alive += deltas[year_i]
update the max_alive and max_alive_year accordingly.

complexity O(R+P) - range and number of people size
10. 
11. Diving Board
Two options at each step - shorter and longer planks.
Recursive solution:
Initialize a hash total_solutions
set initial total_length = 0
with (k-1, length+shorter)
with (k-1, length+longer)
if k==0:
hash.add(length)

Memoization:	
key is k_length
if visited.contains(key)
return;
Optimal solution:
Binomial distribution
k = n = 7
n_short in range(0, k)
n_long = k -n_short
length = n_short * shorter + n_long * longer
12. XML encoding
13.bisect squares
14.Best Line

15. Master mind:

RGBY
GGRR

first pass to remove items from both strings for hits.
count each of the four characters in rest of the string in actual solution and guess

find the min of both arrays(element wise) and then sum it.

—------
Optimized

create an encoding for the colors
then put the frequency in an array

iterate through the guess string
code = encoding of the character at i
if code>0 frequency[code] > 0 & its not a hit
increment the pseudoHit counter
decrement the frequency[code]


16. subsort:
find the end of the left array which is sorted
find the start of the right arry which is sorted


17. contiguous sequence:
current sum goes less than zero, set it to zero.
keep a track of max_sum 
Iterate through all the elements.
 18.Pattern matching:
count the number of as, count the number of bs, starting point of b/end of a
the number of possibilites comes donw.
function for building a string from a pattern, with string for main and alternate

19. pond size:
BFS or DFS; return the size of the pond. keep track of the visited node by setting them to -1. 
time: O (n2)

20. T9
Brute force
recurse and create all possible strings using the 



—---
Heaps:

Top K frequent elements:
find Counter of given array.
heapify k largest elements (count.keys, count.get)

Merge K sorted Lists:
Patterns


Continuous sub arrays:
Maximum sum subarray
 Dynamic programming - kadane's algorithm
   current_subarray <- max between current value and current_subarray so far
   max_subarray <- max(max_subarray, current_subarray)

 Recursive algorithm:
   move from middle to right; find the best_left_sum
   move from middle to left; find the best_right_sum
```
    for i in range(mid - 1, left - 1, -1):
          curr += nums[i]
          best_left_sum = max(best_left_sum, curr)
```

find the best_combined_sum <- middle_val + best_left_sum + best_right_sum

ans: max(left_half , best_combined_sum, right_half)
   

Longest substring with ‘K’ distinct characters:
two pointers, 
move the right pointer, untill we include more than k characters. 
then move the left pointer to a location to remove the left most character.

To find the left most character:
keep a hash map for each element about its right most position visited so far.

time complexity (Nk) , because k is used to find the character with left most position. 
space O(k) for the hash map.

# better solution a ordered dict, which will reduce the complexity to N for time.
