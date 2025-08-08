Feature: User should be able to access Offers for you market page

#  Scenario: User can access Offers for you market page
#    Given Open main page
#    When Enter email onyxcollc@gmail.com
#    When Enter your Childish13!
#    And Click continue button
#    When Click on Market at the left side menu
#    Then Verify market page opens


#  Scenario: User can access Offers for you market page and verify
#    "Learn more" button is available
#    Given Open main page
#    When Enter email onyxcollc@gmail.com
#    When Enter your Childish13!
#    And Click continue button
#    When Click on Market at the left side menu
#    Then Verify market page opens
#    Then Verify Learn more button is visible


Scenario: User can access Offers for you market page and verify
    "Learn more" button is available
    Given Open main page
    When Enter email onyxcollc@gmail.com
    When Enter your Childish13!
    And Click continue button
    When Click on Market at the left side menu
    Then Verify market page opens
    When Click Learn more button
    Then Fill Out Broker Relationship Form