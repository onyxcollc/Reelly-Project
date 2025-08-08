from behave import given, when, then




@when("Fill in Min {min_price} and Max {max_price}")
def min_max_price(context,min_price,max_price):
    min_val = int(min_price)
    max_val = int(max_price)
    context.app.price_page.min_max_price(min_val,max_val)
