# pip install spyne lxml zeep
from spyne import Application, rpc, ServiceBase, Integer, Double
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b
    
    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, a, b):
        return a * b
    
    @rpc(Integer, Integer, _returns=Integer)
    def largest_of_two(ctx, a, b):
        return max(a, b)
    
    @rpc(Integer, Integer, Integer, _returns=Integer)
    def largest_of_three(ctx, a, b, c):
        return max(a, max(b, c))
    
    @rpc(Integer, _returns=Integer)
    def square(ctx, a):
        return a * a
    
    @rpc(Integer, _returns=Integer)
    def cube(ctx, a):
        return a * a * a
    
    @rpc(Integer, Integer, Integer, _returns=Integer)
    def add_three(ctx, a, b, c):
        return a + b + c

# Create the application
application = Application([CalculatorService], 
                          tns='calculator.soap.service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Wrap the application with WSGI
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    # Deploy as a WSGI server
    server = make_server('localhost', 8000, wsgi_application)
    print("Calculator SOAP Service started at http://localhost:8000")
    print("WSDL available at http://localhost:8000/?wsdl")
    server.serve_forever()