Feature: User should be able to filter by Announced in Mobile mode

  Scenario: User can filter by Announced mobile mode
    Given Open main page
    When Enter email onyxcollc@gmail.com
    When Enter your Childish13!
    And Click continue button
    When Click on Off plan bottom left of screen
    Then Verify the off-plan opens
    When Click Sale Status
    And Click Announced button
    Then Verify each product contains the Announced tag