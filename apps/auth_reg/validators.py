import os
from django.contrib.auth.password_validation import get_default_password_validators
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from rest_framework import serializers
from PIL import Image
from apps.user_profile.user_company.models.choices import IndustryChoice


# Password validation
def validate_password(password, user=None, password_validators=None):
    """
    Validate that the password meets all validator requirements.

    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError with all error messages.
    """
    errors = []
    if password_validators is None:
        password_validators = get_default_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, user)
        except ValidationError as error:
            errors.append(error)
    if errors:
        raise serializers.ValidationError({password: errors})


# Company name validation
validate_company_name = RegexValidator(
    regex=r'^[\w\-_:&\.\'\s]*$',
    message="Only alphanumeric (A-Z, 0-9) and symbols -_:&.' characters are allowed."
)

# Select industries validation
validate_select_industries_name = RegexValidator(
    regex=r'^[a-zA-Z]+[a-zA-Z()\s]*$',
    message='Invalid characters, the string should start with letters (A-Z) only and can be used symbols ().'
)


#  Image resolution validation
def validate_image_resolution(image):
    with Image.open(image) as img:
        width, height = img.size
        if width != 300 or height != 300:
            raise ValidationError(
                f"Image resolution should be at 300x300. Got {width}x{height}"
            )


#  List industries validation
def validate_list_industry(data):
    str_data = ','.join(data.split(', '))
    list_data = str_data.split(',')
    for industry in list_data:
        if industry not in [check[1] for check in IndustryChoice.INDUSTRIES]:
            raise ValidationError(
                f"'{industry}' is not a valid choice."
            )


#  Change filename image
def change_filename_logo(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = '{}_{}.{}'.format(instance.company_name, instance.id, ext)
    return os.path.join('logo/company/', new_filename)
