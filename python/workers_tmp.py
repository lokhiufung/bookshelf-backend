# myproject/workers.py
# https://github.com/encode/uvicorn/issues/816#issuecomment-751998254

from uvicorn.workers import UvicornWorker


class MyUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {"loop": "auto", "http": "auto"}
