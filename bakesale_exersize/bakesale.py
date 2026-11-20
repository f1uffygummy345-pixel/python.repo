from datetime import datetime
DATE_FORMAT = "%m/%d/%Y"
class BakeSaleOrder:
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool)->None:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        self.order_id = order_id
        self.customer_name = customer_name
        self.item = item
        self.quantity = quantity
        self.pickup_date = pickup_date
        self.collected = collected
    def __str__(self)->str:
        return (f"{self.order_id} | {self.customer_name} | {self.quantity} x {self.item}"
                f" | {self.pickup_date.strftime(DATE_FORMAT)}"
                f" | {"Collected" if self.collected else "Awaiting Pickup"}"
                )
class GiftOrder(BakeSaleOrder):
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool, 
                 gift_message: str)->None:
        super().__init__(order_id, customer_name, item, quantity, pickup_date, collected)  
        if not gift_message.strip():
            raise ValueError("A gift order must have a gift message.") 
        
pickup_date_object = datetime.strptime("10/02/2008", "%m/%d/%Y").date()

order1 = BakeSaleOrder("abc123","Ruggie Bucchi","Donut",20,pickup_date_object,False)
print(order1)

gift_order1 = GiftOrder("abc123","Ruggie Bucchi","Donut",20,pickup_date_object,False,"We know you're broke, Ruggie. :D")
print(gift_order1)