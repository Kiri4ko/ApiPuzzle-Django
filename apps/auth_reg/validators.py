import os
from django.contrib.auth.password_validation import get_default_password_validators
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from rest_framework import serializers
from datetime import date
from PIL import Image


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


# Generic validator for latin and dot only.
validate_generic_latin_symbols = RegexValidator(
    regex=r'^[a-zA-Z]+[a-zA-Z\W]*$',
    message='Invalid characters, the string should start with letters (A-Z) only and can be used symbols.'
)

# Generic validator for alphanumeric and symbol
validate_generic_alphanumeric_symbols = RegexValidator(
    regex=r'^[\w\W]*$',
    message='Only alphanumeric (A-Z, 0-9) and symbols characters are allowed.'
)

# Generic validator for latin
validate_generic_latin = RegexValidator(
    regex=r'^[a-zA-Z\s]*$',
    message='Only alphabetic (A-Z) characters are allowed.'
)

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


#  Future date validation
def validate_no_future_date(data):
    if data > date.today():
        raise ValidationError("Date cannot be in the future.")


#  Image resolution validation
def validate_image_resolution(image):
    with Image.open(image) as img:
        width, height = img.size
        if width != 300 or height != 300:
            raise ValidationError(
                f"Image resolution should be at 300x300. Got {width}x{height}"
            )


#  Image resolution extension
def validate_image_extension(image):
    ext = os.path.splitext(image.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Invalid file extension, use .png or .jpg image extension.'
        )


#  Change filename image
def change_filename(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = '{}_{}.{}'.format(instance.company_name, instance.id, ext)
    return os.path.join('logo/company/', new_filename)
