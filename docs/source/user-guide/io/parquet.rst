.. Licensed to the Apache Software Foundation (ASF) under one
.. or more contributor license agreements.  See the NOTICE file
.. distributed with this work for additional information
.. regarding copyright ownership.  The ASF licenses this file
.. to you under the Apache License, Version 2.0 (the
.. "License"); you may not use this file except in compliance
.. with the License.  You may obtain a copy of the License at

..   http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing,
.. software distributed under the License is distributed on an
.. "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
.. KIND, either express or implied.  See the License for the
.. specific language governing permissions and limitations
.. under the License.

.. _io_parquet:

Parquet
=======

It is quite simple to read a parquet file using the :py:func:`~datafusion.context.SessionContext.read_parquet` function.

.. code-block:: python

    from datafusion import SessionContext

    ctx = SessionContext()
    df = ctx.read_parquet("file.parquet")

An alternative is to use :py:func:`~datafusion.context.SessionContext.register_parquet`

.. code-block:: python

    ctx.register_parquet("file", "file.parquet")
    df = ctx.table("file")
