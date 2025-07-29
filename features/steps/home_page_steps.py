from time import sleep

from behave import given, when, then




@when('Click on Off plan at the left side menu')
def off_plan_tab(context):
    context.app.home_page.off_plan_tab()


@when('Click on Off plan bottom left of screen')
def off_plan_tab_mobile(context):
    context.app.home_page.off_plan_tab_mobile()

