import os
import json

from handlers.base_handler import BaseHandler


class GetImageHandler(BaseHandler):
    async def get(self, image_dir):
        path_images = f"{os.path.abspath('')}\data\imgs\{image_dir}".replace("\\",'/', 10)
        images = [*os.listdir(path_images)]
        await self.render('showimage.html', image_dir=path_images, images=images)
