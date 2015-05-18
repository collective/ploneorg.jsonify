====================
ploneorg.jsonify
====================

This is the package that provides the export views for the Plone.org migration.
It's mostly based on collective.jsonify. The reason for repackage it is because
c.jsonify made lots of assumptions based that it is aimed to be able to run in
very old Plone versions (1.0 or so).

This work is based without having this constraints. The modifications are barely
noticeable and includes some fixes to deal with dexterity on the other side and
p.a.c.

