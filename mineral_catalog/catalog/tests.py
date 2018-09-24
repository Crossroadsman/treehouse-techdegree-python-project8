from django.test import TestCase
from django.urls import reverse

from .models import Mineral


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


class IndexViewTests(TestCase):
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
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "A Test Mineral Index 2 (id1)"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "A Test Mineral Index 1 (id2)"
        self.test_mineral_2.save()
        self.response = self.client.get(reverse('catalog:index'))

    def test_index_view_shows_all_minerals(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertIn(self.test_mineral_1, self.response.context['minerals'])
        self.assertIn(self.test_mineral_2, self.response.context['minerals'])

    def test_index_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'catalog/index.html')

    def test_index_view_shows_correct_mineral_name(self):
        self.assertContains(self.response, self.test_mineral_1.name)
        self.assertContains(self.response, self.test_mineral_2.name)

    def test_index_view_shows_minerals_in_correct_order(self):
        test_string = str(self.response.content)
        self.assertLess(
            test_string.index(self.test_mineral_2.name),
            test_string.index(self.test_mineral_1.name)
        )


class DetailViewTests(TestCase):
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
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "Test Mineral Index 2 (id1)"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "Test Mineral Index 1 (id2)"
        self.test_mineral_2.save()
        self.response = self.client.get(
            reverse('catalog:detail',
                    kwargs={'mineral_id': self.test_mineral_1.pk})
        )

    def test_detail_view_shows_only_correct_mineral(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.test_mineral_1,
                         self.response.context['mineral'])
        self.assertNotEqual(self.test_mineral_2,
                            self.response.context['mineral'])

    def test_detail_view_passes_correct_context(self):
        exclude_fields = ['id']
        top_section_fields = ['name', 'image_filename', 'image_caption']
        highlighted_fields = ['category', 'group']
        for field in exclude_fields:
            self.assertIn(field, self.response.context['exclude'])
        for field in top_section_fields:
            self.assertIn(field, self.response.context['top_section'])
        for field in highlighted_fields:
            self.assertIn(field, self.response.context['highlighted'])

    def test_detail_view_renders_top_section_before_highlighted(self):
        test_string = str(self.response.content)
        self.assertLess(
            test_string.index(self.response.context['top_section'][0]),
            test_string.index(self.response.context['highlighted'][0])
        )

    def test_detail_view_renders_highlighted_before_nonhighlighted(self):
        test_string = str(self.response.content)
        self.assertLess(
            test_string.index(self.response.context['highlighted'][0]),
            test_string.index('Luster')
        )

    def test_detail_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'catalog/detail.html')

    def test_detail_view_shows_correct_mineral_name(self):
        self.assertContains(self.response, self.test_mineral_1.name)


class RandomMineralViewTests(TestCase):
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
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "Test Mineral Index 2 (id1)"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "Test Mineral Index 1 (id2)"
        self.test_mineral_2.save()
        self.response = self.client.get(reverse('catalog:random'), follow=True)

    def test_random_mineral_view_redirects_to_valid_detail(self):
        self.assertEqual(self.response.status_code, 200)
        final_redirect = self.response.redirect_chain[-1][0]
        self.assertEqual(
            final_redirect,
            reverse('catalog:detail',
                    kwargs={'mineral_id': final_redirect[-1]})
        )
