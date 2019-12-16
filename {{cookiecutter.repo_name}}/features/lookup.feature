@web @yahoo
Feature: Yahoo prices Download
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments


  Scenario Outline: Basic Yahoo Search
    Given  go to https://www.marketwatch.com/tools/quotes/lookup.asp
    When the user finds element with id - Lookup
    And the user enters <phrase> in element
    And the user enters returnkey in element
    And the user finds element with name - price
    And get the attribute content of the element to closeprice variable
    Then save <phrase> closeprice to output.csv file



    Examples:
       | phrase |
        |MSFT|
        |AAPL|
        |GOOG|
