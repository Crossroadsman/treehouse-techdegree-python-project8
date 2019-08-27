import unittest

from django.test import Client, TestCase
from django.urls import resolve, reverse

from catalog.models import Mineral
from catalog.views import (index, detail, random_mineral, initial_letter, group)


VALID_MINERAL_DATA = {
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


class ViewTestCase(TestCase):

    # Setup and teardown
    # ------------------
    def setUp(self):
        self.abstract = True
        self.kwargs = {}
        self.name = 'catalog:'
        self.status_code = 200
        self.target_view = None
        self.template = 'catalog/'
        self.url = '/catalog/'
        
        self.client = Client()

    # Test Methods
    # ------------
    def test_url_resolves_to_correct_view(self):
        """Ensure that expected URLs resolve to their associated views"""

        # don't do anything when the method in the base class is called
        if self.abstract:
            return

        try:
            resolved_view = resolve(self.url).func
        except:
            print("RESOLVER ERROR")
            print(self)
            for setting in [self.name, self.target_view, self.template, self.url]:
                print(setting)

        self.assertEqual(resolved_view, self.target_view)


    def test_view_associated_with_correct_name(self):
        if self.abstract:
            return

        response = self.client.get(reverse(self.name, kwargs=self.kwargs))

        self.assertEqual(response.status_code, self.status_code)

    def test_view_renders_correct_template(self):
        if self.abstract:
            return

        response = self.client.get(reverse(self.name, kwargs=self.kwargs))

        self.assertTemplateUsed(response, self.template)


class IndexViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()

        self.abstract = False
        self.name += "index"
        self.target_view = index
        self.template += "index.html"
        self.url += ""
        
        self.test_mineral_data = VALID_MINERAL_DATA
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "A Test Mineral Index 2 (id1)"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "A Test Mineral Index 1 (id2)"
        self.test_mineral_2.save()
        
    def test_index_view_shows_all_minerals(self):
        response = self.client.get(reverse(self.name))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.test_mineral_1, response.context['minerals'])
        self.assertIn(self.test_mineral_2, response.context['minerals'])

    def test_index_view_shows_correct_mineral_name(self):
        response = self.client.get(reverse(self.name))

        self.assertContains(response, self.test_mineral_1.name)
        self.assertContains(response, self.test_mineral_2.name)

    def test_index_view_shows_minerals_in_correct_order(self):
        """Correct order is alphabetical"""
        response = self.client.get(reverse(self.name))
        test_string = str(response.content)
        
        self.assertLess(
            test_string.index(self.test_mineral_2.name),
            test_string.index(self.test_mineral_1.name)
        )


class DetailViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()

        self.abstract = False
        self.name += "detail"
        self.target_view = detail
        self.template += "detail.html"
        self.url += "mineral/1"

        self.test_mineral_data = VALID_MINERAL_DATA
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "Test Mineral Index 2 (id1)"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "Test Mineral Index 1 (id2)"
        self.test_mineral_2.save()

        self.kwargs = {'mineral_id': self.test_mineral_1.pk}
    
    def test_detail_view_shows_only_correct_mineral(self):
        response = self.client.get(reverse(self.name, kwargs=self.kwargs))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.test_mineral_1,
                         response.context['mineral'])
        self.assertNotEqual(self.test_mineral_2,
                            response.context['mineral'])

    def test_detail_view_passes_correct_context(self):
        response = self.client.get(reverse(self.name, kwargs=self.kwargs))
        exclude_fields = ['id']
        top_section_fields = ['name', 'image_filename', 'image_caption']
        highlighted_fields = ['category', 'group']
        
        for field in exclude_fields:
            self.assertIn(field, response.context['exclude'])
        for field in top_section_fields:
            self.assertIn(field, response.context['top_section'])
        for field in highlighted_fields:
            self.assertIn(field, response.context['highlighted'])

    def test_detail_view_renders_top_section_before_highlighted(self):
        response = self.client.get(reverse(self.name, kwargs=self.kwargs))
        test_string = str(response.content)

        self.assertLess(
            test_string.index(response.context['top_section'][0]),
            test_string.index(response.context['highlighted'][0])
        )

    def test_detail_view_renders_highlighted_before_nonhighlighted(self):
        response = self.client.get(reverse(self.name, kwargs=self.kwargs))
        test_string = str(response.content)
        
        self.assertLess(
            test_string.index(response.context['highlighted'][0]),
            test_string.index('Luster')
        )

    def test_detail_view_shows_correct_mineral_name(self):
        response = self.client.get(reverse(self.name, kwargs=self.kwargs))

        self.assertContains(response, self.test_mineral_1.name)


class RandomMineralViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()

        self.abstract = False
        self.name += "random"
        self.status_code = 302
        self.final_status_code = 200
        self.target_view = random_mineral
        self.template += "random.html"
        self.url += "random"

        self.test_mineral_data = VALID_MINERAL_DATA
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "Test Mineral Index 2 (id1)"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "Test Mineral Index 1 (id2)"
        self.test_mineral_2.save()

    @unittest.skip("never renders template, just redirects")
    def test_view_renders_correct_template(self):
        pass

    def test_random_mineral_view_redirects_to_valid_detail(self):

        response = self.client.get(reverse(self.name), follow=True)
        
        self.assertEqual(response.status_code, self.final_status_code)
        final_redirect = response.redirect_chain[-1][0]
        self.assertEqual(
            final_redirect,
            reverse('catalog:detail',
                    kwargs={'mineral_id': final_redirect[-1]})
        )


class InitialLetterViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()

        self.abstract = False
        self.name += "initial_letter"
        self.target_view = initial_letter
        self.template += "index.html"
        self.url += "initial/B"
        self.kwargs = {'letter': 'B'}

        self.test_mineral_data = VALID_MINERAL_DATA
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "A Test Mineral Index 2 (id1)"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "B Test Mineral Index 1 (id2)"
        self.test_mineral_2.save()


class GroupViewTests(ViewTestCase):
    
    def setUp(self):
        super().setUp()

        self.abstract = False
        self.name += "group"
        self.target_view = group
        self.template += "index.html"
        self.url += "field/category/i/1"
        self.kwargs = {'field': 'category', 'index': 1}

        self.test_mineral_data = VALID_MINERAL_DATA
        self.test_mineral_1 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_1.name = "Test Mineral Index 2 (id1)"
        self.test_mineral_1.category = "Borate"
        self.test_mineral_1.save()
        self.test_mineral_2 = Mineral.objects.create(**self.test_mineral_data)
        self.test_mineral_2.name = "Antimonide"
        self.test_mineral_2.save()
    
    def test_only_shows_minerals_matching_filter(self):
        
        response = self.client.get(reverse(self.name, kwargs=self.kwargs))

        self.assertContains(response, self.test_mineral_2.name)
        self.assertNotContains(response, self.test_mineral_1.name)
