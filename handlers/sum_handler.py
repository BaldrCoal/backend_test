import os
import json

from handlers.base_handler import BaseHandler


class SumHandler(BaseHandler):
    async def get(self):

        # self.set_header('Content-Type', 'application/json')

        a = int(self.get_argument('a'))
        b = int(self.get_argument('b'))

        c = a + b

        answer = {"result": c}

        await self.finish(json.dumps(answer))
