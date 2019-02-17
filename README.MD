# Run Behave Test
1. Install Requirements <br>
`$ pip install -r requirements.txt`
2. Install Chromedriver and place in your $PATH

3. Enter a Twitter username/password into `config.yml`
4. Run Test<br>`$ behave`

# Structure

Test logic lives in the `/lib` folder; elements, page objects,
and steps are separated into their own directory. 

Step logic is imported into an `__all_steps__` variable 
which is used in steps directory's `__init__.py`.

Feature files, which is the file with Gherkin syntax, are the primary driver
of test cases. Find these in their own `features/` directory.

`Screenshots` will save to your local machine if tests fail

See `features/environment.py` for test setup hooks


