#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self. cache = {}
        self.capacity = capacity
        self.LRU, self.MRU = Node(0, 0), Node(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        
    def insert(self, cur):
        cur_prev = self.MRU.prev
        cur_prev.next = cur
        self.MRU.prev = cur
        cur.next = self.MRU
        cur.prev = cur_prev

    def remove(self, cur: Node):
        cur_prev = cur.prev
        cur_next = cur.next
        cur_prev.next = cur_next
        cur_next.prev = cur_prev      
           
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        
         
        if len(self.cache) > self.capacity:
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

