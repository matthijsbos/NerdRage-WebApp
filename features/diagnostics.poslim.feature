Feature: Pitch axis positive limit switch indicator

    The pitch axis positive limit switch indicator provides diagnostic
    realtime information on the current state of the limit switch.

    Scenario: Pitch axis positive limit switch is activated
        Given the pitch axis positive limit switch is activated
        And the user has loaded the diagnostic page
        Then the pitch axis positive limit switch indicator is enabled

    Scenario: Pitch axis positive limit switch is deactivated
        Given the pitch axis positive limit switch is deactivated
        And the user has loaded the diagnostic page
        Then the pitch axis positive limit switch indicator is disabled

    Scenario: Pitch axis positive limit switch becomes activated
        Given the pitch axis positive limit switch is deactivated
        And the user has loaded the diagnostic page
        When the pitch axis positive limit switch is activated
        Then the pitch axis positive limit switch indicator is enabled
    
    Scenario: Pitch axis positive limit switch becomes deactivated
        Given the pitch axis positive limit switch is activated
        And the user has loaded the diagnostic page
        When the pitch axis positive limit switch is deactivated
        Then the pitch axis positive limit switch indicator is disabled
     