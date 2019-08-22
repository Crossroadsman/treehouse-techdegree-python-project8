Project 8: Filtering and Searching the Mineral Catalog
======================================================

Installation
------------
- Clone the repo
- Create and activate a venv
- To run the application install the required packages using `pip install -r requirements.txt` from the 
  [mineral catalog][link02] project folder.
- To be able to run tests and generate coverage reports also install the test-specific packages using 
  `pip install -r test-requirements.txt`

Usage
-----
- The catalog app can be run using `manage.py runserver <ip>:<port>`
- Tests can be run using `manage.py test`. Detailed HTML test reports will be generated and saved in the [
  cover][link03] subdirectory
- The script for populating the database is in the [scripts][link04] subdirectory. You can delete the sqlite database 
  then repopulate it by running `python3 scripts/populate_database.py` from the root of the project.

Feature Checklist
-----------------

### Base Features ###

- [x] : **Allow filtering by the first letter of the mineral name.**
  - [x] : Add links for each letter of the alphabet
  - [x] : This should be added to the layout template so that it appears on every page.
  - [x] : When a letter is clicked, a list of minerals that start with that letter should be displayed in the list view. 
  - [x] : The letter of the alphabet currently being displayed should be bolded. 
  - [x] : In the details view, no letter should be bolded. 
  - [x] : On the homepage, select ‘A’ by default.
- [ ] : **Allow text search.**
  - [x] : Add a search box and button. 
  - [ ] : The search box and button should be implemented as a form.
  - [x] : When the search button is clicked, the site will search for minerals whose name contains the search text.
  - [x] : The names of the minerals that match the search will be displayed in the list view.
  - [x] : Add the search form to the layout template so that searching can be performed from any page in the site.
- [x] : **Allow filtering by group.**
  - [x] : Add the ability to filter the list of minerals by adding links to these groups on the left side of the 
          layout template. 
  - [x] : Clicking a group name displays a list of all of the minerals in the database that are in that group. 
  - [x] : The group name being displayed should be bolded. 
  - [x] : In the details view, no group name should be bolded.
  - [x] : Groups:
    - Silicates
    - Oxides
    - Sulfates
    - Sulfides
    - Carbonates
    - Halides
    - Sulfosalts
    - Phosphates
    - Borates
    - Organic Minerals
    - Arsenates
    - Native Elements
    - Other
- [x] : **Optimize database queries.**
  - [x] : Use the `django-debug-toolbar` to check that queries to the database take no longer than 10ms to complete.
- [ ] : **Unit test the app.**
  - [ ] : Write unit tests to test that each view is displaying the correct information. 
  - [ ] : Write unit tests to test that the models, classes, and other functions behave as expected.
  - [ ] : There are unit tests for all the:
    - [ ] : views
    - [ ] : models
    - [ ] : other functions
  - [ ] : Tests cover a reasonable amount of the code (50–80%).
- [x] : **Make the templates match the style used in the example files.**
  - [x] : Look at the example HTML files and `global.css` to determine the styles used in the pages.
- [ ] : **Coding Style.**
  - [ ] : Make sure your coding style complies with [PEP 8][link05].

### Extra Credit Features ###
- [x] : **Allow full-text search.**
  - [x] : Instead of only searching the mineral names, the site will search all fields in the database and display the names
          of the minerals that contain the search text.
- [x] : **Add more ways to filter.**
  - [x] : Instead of just filtering by first letter and group, add one or more additional filters.
  - [x] : These should behave like the group filter. Example filters are color and crystal habit, but you can choose to 
          add filtering for any property you like. Hint: the filters can act like canned search queries.


Testing
-------

### [Test Running](https://docs.djangoproject.com/en/2.2/topics/testing/overview/#running-tests) ###

- Run all tests:
  ```console
   $ python manage.py test
   ```

- Run a single test suite:
  ```console
  $ python manage.py test accounts
  ```

- Run a single test file:
  ```console
  $ python manage.py test accounts.tests.test_models
  ```

- Run a single test case:
  ```console
  $ python manage.py test accounts.tests.test_models.UserProfileModelTest
  ```

- Run a single test method:
  ```console
  $ python manage.py test accounts.tests.test_models.UserProfileModelTest.test_userprofile_without_required_fields_is_invalid
  ```

### Coverage ###

- Run coverage:
  ```console
  $ coverage run manage.py test [the-app-to-test]
  ```

- Show the coverage report:
  ```console
  $ coverage report
  ```

- Erase the coverage report
  ```console
  $ coverage erase
  ```



[link01]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/blob/master/mineral_catalog/requirements.txt
[link02]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog
[link03]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/cover
[link04]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/scripts
[link05]: https://www.python.org/dev/peps/pep-0008/
