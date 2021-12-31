import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World this is a python command executed from the backend.")


class resourceParameRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        print(studentName)
        self.write(f"Welcome {studentName} the course you are viewing is {courseId}")


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
        #lis of all endpoint
        (r"/", basicRequestHandler), #r Rest point
        (r"/animal", listRequestHandler),
        (r"/isEven", queryParamRequestHandler), #to query we need to use route "/isEven?num=4"
        (r"/students/([A-Z]+[a-z]+)/([0-9])+", resourceParameRequestHandler),
        #"[a-z]+" capture more than 1 letter #"[0-9]+" capture numbers
        #the above only capture lower case words
    ])
    
    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()