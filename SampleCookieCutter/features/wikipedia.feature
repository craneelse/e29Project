Feature: Sample Search

  Scenario Outline: Sample Search
    Given go to https://www.wikipedia.org/
    When the user finds element with name - search
    And the user enters <phrase> in element
    And the user enters returnkey in element
    And the user finds element with id - mw-content-text
    And get the text of the element to closeprice variable
    Then save <phrase> closeprice to data/bloombergoutput.csv file


    Examples:
       | phrase |
       |Rainforest|
