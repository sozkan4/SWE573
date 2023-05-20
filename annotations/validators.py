from django.core.exceptions import ValidationError

def validate_annotation_type(value):
    valid_types = ["Note", "Comment"]  # Add more valid annotation types if needed
    if value not in valid_types:
        raise ValidationError("Invalid annotation type.")
