class Product:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self. price = price
        self.quantity = quantity
        # active-Flag wird in quantity-Setter richtig gesetzt,
        # aber falls quantity beim Start 0 ist, initialisieren wir hier:
        if self.quantity == 0:
            self.__active = False
        else:
            self.__active = True

    # ---------- name ----------
    @property
    def name(self):
        """Getter for name"""
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """Setter for name. Name cannot be empty"""
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = value.strip()


    # ---------- price ----------
    @property
    def price(self)-> float:
        """Getter for name"""
        return self.__name

    @price.setter
    def price(self, value) -> None:
        """Setter for price. Must be non-negative"""
        if value is None or value == "":
            raise ValueError("Price cannot be empty.")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = float(value)

    # ---------- quantity ----------
    @property
    def quantity(self) -> int:
        """Getter for quantity."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """
        Setter for quantity.
        If quantity reaches 0, the product is deactivated.
        """
        if value is None or value == "":
            raise ValueError("Quantity cannot be empty.")
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = int(value)

        # Produkt deaktivieren, wenn Bestand 0
        if self.__quantity == 0:
            self.__active = False
        else:
            # Wenn wieder Bestand > 0, Produkt wieder aktivieren
            self.__active = True

    # ---------- active-status ----------
    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.__active

    def deactivate(self) -> None:
        """Manually deactivate the product."""
        self.__active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")