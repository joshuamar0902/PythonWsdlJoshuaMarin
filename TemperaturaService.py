from spyne import Application, Int, Integer, rpc, ServiceBase, Unicode, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class TempConversionService(ServiceBase):
    @rpc(Integer, _returns=Integer)
    def celsius_to_fahrenheit(ctx, celsius):
        fahrenheit = (celsius * (9/5)) + 32
        return fahrenheit

    @rpc(Integer, _returns=Integer)
    def fahrenheit_to_celsius(ctx, fahrenheit):
        celsius = (fahrenheit - 32) * (9/5)
        return celsius

    @rpc(Integer, _returns=Integer)
    def fahrenheit_to_kelvin(ctx, fahrenheit):
        kelvin = (fahrenheit - 32) * (9/5) + 273.15
        return kelvin


# Crea la aplicación con el servicio y el protocolo SOAP
application = Application(
    [TempConversionService],
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