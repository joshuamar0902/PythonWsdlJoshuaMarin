from spyne import Application, Int, Integer, rpc, ServiceBase, Unicode, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculadoraService(ServiceBase):
    @rpc(Integer,Integer, _returns=Integer)
    def suma(ctx, a,b):
        return a+b

    @rpc(Integer,Integer, _returns=Integer)
    def resta(ctx, a,b):
        return a-b

    @rpc(Integer,Integer, _returns=Integer)
    def multiplicacion(ctx, a,b):
        return a*b
    
    @rpc(Integer,Integer, _returns=Integer)
    def division(ctx, a,b):
        return a/b


# Crea la aplicación con el servicio y el protocolo SOAP
application = Application(
    [CalculadoraService],
    tns='mi.tempspace',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Expón el servicio por WSGI en el puerto 8000
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, WsgiApplication(application))
    print("Servicio SOAP en http://0.0.0.0:8000")
    server.serve_forever()