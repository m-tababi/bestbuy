from products import Product
from store import Store

product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)


def start(best_buy):
    while True:
        print("\n===== Best Buy Management System =====")
        print("1. List all products in store")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            best_buy.list_products()

        elif choice == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")

        elif choice == "3":
            handle_order(best_buy)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


def handle_order(best_buy):
    shopping_list = []
    products = best_buy.get_all_products()

    if not products:
        print("No active products available.")
        return

    # Merkt sich, wie viel pro Produkt in DIESER Bestellung schon bestellt wurde
    ordered_quantities = {}

    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("------")
    print("When you want to finish order, enter empty text.")

    while True:

        choice = input("Which product # do you want? ").strip()

        # Leere Eingabe → Bestellung abschließen
        if choice == "":
            break

       # Produktnummer prüfen
        if not choice.isdigit():
            print("Error adding product!")
            continue

        index = int(choice)

        if index < 1 or index > len(products):
            print("Error adding product!")
            continue

        selected_product = products[index - 1]

        # Menge abfragen
        amount_str = input("What amount do you want? ").strip()

        if amount_str == "":
            print("Error adding product!")
            continue

        if not amount_str.isdigit():
            print("Error adding product!")
            continue

        amount = int(amount_str)

        if amount <= 0:
            print("Error adding product!")
            continue

        if selected_product in ordered_quantities:
            already_ordered = ordered_quantities[selected_product]
        else:
            already_ordered = 0

        if already_ordered + amount > selected_product.quantity:
            print("Error while making order! Quantity larger than what exists")
            continue

        ordered_quantities[selected_product] = already_ordered + amount
        shopping_list.append((selected_product, amount))

        print("Product added to list!")

    if not shopping_list:
        print("No products in order.")
        return

    # Bestellung über den Store ausführen
    total_price = best_buy.order(shopping_list)

    print("********")
    print(f"Order made! Total payment: ${total_price}")

if __name__ == "__main__":
    start(best_buy)