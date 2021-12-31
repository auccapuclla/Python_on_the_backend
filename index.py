import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World this is a python command executed from the backend.")


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
       num = self.get_argument("num")
       if (num.isdigit()):
          r = "odd" if int(num) % 2 else "even"
          self.write(f"The integer {num} is {r}")
       else:
          self.write(f"{num} is not a valid integer.")        

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler), #r Rest point
        (r"/animal", listRequestHandler),
        (r"/isEven", queryParamRequestHandler) #to query we need to use route "/isEven?num=4"
    ])
    
    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()