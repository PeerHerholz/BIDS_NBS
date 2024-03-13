.. _usage:

==========
Usage
==========



Execution and the BIDS format
=============================

The general usage of ``bidsnbs`` is rather straightforward as it only requires the user to go through two steps: 1. Preparing the `NBS metadata` 
and 2. run the `conversion function` to adapt and/or add respective `BIDS NBS` `metadata` to already `BIDS`-compliant datasets.
The exact command to run ``bidsnbs`` depends on the Installation method and user. Regarding the latter ``bidsnbs`` 
can either be used as a ``command line tool`` or directly within ``python``. Please refer to the `Tutorial <../../>`_ for a more detailed walkthrough.

Here's a very conceptual example of running ``bidsnbs`` via ``CLI``: ::

    bidsnbs path/to/BIDS/dataset --get_nbs_files
    bidsnbs path/to/BIDS/dataset nbs_file optional_arguments

and here from within ``python``: ::

    bids_dataset = "path/to/BIDS/dataset"

    from bidsnbs.nbs_files import get_nbs_files
    from bidsnbs.conversion import bids2nbs

    nbs_files = get_nbs_files(bids_dataset)

    bids_nbs = bids2nbs(bids_path=bids_dataset, nbs_path=nbs_files,
                        optional_arguments)

Below, we will focus on the ``CLI`` version. Thus, if you are interested in using ``bidsnbs`` directly within ``python``,
please check the `Examples <../../>`_.

Changing metadata in-place vs new BIDS dataset
==============================================


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
be used in the second step.

Step 2: Running the NBS conversion 

.. code-block:: bash

    bidsnbs \
    /home/user/BIDS_dataset
    /home/user/nbs_file

Here's what's in this call:

- The 1st positional argument is the directory the BIDS-compliant dataset is stored in (e.g. ``/home/user``)
- The 2nd positional argument is the directory the NBS file is stored in (e.g. ``/home/user``)

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