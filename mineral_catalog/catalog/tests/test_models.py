from django.test import TestCase

from catalog.models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.test_mineral_data = {
            'name': "Test Mineral",
            'image_filename': "Test Filename",
            'image_caption': "Test Caption",
            'category': "Test Category",
            'formula': "Test Formula",
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
            'group': "Test Group",
            'refractive_index': "Test Refractive Index",
            'crystal_habit': "Test Crystal Habit",
            'specific_gravity': "Test Specific Gravity"
        }

        self.test_mineral = Mineral.objects.create(**self.test_mineral_data)

    def test_create_model_correctly_reflects_data(self):
        for key, value in self.test_mineral_data.items():
            self.assertEqual(
                value,
                getattr(self.test_mineral, key)
            )

    def test_create_saves_valid_model_to_db(self):
        db_mineral = Mineral.objects.get(
            name=self.test_mineral.name
        )

        self.assertEqual(
            db_mineral,
            self.test_mineral
        )

    def test_meta_models_are_correctly_ordered(self):
        self.test_mineral.name = "Test second"
        self.test_mineral.save()
        self.test_other_mineral = Mineral.objects.create(
            **self.test_mineral_data
        )
        self.test_other_mineral.name = "Test first"
        self.test_other_mineral.save()

        test_minerals = Mineral.objects.all()
        self.assertEqual(
            test_minerals[0].name,
            "Test first"
        )
        self.assertEqual(
            test_minerals[1].name,
            "Test second"
        )

    def test_str_correctly_represents_model(self):
        self.assertEqual(
            str(self.test_mineral),
            self.test_mineral.name
        )

    def test_fieldnames_and_values_returns_valid_data(self):
        test_fieldnames_and_values = self.test_mineral.fieldnames_and_values()
        for key, value in self.test_mineral_data.items():
            self.assertIn(key, test_fieldnames_and_values)
            self.assertEqual(value, test_fieldnames_and_values[key]['value'])
            self.assertEqual(
                key.replace('_', ' '),
                test_fieldnames_and_values[key]['name']
            )
