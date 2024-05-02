class TestAddToBucket:
    def test_bucket(self, main_page, item_page, cart_page):
        main_page.input_into_search_field('Iphone')
        main_page.chose_from_iframe_by_index()

        item_page.add_to_cart()
        item_price: str = item_page.item_price
        item_page.go_to_cart()

        cart_page.check_cart_title()
        cart_page.check_cart_price(item_price)
        cart_page.check_cart_items_amount(1)
        cart_page.check_submit_possible_is_clickable()
