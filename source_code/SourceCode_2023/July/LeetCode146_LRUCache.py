# -*-coding: utf-8-*-
# @Time  :2023/7/10 14:27
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode146_LRUCache.py


'''
[146. LRU Cache]
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''
import collections


class Node:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRUCacheV1:

    def __init__(self, capacity: int):
        self.hash = {}
        self.head = None
        self.end = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.hash.get(key)
        if not node:
            return -1
        self.refresh(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.hash.get(key)
        if not node:
            if len(self.hash) >= self.capacity:
                old_key = self.remove_node(self.head)
                self.hash.pop(old_key)
            node = Node(key, value)
            self.add_node(node)
            self.hash[key] = node
        else:
            node.val = value
            self.refresh(node)

    def refresh(self, node):
        if self.end == node:
            return

        self.remove_node(node)
        self.add_node(node)

    def remove_node(self, node):
        if node == self.head and node == self.end:
            self.head = None
            self.end = None
        elif node == self.head:
            self.head = self.head.next
            self.head.pre = None
        elif node == self.end:
            self.end = self.end.pre
            self.end.next = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre

        return node.key

    def add_node(self, node):
        if self.end:
            self.end.next = node
            node.pre = self.end
            node.next = None
        self.end = node
        if not self.head:
            self.head = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCachev2(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]



    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

