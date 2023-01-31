import os
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError

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


#  Image resolution extension
def validate_image_extension(image):
    ext = os.path.splitext(image.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Invalid file extension, use .png or .jpg image extension.'
        )


#  Future date validation
def validate_no_future_date(data):
    if data > date.today():
        raise ValidationError("Date cannot be in the future.")
