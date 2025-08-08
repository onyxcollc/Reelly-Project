from behave import given, when, then






@then('Fill Out Broker Relationship Form')
def broker_form(context):
    context.app.broker_relationship_page.broker_form()

