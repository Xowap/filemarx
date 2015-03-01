filemarx
========

A tool to check that a directory structure conforms to a given JSON Schema.

In case of check failure, following actions can be taken, depending on your configuration:

- Output defects to the console
- Send a file listing all defects to a `Slack <https://slack.com/>`_ conference room

Installation
------------

Using pip should suffice

.. code-block:: text

   pip install filemarx

Configuration
-------------

You have to produce a JSON Schema file against which your directory's structure will be validated.
An example of this can be found in the ``samples/design.json`` file.

Let's say that your file structure is this:

.. code-block:: text

   ./anotherfile
   ./file1
   ./somedir
   ./somedir/andanother
   ./somedir/andanother/someotherfile
   ./somedir/somefilehere
   ./somedir/anotherdir
   ./file2

Then the produced JSON would be

.. code-block:: javascript

   {
       "files":[
           "anotherfile",
           "file1",
           "file2"
       ],
       "dirs":{
           "somedir":{
               "files":[
                   "somefilehere"
               ],
               "dirs":{
                   "anotherdir":{
                       "files":[
                       ],
                       "dirs":{
                       }
                   },
                   "andanother":{
                       "files":[
                           "someotherfile"
                       ],
                       "dirs":{
                       }
                   }
               }
           }
       }
   }

Usage
-----

The command takes 3 mandatory positional arguments:

1. Check name (to be set arbitrarily)
2. Schema file location
3. Directory to be checked

Example
~~~~~~~

.. code-block:: bash

   filemarx Design samples/design.json /home/myself/designs


State-keeping options
~~~~~~~~~~~~~~~~~~~~~

If you run ``filemarx`` in a cron but you don't want errors to come up every minute, you can ignore
them for X seconds once discovered. This can be done with a combination of options ``-t`` which sets
a timeout (in seconds) and ``-s`` which indicate where to store the state file.

.. code-block:: bash

   # Only pop errors every hour
   filemarx -t 3600 -s /tmp/design_state.json Design samples/design.json /home/myself/designs

Pushing results to Slack
~~~~~~~~~~~~~~~~~~~~~~~~

``filemarx`` can connect to the Slack API in order to push errors to a given Slack channel. In order
to do that, you need to get an `API Token <https://api.slack.com/web>`_, then use options
``--slack-token`` and ``--slack-channels``.

.. code-block:: bash

   # Send it all to Slack
   filemarx --slack-token 'get-your-own' --slack-channels '#general,#design' -t 3600 -s /tmp/design_state.json Design samples/design.json /home/myself/designs
