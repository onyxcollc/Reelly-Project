Feature:  Users should be able to filter by Presale (EOI)

 Scenario: User can filter by  Presale (EOI)
    Given Open main page
    When Enter email onyxcollc@gmail.com
    When Enter your Childish13!
    And Click continue button
    When Click on Off plan at the left side menu
    Then Verify the off-plan opens
    When Click Sale Status
    And Click On PreSale (EOI)
    Then Verify each product contains the PreSale (EOI) tag