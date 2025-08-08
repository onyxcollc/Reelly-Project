Feature: User should be able to filter by Presale EOI in Mobile mode

  Scenario: User can filter by Presale EOI mobile mode
    Given Open main page
    When Enter email onyxcollc@gmail.com
    When Enter your Childish13!
    And Click continue button mobile
    When Click on Off plan bottom left of screen
    Then Verify the off-plan opens
    When Click Sale Status
    And Click On PreSale (EOI)
    Then Verify each product contains the PreSale (EOI) tag