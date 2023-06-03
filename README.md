# CBF - Class Based FastApi

## Description:
Allows to use fast api apps and routers as classed, via aiohttp offered structure.
This architecture allows you to use instance dependencies in handlers.

## Simple example:

```python
from cbf import Cb, CbRouter, CbApp

class SomeRouter2(CbRouter):
    def __init__(self, dependency: str):
        self.dependency = dependency

    @Cb.get(path='/test')
    def get(self):
        print(self.dependency)
        return f'SomeRouter 2 works'

class SomeRouter(CbRouter):
    @Cb.get(path='/test')
    def get(self, string: str):
        return f'SomeRouter 1 works; {string}'

class RestApp(CbApp):
    def __init__(self, some_router: SomeRouter, router_two: SomeRouter2):
        self.mount_router('/router1', some_router)
        self.mount_router('/router2', router_two)

    @Cb.get(path='/root')
    def get(self):
        return 'root works'

entrypoints = RestApp(
    SomeRouter(),
    SomeRouter2('router 2 string')
)

import uvicorn
uvicorn.run(entrypoints.app, host='127.0.0.1', port=8000)
```
