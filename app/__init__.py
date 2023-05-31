import os
import aiohttp_jinja2
from app.manage import create_app
from aiohttp import web
import jinja2

app= create_app()

from app.resource.extract import Upload, Index, Download

app.router.add_view('/', Index)
app.router.add_view('/upload',Upload)
app.router.add_view('/download', Download)
