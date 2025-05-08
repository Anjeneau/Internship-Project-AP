# Created by Anjen at 11/7/2024
Feature: Test to edit personal info

  Scenario: User can go to settings and edit the personal information
    Given Open signin page
    When Enter email leopie19@gmail.com
    And Enter password in input field tac3367109
    And Click signin button
    And Click settings button
    And Click edit profile
    And Enter name in input field Nina
    And Click save button
    Then Click close button