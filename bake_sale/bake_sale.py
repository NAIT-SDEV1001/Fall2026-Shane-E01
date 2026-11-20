from datetime import datetime
from pathlib import Path
import csv

DATE_FORMAT = "%d/%m/%y"
class BakeSaleOrder:
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool) -> None:
        #validate qty
        if quantity <= 0:
            raise ValueError("Quantity must be a positive whole number")
        
        self.order_id = order_id
        self.customer_name = customer_name
        self.item = item
        self.quantity = quantity
        self.pickup_date = pickup_date
        self.collected = collected

    def __str__(self) ->str:       
        # collected = "Collected" if self.collected else "Awaiting Pickup"
        # pickup_date_string = self.pickup_date.strftime("%m/%d/%Y")
        return (
            f"{self.order_id} | {self.customer_name} | {self.quantity} x {self.item}"
            f" | {self.pickup_date.strftime(DATE_FORMAT)} | {"Collected" if self.collected else "Awaiting Pickup"}"
        )

# Create a GiftOrder subclass that inherits from BakeSaleOrder. Call super().__init__() to initialize the shared attributes, then store a nonblank gift_message (str). Override __str__() to reuse the regular display and append the gift message.
class GiftOrder(BakeSaleOrder):
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool, gift_message: str) -> None:
        super().__init__(order_id, customer_name, item, quantity, pickup_date, collected)

        if not gift_message.strip():
            raise ValueError("A gift order needs a gift message")
        self.gift_message = gift_message

    def __str__(self)->str:
        return f"{super().__str__()} | Gift message: {self.gift_message}"

class BakeSale:
    def __init__(self) -> None:
        self.orders: list[BakeSaleOrder] = []

    def load_orders(self, csv_path: Path)->None:
        try:
            with open(csv_path,'r',encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    order_id = row["order_id"]
                    customer_name = row["customer_name"]
                    item = row["item"]
                    quantity = int(row["quantity"]) 
                    pickup_date = datetime.strptime(row["pickup_date"],DATE_FORMAT).date()
                    collected = row["collected"] == "yes"
                    order_type = row["order_type"]
                    if order_type == "regular":
                        order = BakeSaleOrder(order_id,customer_name, item, quantity, pickup_date, collected)
                    else:
                        order = GiftOrder(order_id,customer_name, item, quantity, pickup_date, collected,row["gift_message"])
                    self.orders.append(order)
            #loop through list to test
            for order in self.orders:
                print(order.item)

        except FileNotFoundError:
            print("file not found")

# pickup_date_object = datetime.strptime("11/24/2026","%m/%d/%Y").date()
# test_bake_sale_order_object = BakeSaleOrder("123ABC","Homer Simposon","good stuff",3,pickup_date_object,False)
# print(test_bake_sale_order_object)
# 123ABC | Homer Simposon | 3 x good stuff | 11/24/2026 | Collected

# test_gift_order_object = GiftOrder("123ABC","Homer Simposon","good stuff",3,pickup_date_object,False,"Happy Birthday!")
# test_gift_order_object = GiftOrder("123ABC","Homer Simposon","good stuff",3,pickup_date_object,False,"   ")
# print(test_gift_order_object)

CSV_PATH = Path(__file__).parent / "bake_sale_orders.csv"
bake_sale = BakeSale()
bake_sale.load_orders(CSV_PATH)




