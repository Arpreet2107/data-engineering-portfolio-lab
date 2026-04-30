class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type=tea_type
        self.sweetness=sweetness
        self.size=size

    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size=order_string.split("-")
        return cls(tea_type,sweetness,size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_Size(size):
        return size in ["Small","Medium","Large"].lower()
    
print(ChaiUtils.is_valid_Size("Medium"))
    
order1 = ChaiOrder.from_dict({
    "tea_type":"masala",
    "sweetness":"medium",
    "size":"large"
    })
order2 = ChaiOrder.from_string("Ginger-no sugar-medium")

order3= ChaiOrder("Large","Low","Lemon")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)