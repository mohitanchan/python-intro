


class BillCalculator:

    menu = {
        "sandwich": 70,
        "pizza": 150,
        "frankie": 40,
        "soft-drink": 20,
        "tea": 15,
        "coffee": 20
    }

    def __init__(self):
        self.items = []
        self.total = 0

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, gst):
        gst = (gst/100) * self.total
        total = self.total + gst

        for item in self.items:
            print(f"{item}  Rs.{self.menu[item]}")

        print(f"GST Rs.{gst}")
        print(f"Total Rs.{total}")
