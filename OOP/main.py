from abc import ABC, abstractclassmethod

class Customer():
    customer_id = 100000
    def __init__(self, name) -> None:
        self._name = name
        self.customer_id = Customer.customer_id
        Customer.customer_id +=1
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name=value
            return self
        else:
            raise ValueError("Name must be of type string")
    @property
    def customer_id(self):
        return self.customer_id

    @customer_id.setter
    def customer_id(self, value:int):
        raise ValueError("Cannot Modify Customer ID")
    
    
                    
class Account(ABC):
    
    def __init__(self, customer:Customer, account_type) -> None:
        self.customer_id = customer.customer_id
        
    
    
