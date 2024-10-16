# last number
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def toString(self):
        return f"Customer name: {self.name}, Address: {self.address}"

# Example usage
customer = Customer("James ", "Kireka")
print(customer.toString())  # Output: Customer name: John Doe, Address: 123 Main St
