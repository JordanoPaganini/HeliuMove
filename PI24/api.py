from ninja import NinjaAPI
from ninja.parser import Parser
from ninja.renderers import BaseRenderer
import orjson

class ORJsonParser(Parser):
    def parsy_body(self, request):
        return orjson.loads(request.body)
    
class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)
    
api = NinjaAPI(version='1.5.0', parser=ORJsonParser(), renderer=ORJSONRenderer(), docs_url=None)

api.add_router('', 'Sistemas.api.router')
