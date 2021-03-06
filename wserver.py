import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket

  
class WebSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'connection opened'

     
    def write_message(self, message):
        self.write_message("Hey! the server is working")
    
    def on_close(self):
       print 'connection closed'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
        (r'/ws',  WebSHandler),
        ])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9000)
    myIP = socket.gethostbyname(socket.gethostname())


    tornado.ioloop.IOLoop.instance().start()
