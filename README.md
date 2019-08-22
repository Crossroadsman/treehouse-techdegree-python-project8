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

- [ ] : **Allow filtering by the first letter of the mineral name.**
  - [ ] : Add links for each letter of the alphabet
  - [ ] : This should be added to the layout template so that it appears on every page.
  - [ ] : When a letter is clicked, a list of minerals that start with that letter should be displayed in the list view. 
  - [ ] : The letter of the alphabet currently being displayed should be bolded. 
  - [ ] : In the details view, no letter should be bolded. 
  - [ ] : On the homepage, select ‘A’ by default.
- [ ] : **Allow text search.**
  - [ ] : Add a search box and button. 
  - [ ] : The search box and button should be implemented as a form.
  - [ ] : When the search button is clicked, the site will search for minerals whose name contains the search text.
  - [ ] : The names of the minerals that match the search will be displayed in the list view.
  - [ ] : Add the search form to the layout template so that searching can be performed from any page in the site.
- [ ] : **Allow filtering by group.**
  - [ ] : Add the ability to filter the list of minerals by adding links to these groups on the left side of the 
          layout template. 
  - [ ] : Clicking a group name displays a list of all of the minerals in the database that are in that group. 
  - [ ] : The group name being displayed should be bolded. 
  - [ ] : In the details view, no group name should be bolded.
  - [ ] : Groups:
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

[link01]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/blob/master/mineral_catalog/requirements.txt
[link02]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog
[link03]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/cover
[link04]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/scripts
