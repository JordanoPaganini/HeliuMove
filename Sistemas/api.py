from ninja import Router
from .models import Dados, Sistemas
from typing import List
from .utils import PostDataSchema

router = Router(tags=['Dados'])

@router.post('dados')
def cadastro_dados(request, data: List[PostDataSchema]):
    # Save data on Dados model
    id = request.headers['ClientID']
    sistema = Sistemas(id=id)
    for i in data:
        Dados(sistema=sistema, temp=i.temp, voltage=i.voltage, current=i.current).save()
    return 'Data saved'

@router.get('ping')
def ping(request):
    return 'Pong'