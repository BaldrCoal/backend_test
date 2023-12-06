
import tornado.web

from handlers.index_handler import IndexHandler
from handlers.sum_handler import SumHandler
# from handlers.generate_handler import GenerateHandler
# from handlers.status_handler import StatusHandler
# from handlers.result_handler import ResultHandler
#
from handlers.file_handler import FileHandler
from handlers.download_image_handler import UploadImageHandler
from handlers.get_image_handler import GetImageHandler

urls = [
    (r'/', IndexHandler,),
    (r'/sum', SumHandler,),
    (r'/uploadimage', UploadImageHandler),
    (r'/showimage/(.*)', GetImageHandler),
    (r"/data/(.*)", FileHandler, {"path": "./data"}),
    (r"/(.*)/?", FileHandler, {"path": "./static"}),
]