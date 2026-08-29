class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.page_title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.add_to_cart_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_link = page.locator(".shopping_cart_link")

    def get_inventory_count(self):
        return self.inventory_items.count()

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def get_cart_badge_text(self):
        return self.shopping_cart_badge.inner_text()

    def open_cart(self):
        self.shopping_cart_link.click()

   