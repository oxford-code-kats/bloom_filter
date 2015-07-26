from hashlib import md5
from collections.abc import Container
from functools import reduce
from operator import or_

class BloomFilter(Container):

    def __init__(self, num_hashes):
        self.bitmap = 0
        self.num_hashes = num_hashes
    
    def __contains__(self, item):
        h = self.hash(item)
        return self.bitmap & h == h

    def add(self, item):
        self.bitmap |= self.hash(item)

    def hash(self, item):
        m = md5()
        m.update(bytes(item, 'utf-8'))
        digest = m.digest()
        hashes = digest[:self.num_hashes]
        hashes = [1 << b for b in hashes]
        return reduce(or_, hashes)

    def __str__(self):
        return hex(self.bitmap)

if __name__ == '__main__':
    filter = BloomFilter(10)
    with open('/usr/share/dict/words') as words:
        for word in words:
            filter.add(word)

    print('dog' in filter)

    print('asdsfs' in filter)

    print(filter)