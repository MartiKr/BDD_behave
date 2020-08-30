Feature: make a deposit

    Feature: make a deposit
    As a user I want to login
    and make a deposit

    Scenario Outline: make a deposit
        Given As a client I want to log in as "<name>" properly and balance is 0
        When I make deposit: "<deposit>" for user: "<name>"
        And Balance is changed : "<deposit>" for user: "<name>"
        And I make the withdrawl: "<withdrawl>"
        Then Balance is changed for "<end_balance>" and if test fail screenshot is captured as file: "<name>".png

        Examples:
        | name              | deposit   | withdrawl | end_balance   |
        | Hermoine Granger  |   50      |   49      |   1           |
        | Harry Potter      |   1000    |   1000    |   0           |
        | Ron Weasly        |   34      |   30      |   4           |
        | Albus Dumbledore  |   345     |   300     |   45          |
        | Neville Longbottom| 1000000   |   999999  |   1           |
