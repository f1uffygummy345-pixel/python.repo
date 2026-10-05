from abc import ABC, abstractmethod


class Toppings(ABC):
    def __init__(self):
        self.sold_out = {"mushrooms", "bacon"}
        self.banned_toppings = {"pineapple"}
        self.toppings = []

    @abstractmethod
    def add_topping(self, topping):
        """Add a topping after validation."""

    @abstractmethod
    def remove_topping(self, topping):
        """Remove a topping if it exists."""

    @abstractmethod
    def list_toppings(self):
        """Return the current list of toppings."""


class PizzaToppings(Toppings):
    def add_topping(self, topping):
        cleaned = topping.strip().lower()
        if not cleaned:
            raise ValueError("Topping name cannot be empty.")
        if cleaned in self.banned_toppings:
            raise ValueError(f"{topping} is banned.")
        if cleaned in self.sold_out:
            raise ValueError(f"{topping} is sold out.")
        if cleaned not in self.toppings:
            self.toppings.append(cleaned)
        return self.toppings

    def remove_topping(self, topping):
        cleaned = topping.strip().lower()
        if cleaned in self.toppings:
            self.toppings.remove(cleaned)
            return True
        return False

    def list_toppings(self):
        return list(self.toppings)


if __name__ == "__main__":
    order = PizzaToppings()

    for index in range(1, 6):
        topping = input(f"Enter topping {index}: ")
        if not topping.strip():
            continue
        try:
            order.add_topping(topping)
        except ValueError as exc:
            print(f"Skipping {topping!r}: {exc}")

    print("\nSelected toppings:", order.list_toppings())