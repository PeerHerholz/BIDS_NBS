.. _usage:

======
Usage
======



Execution and the BIDS format
=============================

The general usage of ``bidsnbs`` is rather straightforward as it only requires the user to go through two steps: 1. Preparing the ``NBS metadata``
and 2. run the ``conversion function`` to adapt and/or add respective ``BIDS NBS`` ``metadata`` and ``tsv`` files to already `BIDS`-compliant datasets.
The exact command to run ``bidsnbs`` depends on the Installation method and user. Regarding the latter ``bidsnbs`` 
can either be used as a ``command line tool`` or directly within ``python``. Please refer to the `Tutorial <https://peerherholz.github.io/bidsnbs/walkthrough>`_ for a more detailed walkthrough.

Please be aware that users need to fill out the generated ``template`` files manually by adding the respective information based on their setup and experiment.
ou can use any text editor capable of reading and writing ``json`` files to open the file, fill in the information
and save it. Examples are `VScode <https://code.visualstudio.com/>`_, `Atom <https://atom-editor.cc/>`_, `PyCharm <https://www.jetbrains.com/pycharm/>`_ and `Sublime <https://www.sublimetext.com/index2>`_ 
(`RStudio <https://www.rstudio.com/categories/rstudio-ide/>`_ and `Matlab <https://mathworks.com/products/matlab.html>`_ should also work).
For more information on the ``NBS template files``, please have a look `here <https://peerherholz.github.io/bidsnbs/NBS_files>`_.

Here's a very conceptual example of running ``bidsnbs`` via ``CLI``: ::

    bidsnbs path/to/BIDS/dataset --get_nbs_files
    bidsnbs path/to/BIDS/dataset nbs_files optional_arguments

and here from within ``python``: ::

    bids_dataset = "path/to/BIDS/dataset"

    from bidsnbs.nbs_files import get_nbs_files
    from bidsnbs.conversion import bids2nbs

    nbs_files = get_nbs_files(bids_dataset)

    bidsnbs = bids2nbs(bids_path=bids_dataset, nbs_path=nbs_files,
                        optional_arguments)

Below, we will focus on the ``CLI`` version. Thus, if you are interested in using ``bidsnbs`` directly within ``python``,
please check the `Examples <https://peerherholz.github.io/bidsnbs/auto_examples/index>`_.

Changing files in-place vs new BIDS dataset
==============================================

As ``bidsnbs`` adapts ``BIDS``-compliant datasets to be ``BIDS-NBS`` compliant, already existing files, ie ``events`` and ``sessions``, need
to be adapted by adding/changing ``columns`` (in ``tsv`` files) and ``metadata`` (in ``json`` files). To facilitate this conversion and data version control,
users have two options to run ``bidsnbs``:

1. change files in-place by running ``bidsnbs`` without the ``--new_bids_dir`` argument
2. created a new ``BIDS`` dataset by running ``bidsnbs`` with the ``--new_bids_dir`` argument, specifying a respective path

In case of 2., the already existing ``BIDS`` dataset will be copied to the ``path`` specified via ``--new_bids_dir`` and files will only
be change there. The original ``BIDS`` dataset will not be changed in any way or form.

Currently, there is no recommendation on which option to use but users have to decide based on their given case, aim and setup.

Independent of the use case, each file that is going to be adapted by ``bidsnbs``, ie the ``events`` and `session`` files, will be backed up
to `sourcedata/BIDS_pre_NBS_backup/` so that they are not lost and can be brought back into the ``BIDS`` dataset if needed (e.g. if something
went wrong during the conversion).

Command-Line Arguments
======================
.. argparse::
  :ref: bidsnbs.bidsnbs_cli.get_parser
  :prog: bidsnbs
  :nodefault:
  :nodefaultconst:

Example Call(s)
---------------

Below you'll find two examples calls that hopefully help
you to familiarize yourself with ``bidsnbs`` and its options.

Example 1
~~~~~~~~~

Step 1: Creating the NBS metadata files


.. code-block:: bash

    bidsnbs \
    /home/user/BIDS_dataset
    --get_nbs_files

Here's what's in this call:

- The 1st positional argument is the directory the `BIDS`-compliant dataset is stored in (e.g. ``/home/user``)
- The 2nd positional argument indicates that we would like to get the `NBS metadata file` templates, which stored in a `NBS` 
  directory that will be created in the `sourcedata/` directory of the `BIDS`-dataset (e.g. ``/home/user/BIDS_dataset/sourcedata/NBS``)

The `NBS metadata` templates then need to filled with the respective information for a given study and can then
be used in the second step. You can use any text editor capable of reading and writing ``json`` files to open the file, fill in the information
and save it. 

Step 2: Running the NBS conversion 

.. code-block:: bash

    bidsnbs \
    /home/user/BIDS_dataset
    /home/user/nbs_file

Here's what's in this call:

- The 1st positional argument is the directory the BIDS-compliant dataset is stored in (e.g. ``/home/user``)
- The 2nd positional argument is the directory the NBS file is stored in (e.g. ``/home/user``)

After the command finished, the ``events.tsv`` and ``sessions.tsv`` files should have new ``columns`` and respective values and
the ``events.json`` and ``sessions.json`` files new/adapted ``metadata``, based on the information provided in the ``NBS template files``.

Example 2
~~~~~~~~~

.. code-block:: bash

    bidsnbs \
    /home/user/BIDS_dataset
    /home/user/nbs_file
    --new_BIDS_dataset /home/user/new_BIDS_dataset

Here's what's in this call:

- The 1st positional argument is the directory the `BIDS`-compliant dataset is stored in (e.g. ``/home/user``)
- The 2nd positional argument is the directory the `NBS file` is stored in (e.g. ``/home/user``)
- The 3rd positional argument specifies that a new `BIDS dataset` should be created, ie instead of adapting and/or adding `metadata` in the original
  dataset, a respective new dataset will be created by copying the original to the indicated path and then applying the `metadata` conversion.
  Here, it a new `BIDS dataset` will be created under `/home/user`

After the command finished, the ``events.tsv`` and ``sessions.tsv`` files should have new ``columns`` and respective values and
the ``events.json`` and ``sessions.json`` files new/adapted ``metadata``, based on the information provided in the ``NBS template files``.

Support and communication
=========================

The documentation of this project is found here: https://peerherholz.github.io/bidsnbs.

All bugs, concerns and enhancement requests for this software can be submitted here:
https://github.com/peerherholz/bidsnbs/issues.

If you have a problem or would like to ask a question about how to use ``bidsnbs``,
please submit a question to `NeuroStars.org <http://neurostars.org/tags/bidsnbs>`_ with an ``bidsnbs`` tag.
NeuroStars.org is a platform similar to StackOverflow but dedicated to neuroinformatics.

All previous ``bidsnbs`` questions are available here:
http://neurostars.org/tags/bidsnbs/

Not running on a local machine? - Data transfer
===============================================

Please contact you local system administrator regarding
possible and favourable transfer options (e.g., `rsync <https://rsync.samba.org/>`_
or `FileZilla <https://filezilla-project.org/>`_).

A very comprehensive approach would be `Datalad
<http://www.datalad.org/>`_, which will handle data transfers with the
appropriate settings and commands.
Datalad also performs version control over your data.