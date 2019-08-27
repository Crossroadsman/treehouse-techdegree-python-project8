from django.test import TestCase

from catalog.templatetags.catalog_extras import (nav_field_list, 
    deunderscore, index)
from catalog.group_lookup import groups
from catalog.models import Mineral


MINERAL_DATA = [
    {
        'name': "Test Mineral 1",
        'image_filename': "Test Filename",
        'image_caption': "Test Caption",
        'category': "Silicate, Pyroxene",
        'formula': "B<sub>2</sub>Na",
        'strunz_classification': "Test Strunz Classification",
        'crystal_system': "Test Crystal System",
        'unit_cell': "Test Unit Cell",
        'color': "Test Color",
        'crystal_symmetry': "Test Crystal Symmetry",
        'cleavage': "Test Cleavage",
        'mohs_scale_hardness': "Test Mohs Scale Hardness",
        'luster': "Test xtestxLuster",
        'streak': "Test Streak",
        'diaphaneity': "Test Diaphaneity",
        'optical_properties': "Test Optical Properties",
        'group': "Sulfates",
        'refractive_index': "Test Refractive Index",
        'crystal_habit': "Test Crystal Habit",
        'specific_gravity': "Test Specific Gravity"
    },
    {
        'name': "Test Mineral 2",
        'image_filename': "Test Filename",
        'image_caption': "Test xTESTxCaption",
        'category': "Silicate",
        'formula': "AuB",
        'strunz_classification': "Test Strunz Classification",
        'crystal_system': "Test Crystal System",
        'unit_cell': "Test Unit Cell",
        'color': "Test Color",
        'crystal_symmetry': "Test Crystal Symmetry",
        'cleavage': "Test Cleavage",
        'mohs_scale_hardness': "Test Mohs Scale Hardness",
        'luster': "Test Luster",
        'streak': "Test Streak",
        'diaphaneity': "Test Diaphaneity",
        'optical_properties': "Test Optical Properties",
        'group': "Sulfides",
        'refractive_index': "Test Refractive Index",
        'crystal_habit': "Test Crystal Habit",
        'specific_gravity': "Test Specific Gravity"
    },
    {
        'name': "Test Mineral 3",
        'image_filename': "Test Filename",
        'image_caption': "Test Caption",
        'category': "Pyroxene",
        'formula': "Be",
        'strunz_classification': "Test Strunz Classification",
        'crystal_system': "Test Crystal System",
        'unit_cell': "Test Unit Cell",
        'color': "Test Color",
        'crystal_symmetry': "Test Crystal Symmetry",
        'cleavage': "Test Cleavage",
        'mohs_scale_hardness': "Test Mohs Scale Hardness",
        'luster': "Test Luster",
        'streak': "Test Streak",
        'diaphaneity': "Test Diaphaneity",
        'optical_properties': "Test Optical Properties",
        'group': "Sulfates",
        'refractive_index': "Test Refractive Index",
        'crystal_habit': "Test Crystal Habit",
        'specific_gravity': "Test Specific Gravity"
    },
    {
        'name': "Test Mineral 4",
        'image_filename': "Test Filename",
        'image_caption': "Test Caption",
        'category': "pyroxene, Silicate",
        'formula': "Bi",
        'strunz_classification': "Test Strunz Classification",
        'crystal_system': "Test Crystal System",
        'unit_cell': "Test Unit Cell",
        'color': "Test Color",
        'crystal_symmetry': "Test Crystal Symmetry",
        'cleavage': "Test Cleavage",
        'mohs_scale_hardness': "Test Mohs Scale Hardness",
        'luster': "Test Luster",
        'streak': "Test Streak",
        'diaphaneity': "Test Diaphaneity",
        'optical_properties': "Test Optical Properties",
        'group': "Sulfates and sulfides",
        'refractive_index': "Test Refractive Index",
        'crystal_habit': "Test Crystal Habit",
        'specific_gravity': "Test Specific Gravity"
    },
]

class NavFieldListTests(TestCase):

    def setUp(self):
        for mineral_data in MINERAL_DATA:
            Mineral.objects.create(**mineral_data)
        self.group_lookup = groups['group']

    def test_returns_correct_values(self):

        expected_field = 'group'
        expected_items = ['Sulfates', 'Sulfides', 'Sulfates_and_sulfides']
        expected_range = range(0, 3)

        result = nav_field_list(self.group_lookup, 'N/A')

        self.assertEqual(result['field'], expected_field)
        self.assertEqual(result['items'], expected_items)
        self.assertEqual(result['range'], expected_range)


class DeunderscoreTests(TestCase):

    def test_supplied_text_is_correctly_transformed(self):
        test_text = "This_Is-A__Test"

        result = deunderscore(test_text)

        self.assertEqual(
            result,
            "This Is-A  Test"
        )


class IndexTests(TestCase):

    def test_index_returns_the_correct_element_from_list(self):

        test_list = ['this', 'is', 'a', 'test']
        test_index = 1

        result = index(test_list, test_index)

        self.assertEqual(
            result,
            'is'
        )
