from ninja import ModelSchema
from .models import Dados

class PostDataSchema(ModelSchema):
    class Meta:
        model = Dados
        fields  = ['temp', 'voltage', 'current']