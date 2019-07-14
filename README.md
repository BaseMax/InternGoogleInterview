# Google Interview

# Google Intern Interview

## Google Interview Experience (For Software Engineering Intern)

Remember it was not my interview, But I love to solve it.

I have this has the chance to attend to design question or analyze in some big company such as EA.

### Round 1: Coding Sample

In this coding sample, I was given 90 minutes to answer 2 coding questions.

#### Question 1

Given a string A consisting of n characters and a string B consisting of m characters, write a function that will return the number of times A must be stated such that B is a substring of the repeated A. If B can never be a substring, return -1.

Example:

A = ‘abcd’

B = ‘cdabcdab’
The function should return 3 because after stating A 3 times, getting ‘abcdabcdabcd’, B is now a substring of A.

You can assume that n and m are integers in the range [1, 1000].

#### Question 2

Consider an undirected tree with N nodes, numbered from 1 to N. Each node has a label associated with it, which is an integer value. Different nodes can have the same label. Write a function that, given a zero indexed array A of length N, where A[j] is the label value of the (j + 1)-th node in the tree and a zero-indexed array E of length K = (N – 1) * 2 in which the edges of the tree are described, returns the length of the longest path such that all the nodes on that path have the same label. The length is the number of edges in that path.

Example:

A = [1, 1, 1, 2, 2]

E = [1, 2, 1, 3, 2, 4, 2, 5]

This tree is shown below. A node follows the form label, value.

```
----------1, 1

-----1, 2        1, 3

2, 4      2, 5
```

The function should return 2, because the longest path is 2->1->3, and there are 2 edges in this path.

Assume that 1 <= N <= 1000 and each element of the array A is an integer in the range [1, 1000000000].

 
