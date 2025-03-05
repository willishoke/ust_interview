from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RPC_Server:
    # Initialize RPC server with supplied parameters
    def __init__(self, hostname: str, port: int, request_handler: SimpleXMLRPCRequestHandler):
        self.server = SimpleXMLRPCServer((hostname, port), requestHandler=request_handler)
        self.server.register_introspection_functions()
    
    # Register a function to be executed on the RPC
    def register_function(self, func):
        if not self.server:
            return
        self.server.register_function(func)
    
    # Start server
    def start(self):
        self.server.serve_forever()

