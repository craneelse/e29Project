@web @yahoo
Feature: Yahoo prices Download
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments


  Scenario Outline: Basic IMDB search
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
