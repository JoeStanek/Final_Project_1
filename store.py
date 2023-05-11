from PyQt5.QtWidgets import *
from gui import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Store(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        """
        Initializes variables, links buttons, and hides certain widgets on the GUI
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.cart_amt = 0
        self.total = 0
        self.sand_amt = 0
        self.cookie_amt = 0
        self.water_amt = 0
        self.pizza_amt = 0
        self.soda_amt = 0
        self.salad_amt = 0

        self.shop_button.clicked.connect(lambda: self.shop())
        self.back_button.clicked.connect(lambda: self.back())
        self.add_button.clicked.connect(lambda: self.add_sand())
        self.add_button_2.clicked.connect(lambda: self.add_cookie())
        self.add_button_3.clicked.connect(lambda: self.add_water())
        self.add_button_4.clicked.connect(lambda: self.add_pizza())
        self.add_button_5.clicked.connect(lambda: self.add_soda())
        self.add_button_6.clicked.connect(lambda: self.add_salad())
        self.checkout_button.clicked.connect(lambda: self.checkout())

        self.label_2.hide()

        self.add_button.hide()
        self.add_button_2.hide()
        self.add_button_3.hide()
        self.add_button_4.hide()
        self.add_button_5.hide()
        self.add_button_6.hide()

        self.sand_label.hide()
        self.cookie_label.hide()
        self.water_label.hide()
        self.pizza_label.hide()
        self.soda_label.hide()
        self.label_5.hide()
        self.added_1.hide()
        self.added_2.hide()
        self.added_3.hide()
        self.added_4.hide()
        self.added_5.hide()
        self.added_6.hide()

        self.checkout_label_1.hide()
        self.checkout_label_2.hide()
        self.checkout_label_3.hide()
        self.line_2.hide()
        self.label_sand.hide()
        self.label_cookie.hide()
        self.label_water.hide()
        self.label_pizza.hide()
        self.label_soda.hide()
        self.label_salad.hide()
        self.label_sand_amt.hide()
        self.label_cookie_amt.hide()
        self.label_water_amt.hide()
        self.label_pizza_amt.hide()
        self.label_soda_amt.hide()
        self.label_salad_amt.hide()
        self.label_sand_total.hide()
        self.label_cookie_total.hide()
        self.label_water_total.hide()
        self.label_pizza_total.hide()
        self.label_soda_total.hide()
        self.label_salad_total.hide()
        self.line_3.hide()
        self.total_label.hide()
        self.total_amt_label.hide()

        self.amt_label.hide()
        self.sand_amt_line.hide()
        self.cookie_amt_line.hide()
        self.water_amt_line.hide()
        self.pizza_amt_line.hide()
        self.soda_amt_line.hide()
        self.salad_amt_line.hide()

        self.back_button.hide()

    def shop(self):
        """
        Changes the display of the GUI by hiding and showing widgets
        :return: None
        """
        self.add_button.show()
        self.add_button_2.show()
        self.add_button_3.show()
        self.add_button_4.show()
        self.add_button_5.show()
        self.add_button_6.show()

        self.sand_label.show()
        self.cookie_label.show()
        self.water_label.show()
        self.pizza_label.show()
        self.soda_label.show()
        self.label_5.show()

        self.amt_label.show()
        self.sand_amt_line.show()
        self.cookie_amt_line.show()
        self.water_amt_line.show()
        self.pizza_amt_line.show()
        self.soda_amt_line.show()
        self.salad_amt_line.show()

        self.back_button.show()

        self.shop_button.hide()
        self.checkout_button.hide()

    def add_sand(self):
        """
        Adds the amount of sandwiches typed into the textbox on the gui to the cart, and adds to the final total
        :return: None
        """
        self.added_2.hide()
        self.added_3.hide()
        self.added_4.hide()
        self.added_5.hide()
        self.added_6.hide()
        try:
            self.label_2.hide()
            amt = int(self.sand_amt_line.text())
            self.cart_amt += amt
            self.sand_amt += amt

            self.total += (4*amt)

            self.cart_amt_label.setText(f"Items in cart: {self.cart_amt}")
            self.added_1.show()
            self.sand_amt_line.setText("")

        except ValueError:
            self.label_2.show()

    def add_cookie(self):
        """
        Adds the amount of cookies typed into the textbox on the gui to the cart, and adds to the final total
        :return: None
        """
        self.added_1.hide()
        self.added_3.hide()
        self.added_4.hide()
        self.added_5.hide()
        self.added_6.hide()

        try:
            self.label_2.hide()
            amt = int(self.cookie_amt_line.text())
            self.cart_amt += amt
            self.cookie_amt += amt

            self.total += (1.5*amt)

            self.cart_amt_label.setText(f"Items in cart: {self.cart_amt}")
            self.added_2.show()
            self.cookie_amt_line.setText("")
        except ValueError:
            self.label_2.show()

    def add_water(self):
        """
        Adds the amount of waters typed into the textbox on the gui to the cart, and adds to the final total
        :return: None
        """
        self.added_2.hide()
        self.added_1.hide()
        self.added_4.hide()
        self.added_5.hide()
        self.added_6.hide()

        try:
            self.label_2.hide()
            amt = int(self.water_amt_line.text())
            self.cart_amt += amt
            self.water_amt += amt

            self.total += (1*amt)

            self.cart_amt_label.setText(f"Items in cart: {self.cart_amt}")
            self.added_3.show()
            self.water_amt_line.setText("")
        except ValueError:
            self.label_2.show()

    def add_pizza(self):
        """
        Adds the amount of pizzas typed into the textbox on the gui to the cart, and adds to the final total
        :return: None
        """
        self.added_2.hide()
        self.added_3.hide()
        self.added_1.hide()
        self.added_5.hide()
        self.added_6.hide()

        try:
            self.label_2.hide()
            amt = int(self.pizza_amt_line.text())
            self.cart_amt += amt
            self.pizza_amt += amt

            self.total += (8*amt)

            self.cart_amt_label.setText(f"Items in cart: {self.cart_amt}")
            self.added_4.show()
            self.pizza_amt_line.setText("")
        except ValueError:
            self.label_2.show()

    def add_soda(self):
        """
        Adds the amount of sodas typed into the textbox on the gui to the cart, and adds to the final total
        :return: None
        """
        self.added_2.hide()
        self.added_3.hide()
        self.added_4.hide()
        self.added_1.hide()
        self.added_6.hide()

        try:
            self.label_2.hide()
            amt = int(self.soda_amt_line.text())
            self.cart_amt += amt
            self.soda_amt += amt

            self.total += (2*amt)

            self.cart_amt_label.setText(f"Items in cart: {self.cart_amt}")
            self.added_5.show()
            self.soda_amt_line.setText("")
        except ValueError:
            self.label_2.show()

    def add_salad(self):
        """
        Adds the amount of salads typed into the textbox on the gui to the cart, and adds to the final total
        :return: None
        """
        self.added_2.hide()
        self.added_3.hide()
        self.added_4.hide()
        self.added_5.hide()
        self.added_1.hide()

        try:
            self.label_2.hide()
            amt = int(self.salad_amt_line.text())
            self.cart_amt += amt
            self.salad_amt += amt

            self.total += (3*amt)

            self.cart_amt_label.setText(f"Items in cart: {self.cart_amt}")
            self.added_6.show()
            self.salad_amt_line.setText("")
        except ValueError:
            self.label_2.show()

    def checkout(self):
        self.shop_button.hide()
        self.checkout_button.hide()
        self.cart_amt_label.hide()

        self.welcome_label.setText("Checkout")

        self.checkout_label_1.show()
        self.checkout_label_2.show()
        self.checkout_label_3.show()
        self.line_2.show()
        self.label_sand.show()
        self.label_cookie.show()
        self.label_water.show()
        self.label_pizza.show()
        self.label_soda.show()
        self.label_salad.show()
        self.label_sand_amt.show()
        self.label_cookie_amt.show()
        self.label_water_amt.show()
        self.label_pizza_amt.show()
        self.label_soda_amt.show()
        self.label_salad_amt.show()
        self.label_sand_total.show()
        self.label_cookie_total.show()
        self.label_water_total.show()
        self.label_pizza_total.show()
        self.label_soda_total.show()
        self.label_salad_total.show()
        self.line_3.show()
        self.total_label.show()
        self.total_amt_label.show()

        self.label_sand_amt.setText(f"{self.sand_amt}")
        self.label_cookie_amt.setText(f"{self.cookie_amt}")
        self.label_water_amt.setText(f"{self.water_amt}")
        self.label_pizza_amt.setText(f"{self.pizza_amt}")
        self.label_soda_amt.setText(f"{self.soda_amt}")
        self.label_salad_amt.setText(f"{self.salad_amt}")

        self.label_sand_total.setText(f"${(self.sand_amt * 4.0):.2f}")
        self.label_cookie_total.setText(f"${(self.cookie_amt * 1.5):.2f}")
        self.label_water_total.setText(f"${(self.water_amt * 1.0):.2f}")
        self.label_pizza_total.setText(f"${(self.pizza_amt * 8.0):.2f}")
        self.label_soda_total.setText(f"${(self.soda_amt * 2.0):.2f}")
        self.label_salad_total.setText(f"${(self.salad_amt * 3.0):.2f}")
        self.total_amt_label.setText(f"${self.total:.2f}")



    def back(self):
        if self.cart_amt == 0:
            self.checkout_button.setEnabled(False)
        else:
            self.checkout_button.setEnabled(True)

        self.added_1.hide()
        self.added_2.hide()
        self.added_3.hide()
        self.added_4.hide()
        self.added_5.hide()
        self.added_6.hide()

        self.add_button.hide()
        self.add_button_2.hide()
        self.add_button_3.hide()
        self.add_button_4.hide()
        self.add_button_5.hide()
        self.add_button_6.hide()

        self.sand_label.hide()
        self.cookie_label.hide()
        self.water_label.hide()
        self.pizza_label.hide()
        self.soda_label.hide()
        self.label_5.hide()

        self.amt_label.hide()
        self.sand_amt_line.hide()
        self.cookie_amt_line.hide()
        self.water_amt_line.hide()
        self.pizza_amt_line.hide()
        self.soda_amt_line.hide()
        self.salad_amt_line.hide()

        self.back_button.hide()
        self.label_2.hide()

        self.shop_button.show()
        self.checkout_button.show()
