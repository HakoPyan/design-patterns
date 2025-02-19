# Main idea: extract related algorithms into separate classes and define a common interface for them
from abc import ABC, abstractmethod


# Step 1: Create the DiscountStrategy interface
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass


# Step 2: Implement the discount strategies
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self._percentage = percentage

    def apply_discount(self, total: float) -> float:
        return (1 - self._percentage / 100) * total


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixed_amount: float):
        self._fixed_amount = fixed_amount

    def apply_discount(self, total: float) -> float:
        return max(total - self._fixed_amount, 0)


# Step 3: Implement the ShoppingCart class
class ShoppingCart:
    def __init__(self, discount_strategy):
        self._discount_strategy = discount_strategy
        self._items = {}

    def add_item(self, item: str, price: float):
        self._items[item] = price

    def remove_item(self, item: str):
        self._items.pop(item, None)

    def get_total(self) -> float:
        return sum(self._items.values())

    def get_total_after_discount(self) -> float:
        return self._discount_strategy.apply_discount(self.get_total())


# Step 4: Test your implementation
if __name__ == "__main__":
    cart = ShoppingCart(FixedAmountDiscount(5))

    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    print("Total before discount:", cart.get_total())

    print("Total after discount:", cart.get_total_after_discount())
