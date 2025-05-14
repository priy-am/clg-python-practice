# 54 WAP to distinct elements of a list without using set

def distinctElement(lst):
    distinct = []
    for i in lst:
        if i not in distinct:
            distinct.append(i)
    return distinct


numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Oringinal list is:", numbers)
print("Distinct elements are:", distinctElement(numbers))


# 54 WAP to perform different set operations (union, intersection, disjoint, issubset, issuperset)
class Myset:

    def __init__(self, elements ):
        self.elements = [ ]
        for i in elements:
            if i not in self.elements:
                self.elements.append(i)
    
    def union(self, other):
        result = self.elements.copy()
        for i in other.elements:
            if i not in result:
                result.append(i)
        return result
    
    def intersection(self, other):
        result = []
        for i in self.elements:
            if i in other.elements:
                result.append(i)
        return result
    
    def disjoint(self, other):
        for i in self.elements:
            if i in other.elements:
                return False
        return True
    
    def is_subset(self, other):
        for i in self.elements:
            if i not in other.elements:
                return False
        return True
    
    def is_superset(self, other):
        return other.is_subset(self)
    
    def display(self):
        return self.elements


set1 = Myset([1, 2, 3, 4, 5])
set2 = Myset([4, 5, 6, 7, 8])
print("Set 1:", set1.display())
print("Set 2:", set2.display())
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Disjoint:", set1.disjoint(set2))
print("Is Set 1 a subset of Set 2?", set1.is_subset(set2))
print("Is Set 1 a superset of Set 2?", set1.is_superset(set2))


