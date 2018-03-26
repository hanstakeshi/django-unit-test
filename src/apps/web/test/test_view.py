from django.test import TestCase


from apps.web.models import Autor

from django.urls import reverse


class AutorViewTest(TestCase):
    def setUp(self):
        numero_iteraciones = 13
        for autor_num in range(numero_iteraciones):
            Autor.objects.create(first_name="Hans %s" % autor_num, last_name="Agurto %s" % autor_num)

    def test_view_url_autores(self):
        resp = self.client.get('/autores/')
        self.assertEqual(resp.status_code, 200)


    def test_view_url_autores_by_name(self):
        resp = self.client.get(reverse('web:autores'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'web/autores.html')