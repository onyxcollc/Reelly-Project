from behave import given, when, then


@when('Enter email {address}')
def email_address(context,address):
    context.app.log_in_page.email_address(address)

@when('Enter your {password}')
def enter_password(context,password):
    context.app.log_in_page.enter_password(password)

@when('Click continue button')
def continue_button(context):
    context.app.log_in_page.continue_button()


