Overview
===================================
`Openapy` simplifies continuous development with `OpenAPI Generator <https://github.com/OpenAPITools/openapi-generator>`_.
What this tool does is read python source files and copy functions into individual files.
This will prevent the openapi generator from overwriting the code you have written.


Installation
===================================
Docker image is available: `Openapy  <https://github.com/edge-minato/openapy>`_

:code:`poetry add -D openapy` or :code:`pip install openapy`



Quick Start
===================================
**Prerequisite**: Source code are generated with OpenAPI Generator.

:code:`docker run -v ${PWD}:/src edgem/openapy openapy --src src/openapi-server/apis`

Copied files per function are generated under `src/openapi-server/processor`.

.. code-block:: python

   # src/openapi-server/processor/get_pet.py
   import sys
   print(sys.path)

Content
===================================

.. toctree::
   :maxdepth: 2

   pages/examples/index
   pages/template/index
