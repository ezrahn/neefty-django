from django.db import models
from django.forms import ModelForm
from neefty.models import Dimension, ListItem

class DimensionForm(ModelForm):
    class Meta:
        model = Dimension

class ListItemForm(ModelForm):
    class Meta:
        model = ListItem
        
        