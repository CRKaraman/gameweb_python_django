from django.forms import (CharField, Form)
from django.utils.translation import ugettext_lazy as _


class AddDeveloperForm(Form):
    name = CharField(max_length=64, label=_('Name'))
