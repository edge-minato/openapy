# Split files

Let's try the most basic function of `Openapy` that is splitting each function into files. Copy and save the following two files, and execute the `openapy.sh`.

```
.
├── apis
│   └── source.py
└── openapy.sh
```

```python
# ./apis/source.py
def function_a(name: str, age: int) -> None:
    pass


def function_b(height: int, weight: int) -> int:
    pass
```

```sh
# ./openapy.sh
docker run --rm -v "$PWD:/src" edgem/openapy \
openapy --src /src/apis

sudo chown $USER:$USER processor -R
```

As the result of above docker command, `./processor` directory is generated beside of `./aps`. The `./processor` directory contains two files for each function.

```
.
├── apis
│   └── source.py
└── processor
    ├── process_function_a.py
    └── process_function_b.py
```

```python
# coding: utf-8

# function_a.py
def function_a(name: str, age: int) -> None:

    # implement me
    ...
```

```python
# coding: utf-8

# function_b.py
def function_b(height: int, weight: int) -> int:

    # implement me
    ...
```

With this very first tutorial, there is no functional relations between `./apis/source.py` and `./processor/function_x.py`. We are going to do that in the next tutorial.
