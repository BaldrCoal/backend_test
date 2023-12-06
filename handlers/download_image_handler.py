import os
import json
import uuid
import io
from  PIL import Image

from handlers.base_handler import BaseHandler


class DownloadImageHandler(BaseHandler):

    async def post(self):
        self.set_header('Content-Type', 'application/json')

        dir_path = os.path.join("data/imgs")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        id = uuid.uuid4()
        img_path = os.path.join(f"{dir_path}/{id}")
        os.makedirs(f"{img_path}")
        img_data = self.request.files

        for num, img in enumerate(img_data["file"]):
            image = Image.open(io.BytesIO(img["body"]))
            image.save(f"{os.path.abspath(img_path)}/image{num}.png")
