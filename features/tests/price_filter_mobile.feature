Feature: Users should be able to give a range of price
  between min and max and verify the properties price

  Scenario: User can filter by Price filter
    Given Open main page
    When Enter email onyxcollc@gmail.com
    When Enter your Childish13!
    And Click continue button mobile
    When Click on Off plan bottom left of screen
    Then Verify the off-plan opens
    When Click Price
    And  Fill in Min 500000 and Max 1000000
    Then Verify each product contains the PreSale (EOI) tag