# Created by churt at 1/3/19
@twitter
Feature: Login to Twitter
  The Bot should always be able to post.
  It is important that the login always works.
  Run this test all damn day and let me know if it fails
  cuz that means my API key is likely revoked!

  Scenario Outline: GlobalEntry Bot logs in to twitter
    Given twitters homepage
    When "<user>" logs in
    Then the twitter timeline appears

    Examples: users
      | user        |
      | GlobalEntry |