from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs

fw = open('database.txt', 'w')
fw.write("testing 123")
fw.close()

class httpServerRequsetHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            if self.path == "/plants":
                lines = [line.rstrip('\n') for line in open('database.txt')]
                fw.close()

                my_data = lines
                json_string = json.dumps(my_data)

                print("JSON:", json_string)

                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(json_string, "utf-8"))
                return
            else:
                self.handle404()
                print("Oops, the page you are looking for is not here.")


       # def handlePlantsList(self):



#                self.send_response(200)
 #               self.send_header("Access-Control-Allow-Origin", "*")
  #              self.send_header("Content-type", "application/json")
   #             self.end_headers()
    #            self.wfile.write(bytes(json_string, "utf-8"))
     #           return

        def do_POST(self):
                if self.path == "/plants":
                    length = self.headers['Content-Length']
                    length = int(length)

                    body = self.rfile.read(length).decode("utf-8")
                    data = parse_qs(body)

                    message = data['message'][0]
                    print(message)

                    fw = open('database.txt', 'a')
                    message = str(message)
                    fw.write(message + "\n")
                    fw.close()


                    self.send_response(201)
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()
                else:
                    self.handle404()
        #def handlePlantsCreate(self):
        #        length = self.headers['Content-Length']
        #        length = int(length)
        #        body = self.rfile.read(length).decode("utf-8")
         #       data = parse_qs(body)

          #      message = data['message'][0]
            #    first_name = data['first_name'][0]
           #     print(message)


             #   self.send_response(201)
              #  self.send_header("Access-Control-Allow-Origin", "*")
               # self.end_headers()

        def handle404(self):
            self.send_response(404)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-type", "text/html")#name of header and value
            self.end_headers()
            self.wfile.write(bytes("<strong>Not Found</strong>", "utf-8")) #dont write just a string, http doesnt understand ordinary strings.
def main():
    listen = ("127.0.0.1", 8080)
    server = HTTPServer(listen, httpServerRequsetHandler)

    print("Listening...")
    server.serve_forever()


main()