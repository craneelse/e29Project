# Webscrapping using pytest-bdd and cookiecutter


The project is an attempt at a framework which can be used to quickly write scripts to scrape websites.
To make it easier for non programmers, most of the scripting is already coded into the generated project and they would only be interacting with 'feature' files, which take scripts written natural language.

To make this possible, I am using cucumber based framework pytest-bdd which handles natural language to code translation using step definitions. Language phrases are mapped to specific methods using annotations like '@Given', '@Then' etc.
I use cookiecutter to use existing feature file templates and embedd input data (csv) into the feature file. 
This makes it easy for the application for a non-programmer to write a quick script to get information from an website and save it to an output file





<b>Pre-requisites</b>
 1) Install pipenv on your python environmet
 2) Add the folder containing chromedriver.exe to PATH variable( chromedriver.exe is present under the bin directory of the generated template project)
 
 
<b> How to use the project</b>
1) Create a project using cookie-cutter
        $cookiecutter .
  Some of the defaults to pay attention to are 
      - feature_file : defaults to sample ( this means that you would find a features/sample.feature file in the generated project- this can be using as starting point of a webscrapping script)
      - input_data_file: give the path of the file if you have an input data which needs to be embedded into the feature file
2) Add chromedriver.ext into the path
       $cd {{cookiecutter.repo_name}}
       $set PATH=%PATH%;./bin
3) Run pytest to see the script run
       $pytest
     
   
  <h2><b>Sample Cookie Cutter<b></h2>
  
  I have included a sample cookie cutter project I generated using the attached cookiecutter template.
  
  <b>Feature file Content for the project</b>
 
 marketwatch.feature
  
 <pre> Feature: Sample Feature

  Scenario Outline: Basic Stock Search
    Given  go to https://www.marketwatch.com/tools/quotes/lookup.asp
    When the user finds element with id - Lookup
    And the user enters <phrase> in element
    And the user enters returnkey in element
    And the user finds element with name - price
    And get the attribute content of the element to closeprice variable
    Then save <phrase> closeprice to data/output.csv file
    
        Examples:
	      |phrase|
        |MSFT|
        |AAPL|
        |GEO|
  </pre>
  
  $cd SampleCookieCutter
  
  $set PATH=$PATH:./bin
  
  $pytest

  
