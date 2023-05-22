import traceback

import aiohttp_jinja2
import jinja2
from aiohttp import web
import zipfile

def extract_zip(zip_file):
    extracted_files=[]
    with zipfile.ZipFile(zip_file,'r') as f:
        for file_name in f.namelist():
            extracted_files.append(file_name)
            f.extract(file_name)
    return extracted_files
# from app import logger
# from app.service.random_string.generate_v1 import RandomStringGeneratorV1

class Index(web.View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        return {}

class Upload(web.View):
    @aiohttp_jinja2.template('upload.html')
    async def post(self):
        data = await self.request.post()
        file=data['file'].file

        extracted_files=extract_zip(file)
        return {'extracted_files' : extracted_files}


import os
from aiohttp import web


class Download(web.View):
    async def get(self):
        file = self.request.query.get('file')
        filepath = os.path.join(os.getcwd(), file)

        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                content = f.read()

            headers = {
                'Content-Disposition': f'attachment; filename="{file}"'
            }

            return web.Response(body=content, headers=headers)
        else:
            return web.Response(text=f'File not found: {file}', status=404)
