from django.test import TestCase


from datetime import datetime
from datetime import timedelta
from apps.web.forms import RenewBookForm


class RenewBookFormTest(TestCase):
    def test_renew_form_date_field_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renew_date'].label == None or form.fields['renew_date'.label == "renewal date"])

    def test_renew_form_date_field_help_text(self):
        form = RenewBookForm()
        self.assertEqual(form.fields['renew_date'].help_text, 'Enter a date now and 4 weeks')

    def test_renew_form_date_in_past(self):
        date = datetime.today() - timedelta(days=1)
        form_data = {'renew_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_too_far_in_future(self):
        date = datetime.today() + timedelta(days=1) + timedelta(weeks=4)
        form_data = {'renew_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        today = datetime.today()
        form_data = {'renew_date': today}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())


