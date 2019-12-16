Feature: Sample Feature

  Scenario Outline: Basic Stock Search
    Given  go to https://www.marketwatch.com/tools/quotes/lookup.asp
    When the user finds element with id - Lookup
    And the user enters <phrase> in element
    And the user enters returnkey in element
    And the user finds element with name - price
    And get the attribute content of the element to closeprice variable
    Then save <phrase> closeprice to data/output.csv file



    Examples:
       | phrase |
