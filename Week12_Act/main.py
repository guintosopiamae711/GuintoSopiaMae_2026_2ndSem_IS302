from product import Product
from inventory_manager import add_product_smg, view_products_smg, search_product_smg, update_product_quantity_smg


def add_product_menu_smg():
    product_id_smg = input("Enter Product ID: ").strip()
    name_smg = input("Enter Product Name: ").strip()

    if not product_id_smg or not name_smg:
        print("Product ID and name are required.")
        return

    try:
        price_smg = float(input("Enter Price: ").strip())
        quantity_smg = int(input("Enter Quantity: ").strip())
    except ValueError:
        print("Invalid input")
        return

    product_smg = Product(product_id_smg, name_smg, price_smg, quantity_smg)
    add_product_smg(product_smg)
    print("Product added successfully")


def search_product_menu_smg():
    product_id_smg = input("Enter Product ID: ").strip()
    if not product_id_smg:
        print("Product ID is required.")
        return

    product_smg = search_product_smg(product_id_smg)
    if product_smg:
        print("Product Found:")
        print(", ".join(product_smg))
    else:
        print("Product not found")


def update_quantity_menu_smg():
    product_id_smg = input("Enter Product ID: ").strip()
    if not product_id_smg:
        print("Product ID is required.")
        return

    try:
        quantity_smg = int(input("Enter new quantity: ").strip())
    except ValueError:
        print("Invalid input")
        return

    if quantity_smg < 0:
        print("Quantity cannot be negative.")
        return

    success_smg = update_product_quantity_smg(product_id_smg, quantity_smg)
    if success_smg:
        print("Quantity updated successfully")
    else:
        print("Product not found or inventory file missing")


if __name__ == "__main__":
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1 Add Product")
        print("2 View Products")
        print("3 Search Product")
        print("4 Update Quantity")
        print("5 Exit")
        choice_smg = input("Enter choice: ").strip()

        if choice_smg == "1":
            add_product_menu_smg()
        elif choice_smg == "2":
            view_products_smg()
        elif choice_smg == "3":
            search_product_menu_smg()
        elif choice_smg == "4":
            update_quantity_menu_smg()
        elif choice_smg == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid option")
