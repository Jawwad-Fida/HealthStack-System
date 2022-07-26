from django.db import models

#import uuid

# Create your models here.

# django automatically creates an id field for each model (int)
# null=True --> don't require a value when inserting into the database
# blank=True --> allow blank value when submitting a form
# auto_now_add --> automatically set the value to the current date and time
# unique=True --> prevent duplicate values
# primary_key=True --> set this field as the primary key
# editable=False --> prevent the user from editing this field
