```
 ██████╗ ██████╗ ███████╗███╗   ██╗ █████╗ ██████╗ ██╗   ██╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████║██████╔╝ ╚████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║██╔═══╝   ╚██╔╝
╚██████╔╝██║     ███████╗██║ ╚████║██║  ██║██║        ██║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝        ╚═╝
```


[![pypi version](https://img.shields.io/pypi/v/openapy.svg?style=flat)](https://pypi.org/pypi/openapy/)
[![python versions](https://img.shields.io/pypi/pyversions/openapy.svg?style=flat)](https://pypi.org/pypi/openapy/)
[![license](https://img.shields.io/pypi/l/openapy.svg?style=flat)](https://github.com/edge-minato/openapy/blob/master/LICENSE)
[![Unittest](https://github.com/edge-minato/openapy/actions/workflows/unittest.yml/badge.svg)](https://github.com/edge-minato/openapy/actions/workflows/unittest.yml)
[![codecov](https://codecov.io/gh/edge-minato/openapy/branch/main/graph/badge.svg?token=YDZAMKUNS0)](https://codecov.io/gh/edge-minato/openapy)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black")
[![Downloads](https://pepy.tech/badge/openapy)](https://pepy.tech/project/openapy)
[![Downloads](https://pepy.tech/badge/openapy/week)](https://pepy.tech/project/openapy)

`openapy` adds CI/CD capability to [OpenAPI generator](https://github.com/OpenAPITools/openapi-generator)


## Overview

## Quick start

### With Docker

```
docker run
```

### With Installation

```
pip install openapy
```

## USAGE

```
> openapy -h
usage: openapy [-h] [--src SRC] [--template TEMPLATE] [--all] [--version]

Additional files generator for openapi

options:
  -h, --help            show this help message and exit
  --src SRC, -s SRC     source dir path
  --template TEMPLATE, -t TEMPLATE
                        file path of the processor template
  --all, -a             whether overwrite all files or not
  --version, -v         show version
```

## Options

(*) means it is a required option.

- **src** (*): Path to the source directory that contains apis
- **template**: Path to the custom template file
- **all**: With this option, all files will be overwritten

## Custom Template

Following variables with `{}` brackets are available.

- **IMPORTS**: All of imports of the source file like `import X`, `from X import Y`
- **ASSIGNS**: All assigns of the source file like `var = "string"`
- **DEF**: `async def` or `def` of the function
- **NAME**: The function name
- **ARGS**: Arguments of the function with type annotations
- **RETURN_TYPE**: A type annotation for the return of the function
- **COMMENT**: A comment inside of the function
- **BODY**: A body of the function, like assign statement
- **RETURN**: A return statement of the function


### Example


**apis/user_api.py**

```python
from typing import Any, Dict, List, Optional, Union  # noqa: F401
from fastapi import APIRouter
from openapi_server.model.user import User

router = APIRouter()

@router.post("/get_user", tags=["user"], summary="get user")
async def get_user(id: int) -> User:
    """This function returns a new user"""
    return processor.get_user.process()

@router.post("/delete_user", tags=["user"], summary="delete user")
async def delete_user(id: int, password:str="default_password") -> bool:
    """This function deletes user and return the result"""
    return processor.delete_user.process()
```

**Custom Template: template.txt**

```
# coding: utf-8

{IMPORTS}

def process({ARGS}) -> {RETURN_TYPE}:
    # Implement me!
    ...
```

**processor/get_user.py**

```python
# coding: utf-8

from typing import Any, Dict, List, Optional, Union  # noqa: F401
from fastapi import APIRouter  # noqa: F401
from openapi_server.model.user import User  # noqa: F401

def process(id: int) -> User:
    # Implement me!
    ...
```

**processor/delete_user.py**

```python
# coding: utf-8

from typing import Any, Dict, List, Optional, Union  # noqa: F401
from fastapi import APIRouter  # noqa: F401
from openapi_server.model.user import User  # noqa: F401

def process(id: int) -> User:
    # Implement me!
    ...
```
