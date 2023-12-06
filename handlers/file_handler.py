from tornado.web import StaticFileHandler


class FileHandler(StaticFileHandler):
    def set_default_headers(self):
        print("FILE HANDLER")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, authorization")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
