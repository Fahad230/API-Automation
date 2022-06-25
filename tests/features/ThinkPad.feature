unit @Thinking
Feature: FETCHING THINKPADS DATA
    Scenario: getting certain Thinkpads data with get request
        Given the endpoint of ThinkPad after the base URL
        When the GET request sent with header and token
        Then the response code should be 200 with the valid response body data


