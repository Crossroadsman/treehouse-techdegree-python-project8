#!/usr/bin/env python3

"""Populate Database
A simple script to populate the minerals database with entries from a JSON
file
Created: 2018
Last Update: 2018-08-15
Author: Alex Koumparos
Modified By: Alex Koumparos
"""
import os
import sys
import logging
import json

from django.core.wsgi import get_wsgi_application

# Get the absolute path to the project's root and add it to the path
# that python looks for files in
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Tell Django that settings.py is in the inner project-name folder
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mineral_catalog.settings")

# makes it possible to load models etc
application = get_wsgi_application()

# the following line is strictly a PEP8 E402 violation but this structure
# seems to be standard for creating standalone scripts in Django projects
from catalog.models import Mineral

# set the working directory
# (this ensures that relative paths work no matter where in the filesystem
# we are when we run this script)
os.chdir(BASE_DIR)


logging.basicConfig(
    filename='populate_database.log',
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

FILENAME = '../data/minerals.json'


def file_to_dicts():
    """opens FILENAME, a json file that can be decoded to a list of dicts
    and returns the decoded list of dicts"""
    with open(FILENAME) as file_handle:
        objects = json.load(file_handle)
        return objects


def strip_leading_characters(string, num):
    """Returns the input string after removing `num` leading characters"""
    return string[num:]


def set_name_from_dict(string, dictionary, key, leading, trailing):
    """Replaces the string with the value from a specified dictionary key,
    prepending and appending the leading/trailing text as applicable"""
    return "{}{}{}".format(leading,
                           dictionary[key],
                           trailing)


def clean_data(dictionary):
    name_map = {
        'image filename': 'image_filename',
        'image caption': 'image_caption',
        'strunz classification': 'strunz_classification',
        'crystal system': 'crystal_system',
        'unit cell': 'unit_cell',
        'crystal symmetry': 'crystal_symmetry',
        'mohs scale hardness': 'mohs_scale_hardness',
        'optical properties': 'optical_properties',
        'refractive index': 'refractive_index',
        'crystal habit': 'crystal_habit',
        'specific gravity': 'specific_gravity',
    }
    for key, value in name_map.items():
        try:
            dictionary[value] = dictionary.pop(key)
        except KeyError:
            msg = "object had no value with the key: {}".format(key)
            logging.info(msg)

    tweaks_map = {
        'image_filename': {'function': set_name_from_dict,
                           'args': [dictionary,
                                    'name',
                                    '',
                                    '.jpg']},
    }

    for key, value in tweaks_map.items():
        f = value['function']
        args = value['args']
        try:
            dictionary[key] = f(dictionary[key], *args)
        except KeyError:
            msg = "object had no value with the key: {}".format(key)
            logging.info(msg)
    return dictionary


def create_instance(**kwargs):
    Mineral.objects.create(**kwargs)


def populate_database():
    objects = file_to_dicts()
    for object in objects:
        cleaned = clean_data(object)
        create_instance(**cleaned)

# ---------------------------------

if __name__ == "__main__":

    populate_database()
