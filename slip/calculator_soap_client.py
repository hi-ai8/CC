from zeep import Client

# Create a client using the WSDL
client = Client('http://localhost:8000/?wsdl')

# Test the service methods
print("Add: 10 + 5 =", client.service.add(10, 5))
print("Multiply: 10 * 5 =", client.service.multiply(10, 5))
print("Largest of Two: 10, 5 =", client.service.largest_of_two(10, 5))
print("Largest of Three: 10, 20, 15 =", client.service.largest_of_three(10, 20, 15))
print("Square: 6² =", client.service.square(6))
print("Cube: 3³ =", client.service.cube(3))
print("Add Three Numbers: 1 + 2 + 3 =", client.service.add_three(1, 2, 3))