# Get product name and price from the user
product_smg = input("Enter product name: ")
price_smg = input("Enter price: ")

# Open the inventory.txt file in append mode to store data
with open("inventory.txt", "a") as file_smg:
    file_smg.write(product_smg + "," + price_smg + "\n")

print("Product saved successfully")