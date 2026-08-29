class CartPage:
    def __init__(self, page):
        self.page = page

        self.cart_item = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def get_cart_items_count(self):
        return self.cart_item.count()

    def click_checkout(self):
        self.checkout_button.click()