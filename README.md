# openapy

`openapy` adds CI/CD capability to [OpenAPI generator](https://github.com/OpenAPITools/openapi-generator)


## How to use

### Config



```yml
- config_name:
  - src:
    - dir: "src/openapi_server/api"
    - prefix: ""
    - suffix: "_api.py"
  - dst:
    - dir: "src/openapi_server/processor"
    - prefix: ""
    - suffix: ".py"
  - template: "tests/template/per_file.j2"
  - iter: "file"
```
