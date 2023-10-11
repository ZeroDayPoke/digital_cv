#!/usr/bin/env python3

from wtforms.validators import ValidationError
from wtforms.fields import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from uuid import UUID

class MultiCheckboxField(SelectMultipleField):
    """
    A custom form field that allows multiple checkboxes to be selected.

    :param SelectMultipleField: The base class for the field.
    :type SelectMultipleField: class
    """
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

    def process_formdata(self, valuelist):
        """
        Process the form data for the field.

        :param valuelist: A list of values to process.
        :type valuelist: list
        """
        if valuelist:
            self.data = [str(UUID(x)) for x in valuelist]
        else:
            self.data = []

    def process_data(self, value):
        """
        Process the data for the field.

        :param value: The value to process.
        :type value: any
        """
        if value:
            self.data = [str(x) for x in value]
        else:
            self.data = []

def at_least_one_checkbox(form, field):
    """
    Validates that at least one checkbox is checked in a given field.

    Args:
        form: The form object.
        field: The field to be validated.

    Raises:
        ValidationError: If no checkbox is checked.
    """
    if not any(field.data):
        raise ValidationError("At least one checkbox should be checked.")
