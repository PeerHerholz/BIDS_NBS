============
Installation
============

In general, there are two distinct ways to install and use ``bidsnbs``:
either through virtualization/container technology, that is `Docker`_ or
`Singularity`_, or in a `Bare metal version (Python 3.10+)`_.
Once you are ready to run ``bidsnbs``, see `Usage <https://peerherholz.github.io/bidsnbs/usage>`_ for details.

Docker
======

In order to run ```bidsnbs``` in a Docker container, Docker must be `installed
<https://docs.docker.com/engine/installation/>`_ on your system.
Once Docker is installed, you can get ``bidsnbs`` through  running one of the following
commands in the terminal of your choice.

Option 1: pulling from the `dockerhub registry <https://hub.docker.com/repository/docker/peerherholz/bidsnbs/general>`_ :


.. code-block:: bash

    docker pull peerherholz/bidsnbs:version

Option 2: pulling from the `github container registry <https://github.com/PeerHerholz/bidsnbs/pkgs/container/bidsnbs>`_ :

.. code-block:: bash

    docker pull ghcr.io/peerherholz/bidsnbs:version

Where ``version`` is the specific version of ``bidsnbs`` you would like to use. For example, if you want 
to employ the ``latest``/most up to date ``version`` you can either run 

.. code-block:: bash

    docker pull peerherholz/bidsnbs:latest

.. code-block:: bash

    docker pull ghcr.io/peerherholz/bidsnbs:latest

or the same command withouth the ``:latest`` tag, as ``Docker`` searches for the ``latest`` tag by default.
However, as the ``latest`` version is subject to changes and not necessarily in synch with the most recent ``numbered version``, it 
is recommend to utilize the latter to ensure reproducibility. For example, if you want to employ ``bidsnbs v0.0.1`` the command would look as follows:

.. code-block:: bash

    docker pull peerherholz/bidsnbs:v0.0.1

.. code-block:: bash

    docker pull ghcr.io/peerherholz/bidsnbs:v0.0.1

After the command finished (it may take a while depending on your internet connection),
you can run ``bidsnbs`` like this:

.. code-block:: bash

    $ docker run -ti --rm \
        -v path/to/save/bidsnbs:/bidsnbs_dataset \
        -v path/to/nbs/file:/nbs_file
        peerherholz/bidsnbs:latest \
        /bidsnbs_dataset \
        nbs_file
        

Please have a look at the examples under `Usage <https://peerherholz.github.io/bidsnbs/usage>`_ to get more information
about and familiarize yourself with ``bidsnbs``'s functionality.

Singularity
===========

For security reasons, many HPCs (e.g., TACC) do not allow Docker containers, but support
allow `Singularity <https://github.com/singularityware/singularity>`_ containers. Depending
on the ``Singularity`` version available to you, there are two options to get ``bidsnbs`` as
a ``Singularity image``.

Preparing a Singularity image (Singularity version >= 2.5)
----------------------------------------------------------
If the version of Singularity on your HPC is modern enough you can create a ``Singularity
image`` directly on the HCP.
This is as simple as: 

.. code-block:: bash

    $ singularity build /my_images/bidsnbs-<version>.simg docker://peerherholz/bidsnbs:<version>

Where ``<version>`` should be replaced with the desired version of ``bidsnbs`` that you want to download.
For example, if you want to use ``bidsnbs v0.0.4``, the command would look as follows.

.. code-block:: bash

    $ singularity build /my_images/bidsnbs-v0.0.4.simg docker://peerherholz/bidsnbs:v0.0.4


Preparing a Singularity image (Singularity version < 2.5)
---------------------------------------------------------
In this case, start with a machine (e.g., your personal computer) with ``Docker`` installed and
the use `docker2singularity <https://github.com/singularityware/docker2singularity>`_ to
create a ``Singularity image``. You will need an active internet connection and some time. 

.. code-block:: bash

    $ docker run --privileged -t --rm \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /absolute/path/to/output/folder:/output \
        singularityware/docker2singularity \
        peerherholz/bidsnbs:<version>

Where ``<version>`` should be replaced with the desired version of ```bidsnbs``` that you want
to download and ``/absolute/path/to/output/folder`` with the absolute path where the created ``Singularity image``
should be stored. Sticking with the example of ``bidsnbs v0.0.4`` this would look as follows:

.. code-block:: bash

    $ docker run --privileged -t --rm \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /absolute/path/to/output/folder:/output \
        singularityware/docker2singularity \
        peerherholz/bidsnbs:v0.0.4

Beware of the back slashes, expected for Windows systems. The above command would translate to Windows systems as follows:

.. code-block:: bash

    $ docker run --privileged -t --rm \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v D:\host\path\where\to\output\singularity\image:/output \
        singularityware/docker2singularity \
        peerherholz/bidsnbs:<version>


You can then transfer the resulting ``Singularity image`` to the HPC, for example, using ``scp``. ::

    $ scp peerherholz_bidsnbs<version>.simg <user>@<hcpserver.edu>:/my_images

Where ``<version>`` should be replaced with the version of ``bidsnbs`` that you used to create the ``Singularity image``, ``<user>``
with your ``user name`` on the HPC and ``<hcpserver.edu>`` with the address of the HPC.  

Running a Singularity Image
---------------------------

.. code-block:: bash

    $ singularity run --cleanenv /my_images/bidsnbs-<version>.simg \
       bidsnbs_dataset nbs_file

.. note::

    Make sure to check the name of the created ``Singularity image`` as that might
    diverge based on the method you used. Here and going forward it is assumed that you used ``Singularity >= 2.5``
    and thus ``bidsnbs-<version>.simg`` instead of ``peerherholz_bidsnbs<version>.simg``.   


.. note::

   Singularity by default `exposes all environment variables from the host inside
   the container <https://github.com/singularityware/singularity/issues/445>`_.
   Because of this your host libraries (such as nipype) could be accidentally used
   instead of the ones inside the container - if they are included in ``PYTHONPATH``.
   To avoid such situation we recommend using the ``--cleanenv`` singularity flag
   in production use. For example: ::

    $ singularity run --cleanenv /my_images/bidsnbs-<version>.simg \
       bidsnbs_dataset nbs_file


   or, unset the ``PYTHONPATH`` variable before running: ::

    $ unset PYTHONPATH; singularity /my_images/bidsnbs-<version>.simg \
       bidsnbs_dataset nbs_file

.. note::

   Depending on how ``Singularity`` is configured on your cluster it might or might not
   automatically ``bind`` (``mount`` or ``expose``) ``host folders`` to the container.
   If this is not done automatically you will need to ``bind`` the necessary folders using
   the ``-B <host_folder>:<container_folder>`` ``Singularity`` argument.
   For example: ::

    $ singularity run --cleanenv -B path/to/bidsnbs/on_host:/bidsnbs \
        /my_images/bidsnbs-<version>.simg \
        bidsnbs_dataset nbs_file

Bare metal version (Python 3.10+)
===========================================

``bidsnbs`` is written using Python 3.10 (or above).
Until the first official version/release will be provided, `bidsnbs`'s bare metal version can be installed by opening a terminal and running the following:

.. code-block:: bash

    git clone https://github.com/peerherholz/bidsnbs.git
    cd bidsnbs
    pip install .

Please note that you need to have at least `Python 3.10` installed.

Check your installation with the ``--version`` argument:

.. code-block:: bash

    $ bidsnbs --version
