from behave import given, when, then







@when('Click Sale Status')
def sale_status_tab(context):
    context.app.off_plan_page.sale_status_tab()


@when('Click Announced button')
def announced_btn(context):
    context.app.off_plan_page.announced_btn()


@when('Click On PreSale (EOI)')
def on_sale_btn(context):
    context.app.off_plan_page.pre_sale_btn()



@then('Verify the off-plan opens')
def verify_off_plan_opens(context):
    context.app.off_plan_page.verify_off_plan_page_opened()


@then('Verify each product contains the Announced tag')
def verify_announced_tag(context):
    context.app.off_plan_page.verify_announced_tag()



@then('Verify each product contains the PreSale (EOI) tag')
def verify_pre_sale_eoi_tag(context):
    context.app.off_plan_page.verify_pre_sale_eoi_tag()