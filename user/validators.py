from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_characters(value):
    if not re.match('^[a-zA-Z0-9_& .-@]+$', value):
        raise ValidationError(
            _('Field contains disallowed characters'))

def validate_employ(value):
    if not re.match('^[a-zA-Z0-9_& .-]+$', value):
        raise ValidationError(
            _('Field contains disallowed characters'))

def validate_name(value):
    if not re.match('^[a-zA-Z0-9_& .]+$', value):
        raise ValidationError(
            _('Field contains disallowed characters'))