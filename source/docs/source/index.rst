.. ComPDFKit API Libraries documentation master file, created by
   sphinx-quickstart on Mon Aug 21 10:43:57 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ComPDFKit API Libraries's documentation!
===================================================

ComPDFKit API provides a variety of Python API tools that allow you to create an efficient document processing workflow
in a single API call. Try our various APIs for free — no credit card required.

Requirements
------------

Programming Environment: Python 3.8 and higher.

Installation
------------

You can install the library via pip. Run the following command:

.. code-block:: bash

    pip install compdfkit-api-python

Create API Client
-----------------

You can use your publicKey and secretKey to complete the authentication. You need to sign in your ComPDFKit API account
to get your publicKey and secretKey at the dashboard.
If you are new to ComPDFKit, click here to sign up for a free trial.

.. code-block:: python

        # Create a client
         client = CPDFClient(public_key, secret_key)

Create Task
-----------

A task ID is automatically generated for you based on the type of PDF tool you choose.
You can provide the callback notification URL.
After the task processing is completed, we will notify you of the task result through the callback interface.
You can perform other operations according to the request result,
such as checking the status of the task, uploading files, starting the task, or downloading the result file.

.. code-block:: python

         # Create a client
         client = CPDFClient(public_key, secret_key)

         # Create a task
         # Create an example of a PDF TO WORD task
         create_task_result = client.create_task(CPDFConversionEnum.PDF_TO_WORD)

         # Get a task id
         task_id = create_task_result.task_id

Upload Files
------------

Upload the original file and bind the file to the task ID.
The field parameter is used to pass the JSON string to set the processing parameters for the file.
Each file will generate automatically a unique filekey.
Please note that a maximum of five files can be uploaded for a task ID and no files can be uploaded for that task after
it has started.

.. code-block:: python

         # Create a client
         client = CPDFClient(public_key, secret_key)

         # Create a task
         # Create an example of a PDF TO WORD task
         create_task_result = client.create_task(CPDFConversionEnum.PDF_TO_WORD)

         # Get a task id
         task_id = create_task_result.task_id

         # Upload files
         client.upload_file(convert_file, task_id)

Execute the task
----------------

After the file upload is completed, call this interface with the task ID to process the files.

.. code-block:: python

         # Create a client
         client = CPDFClient(public_key, secret_key)

         # Create a task
         # Create an example of a PDF TO WORD task
         create_task_result = client.create_task(CPDFConversionEnum.PDF_TO_WORD)

         # Get a task id
         task_id = create_task_result.task_id

         # Upload files
         client.upload_file(convert_file, task_id)

         # execute Task
         client.execute_task(task_id)

Get Task Info
-------------

Request task status and file-related meta data based on the task ID.

.. code-block:: python

         # Create a client
         client = CPDFClient(public_key, secret_key)

         # Create a task
         # Create an example of a PDF TO WORD task
         create_task_result = client.create_task(CPDFConversionEnum.PDF_TO_WORD)

         # Get a task id
         task_id = create_task_result.task_id

         # Upload files
         client.upload_file(convert_file, task_id)

         # execute Task
         client.execute_task(task_id)

         # Query TaskInfo
         task_info = client.get_task_info(task_id)

Reporting Problems
------------------

Thanks for your interest in the ComPDFKit API! The ComPDFKit API provides an excellent set of document processing tools,
enabling your developers to easily integrate PDF rendering capabilities into your applications,
providing your users with an efficient and high-quality document experience.
If you encounter any technical questions or bug issues when using ComPDFKit API,
please submit the problem report to the ComPDFKit team. More information as follows would help us to solve your problem:

* The version of the ComPDFKit API you are currently using.
* Your operating system and IDE version.
* Detailed description of the problem.
* Any other related information, such as screenshots of errors.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`


