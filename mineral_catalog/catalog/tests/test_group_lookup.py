from django.test import TestCase

import catalog.group_lookup
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
        'name': "Test Mineral 2",
        'image_filename': "Test Filename",
        'image_caption': "Test Caption",
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


class GroupLookupTests(TestCase):

    def setUp(self):
        for mineral_data in MINERAL_DATA:
            Mineral.objects.create(**mineral_data)

    def test_get_matching_queryset_creates_correct_queryset_for_group(self):

        name = 'group'
        list = ['Organic Minerals', 'Arsenates', 'Halides', 'Sulfides', 'Silicates', 'Other', 'Oxides', 'Sulfosalts', 'Phosphates', 'Carbonates', 'Sulfates', 'Native Elements', 'Borates']
        match = 'exact'
        i = 3

        group_lookup = catalog.group_lookup.GroupLookup(
            name,
            list,
            match
        )

        test_queryset = group_lookup.get_matching_queryset(i)
        expected_matches = [
            'Test Mineral 2',
            'Test Mineral 4'
        ]

        self.assertEqual(
            test_queryset.count(),
            2
        )
        result_names = [mineral.name for mineral in test_queryset]
        for name in expected_matches:

            self.assertTrue(name in result_names)

    def test_get_matching_queryset_creates_correct_queryset_for_category(self):

        name = 'category'
        list = [
            'Amphibole', 'Antimonide', 'Arsenate', 'Arsenic', 'Arsenide',
            'Arsenite', 'Borate', 'Carbonate', 'Chromate', 'Copper',
            'Dark mica', 'Feldspar', 'Feldspathoid', 'Garnet', 'Halide',
            'Inosilicate', 'Iodate', 'Manganese', 'Metals and intermetallic alloys', 'Meteorite', 
            'Molybdate', 'Native', 'Nesosilicates', 'Nitrate', 'Organic', 
            'Oxalate', 'Oxide', 'Phosphate', 'Pyroxene', 'Rare earth', 'Selenate', 'Selenide', 'Silicate', 'Sulfate', 'Sulfide', 'Sulfosalt', 'Tectosilicates', 'Tektoborate', 'Telluride', 'Tellurate', 'Tellurite', 'Titanium', 'Tungstate', 'Uranium', 'Vanadate', 'Zeolite']
        match = 'contains'
        i = 28

        group_lookup = catalog.group_lookup.GroupLookup(
            name,
            list,
            match
        )

        test_queryset = group_lookup.get_matching_queryset(i)

        # Note, Test Mineral 4 is a match because although we are using
        # `contains` which writes a case-sensitive SQL query, SQLite
        # doesn't support case-sensitive LIKE statements, in which case
        # `contains` works like `icontains`.
        # In the future, if we migrate to, e.g., PostgreSQL for production,
        # we will have to change our expectation to exclude Test Mineral 4.
        # Note, we are not changing the match criterion to `icontains` instead
        # of `contains` because `contains` does describe the dataset (we never
        # encounter a lowercase 'pyroxene', for example.) Contrast this to
        # crystal system, where we really do need to specify `icontains`
        # because the dataset contains both cases.
        expected_matches = [
            'Test Mineral 1',
            'Test Mineral 3',
            'Test Mineral 4',
        ]
        
        self.assertEqual(
            test_queryset.count(),
            3
        )
        result_names = [mineral.name for mineral in test_queryset]
        for name in expected_matches:

            self.assertTrue(name in result_names)

    def test_get_matching_queryset_creates_correct_queryset_for_formula(self):

        name = 'formula'
        list = ['Au', 'B', 'Ba', 'Bi', 'Na', 'Ti']
        match = 'regex'
        i = 1
        before = r''
        after = r'([^a-z]|$)'

        group_lookup = catalog.group_lookup.GroupLookup(
            name,
            list,
            match,
            before=before,
            after=after
        )

        test_queryset = group_lookup.get_matching_queryset(i)
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

