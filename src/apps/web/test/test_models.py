from django.test import TestCase

from apps.web.models import Autor

class AutorModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.autor = Autor.objects.create(first_name="Hans", last_name="Agurto")

    def test_first_name_label(self):
        field_label = self.autor._meta.get_field('first_name').verbose_name

        self.assertEquals(field_label, "first name")

    def test_date_of_death(self):
        field_label = self.autor._meta.get_field("date_of_death").verbose_name
        self.assertEquals(field_label, 'Died')

    def test_first_name_max_length(self):
        max_length = self.autor._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        expected_object_name = "%s, %s" % (self.autor.last_name, self.autor.first_name)
        self.assertEquals(expected_object_name, str(self.autor))

    def test_get_absolute_url(self):
        url_test = '/autor_detalle/%s' % self.autor.id
        self.assertEquals(self.autor.get_absolute_url(), url_test)