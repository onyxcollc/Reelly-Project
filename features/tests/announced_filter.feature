Feature: Announced filter feature works as it should

  Scenario: User can filter by  Announced
    Given Open main page
    When Enter email onyxcollc@gmail.com
    When Enter your Childish13!
    And Click continue button
    When Click on Off plan at the left side menu
    Then Verify the off-plan opens
    When Click Sale Status
    And Click Announced button
    Then Verify each product contains the Announced tag