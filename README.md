Project 8: TBD
====================================

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

- [ ] : Uses provided base HTML/CSS


[link01]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/blob/master/mineral_catalog/requirements.txt
[link02]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog
[link03]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/cover
[link04]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/scripts
