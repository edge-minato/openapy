Overview
===================================
`Openapy` simplifies continuous development with `OpenAPI Generator <https://github.com/OpenAPITools/openapi-generator>`_.
What this tool does is read python source files and copy functions into individual files.
This will prevent the openapi generator from overwriting the code you have written.



Quick Start
===================================

.. code-block:: shell

   docker run -v ${PWD}:/src edgem/openapy \
   openapy generate --src src/openapi-server/apis

.. code-block::

   pip install openapy
   openapy generate --src ./openapi-server/apis

Content
===================================

.. toctree::
   :maxdepth: 2

   pages/examples/index
   pages/template/index
