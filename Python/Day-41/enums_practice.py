"""
enums_practice.py

Demonstrates Enum: defining members, auto(), printing, .name/.value access,
comparison, and iteration.
"""

from enum import Enum, auto


class Department(Enum):
    HR = auto()
    IT = auto()
    FINANCE = auto()
    MARKETING = auto()


class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()


def main():
    # --- Printing enums ---
    print("Printing enums:")
    print(Department.IT)  # Department.IT
    print(OrderStatus.SHIPPED)  # OrderStatus.SHIPPED

    # --- Accessing .name and .value ---
    status = OrderStatus.PROCESSING
    print(f"\n.name  -> {status.name}")
    print(f".value -> {status.value}")

    # --- Comparing enums ---
    print("\nComparing enums:")
    print("OrderStatus.PENDING == OrderStatus.PENDING:", OrderStatus.PENDING == OrderStatus.PENDING)
    print("OrderStatus.PENDING == OrderStatus.SHIPPED:", OrderStatus.PENDING == OrderStatus.SHIPPED)
    print("Department.HR == OrderStatus.PENDING:", Department.HR == OrderStatus.PENDING)

    # --- Looping through enums ---
    print("\nAll departments:")
    for department in Department:
        print(f"  {department.name} = {department.value}")

    print("\nAll order statuses:")
    for order_status in OrderStatus:
        print(f"  {order_status.name} = {order_status.value}")

    # --- Using an enum to drive logic instead of magic strings ---
    def describe_order(status: OrderStatus) -> str:
        if status == OrderStatus.DELIVERED:
            return "Order has arrived."
        if status == OrderStatus.CANCELLED:
            return "Order was cancelled."
        return "Order is still in progress."

    print("\nDescribe DELIVERED:", describe_order(OrderStatus.DELIVERED))
    print("Describe CANCELLED:", describe_order(OrderStatus.CANCELLED))
    print("Describe PENDING:", describe_order(OrderStatus.PENDING))


if __name__ == "__main__":
    main()
