from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Project name validation
validate_project_name = RegexValidator(
    regex=r"^[\w.-_]+\Z",
    message=_("Enter a valid Project name. This value may contain only letters, numbers, and ./-/_/ characters.")
)
