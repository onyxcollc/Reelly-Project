from behave import given, when, then








@when('Click Learn more button')
def click_learn_more_button(context):
    context.app.market_page.click_learn_more_button()



@then('Verify market page opens')
def verify_market_page(context):
    context.app.market_page.verify_market_page_open()


@then('Verify Learn more button is visible')
def verify_learn_more_button(context):
    context.app.market_page.verify_learn_more_button()