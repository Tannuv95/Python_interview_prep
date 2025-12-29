
---

## 🐍 `Day_01/solution.py`

```python
"""
Day 1: Intersection of Two Lists
"""

# --------------------------------------------------
# Approach 1: Brute Force using loop
# Time Complexity: O(N * M)
# Space Complexity: O(K)
# --------------------------------------------------

def intersection_bruteforce(a, b):
    intersection_list = []
    for value in a:
        if value in b:
            intersection_list.append(value)
    return intersection_list


# --------------------------------------------------
# Approach 2: Using List Comprehension
# Time Complexity: O(N * M)
# Space Complexity: O(K)
# --------------------------------------------------

def intersection_list_comprehension(a, b):
    return [value for value in a if value in b]


# --------------------------------------------------
# Approach 3: Optimized using Sets (Recommended)
# Time Complexity: O(min(N, M))
# Space Complexity: O(N + M)
# --------------------------------------------------

def intersection_optimized(a, b):
    set_a = set(a)
    set_b = set(b)

    if len(set_a) < len(set_b):
        return [x for x in set_a if x in set_b]
    else:
        return [x for x in set_b if x in set_a]


# --------------------------------------------------
# Example Usage
# --------------------------------------------------

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = [0, 1, 3, 7]

    print("Brute Force:", intersection_bruteforce(A, B))
    print("List Comprehension:", intersection_list_comprehension(A, B))
    print("Optimized:", intersection_optimized(A, B))
