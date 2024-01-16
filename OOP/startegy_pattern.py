from abc import ABC, abstractmethod

class Sorting(ABC):
    def __init__(self, my_list: list) -> None:
       self.list = my_list
    @abstractmethod
    def sorting_method(self):
        pass
    
class RemoveNegative(Sorting):
    def sorting_method(self):
        x = [element for element in self.list if element > 0]
        print(x)
class RemovePositive(Sorting):
    def sorting_method(self):
        x = [element for element in self.list if element < 0 ]
        print(x)
class AddTen(Sorting):
    def add_ten(self):
        x = [element+10 for element in self.list ]
        print(x)
        
remove_negative_instance = RemoveNegative([1, 2, 3, 45, 6, -6, -8, 10, 20])
remove_postive_instance = RemovePositive([1, 2, 3, 45, 6, -6, -8, 10, 20])
add_ten = AddTen([1, 2, 3, 45, 6, -6, -8, 10, 20])

# Call the sorting method
remove_negative_instance.sorting_method()
remove_postive_instance.sorting_method()
add_ten.add_ten()