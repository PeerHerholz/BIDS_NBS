.. _nbsfiles:

====================================
The BIDS-NBS metadata file templates
====================================

As mentioned before, one of the core aspects of ``bidsnbs`` are the ``NBS metadata template files``. 
These are based on the `BIDS NBS BEP <https://docs.google.com/document/d/1drYd7kaNbHTcYPR3T_CRDsPcEbFSV7JbJUmhMPeWMqY/edit#heading=h.4k1noo90gelw>`_ and entail the
``metadata`` outlined and proposed by this ``BEP``. Specifically, the rationale behind the ``BIDS NBS BEP`` is to add and 
adapt ``metadata`` of existing ``BIDS``-compliant datasets to make them ``BIDS NBS`` compliant, ie sufficiently capturing and describing
``NBS`` data.

To streamline and standardize the process of adapting and adding the respective ``metadata``, the ``bidsnbs`` toolbox includes
a set of ``NBS metadata template`` files that are utilized in the following manner:

1. Add the `NBS metadata template` files are added to the ``sourcedata/`` directory of an existing ``BIDS`` dataset 
2. Users fill out the respective information, ie ``values`` of the ``metadata`` ``keys`` based on their respective experiment/data
3. The files are used within the conversion of an existing ``BIDS`` dataset to an ``BIDS NBS`` dataset, the provided ``metadata`` information is added/apdated
   in the ``metadata`` files of the existing ``BIDS`` dataset 

There are two different types of ``BIDS-NBS metadata files``: ``events.tsv`` and ``sessions.tsv``. 
While the former have to be adapted for each file in a given ``subject``, ``session``, ``run`` and/or ``task``, the later
only have to adapted once per ``subject``. This is based on their status and respective guidelines within ``BIDS`` datasests

Below, you will find further explanations for both file types and the ``metadata`` that should be added/adapted correspondigly.

BIDS-NBS events files
=====================

Within the following, the ``BIDS NBS metadata`` for ``events`` files is shown. Specifically, on the left you can see the contents of ``metadata template`` file and on the
right an example with all ``metadata`` information filled out based on an actual example dataset.


.. tabs::

    .. tab:: ``*_events`` metadata template

        Below you can see the template for the NBS metadata concerning ``*_events`` files.

        .. literalinclude:: ../../bidsnbs/data/nbs_template_events.json
            :language: json
            :linenos:

    .. tab:: ``*_events`` metadata example

        Below you can see an example for the NBS metadata concerning ``*_events`` files.

        .. literalinclude:: ../../bidsnbs/data/nbs_example_events.json
            :language: json
            :linenos:


BIDS-NBS sessions files
=======================

Within the following, the ``BIDS NBS metadata`` for ``sessions`` files is shown. Specifically, on the left you can see the contents of ``metadata template`` file and on the
right an example with all ``metadata`` information filled out based on an actual example dataset.


.. tabs::

    .. tab:: ``*_sessions`` metadata template

        Below you can see the template for the NBS metadata concerning ``*_sessions`` files.

        .. literalinclude:: ../../bidsnbs/data/nbs_template_sessions.json
            :language: json
            :linenos:

    .. tab:: ``*_sessions`` metadata example

        Below you can see an example for the NBS metadata concerning ``*_sessions`` files.

        .. literalinclude:: ../../bidsnbs/data/nbs_example_sessions.json
            :language: json
            :linenos: