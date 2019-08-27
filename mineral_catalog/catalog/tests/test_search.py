from django.test import TestCase

from catalog.models import Mineral
from catalog.search import full_text_search


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
        'group': "Sulfides",
        'refractive_index': "Test Refractive Index",
        'crystal_habit': "Test Crystal Habit",
        'specific_gravity': "Test Specific Gravity"
    },
]


class SearchTests(TestCase):

    def setUp(self):
        for mineral_data in MINERAL_DATA:
            Mineral.objects.create(**mineral_data)
    
    def test_search_term_is_found_anywhere_in_text_fields(self):

        search_term = "xtestx"

        test_queryset = full_text_search(search_term)
        expected_matches = [
            'Test Mineral 1',
            'Test Mineral 2'
        ]

        self.assertEqual(
            test_queryset.count(),
            2
        )
        result_names = [mineral.name for mineral in test_queryset]
        for name in expected_matches:

            self.assertTrue(name in result_names)
