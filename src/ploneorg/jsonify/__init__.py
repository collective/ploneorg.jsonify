# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory
import pkg_resources

_ = MessageFactory('ploneorg.jsonify')


try:
    pkg_resources.get_distribution('cioppino.twothumbs')
except pkg_resources.DistributionNotFound:
    HAS_RATINGS = False
else:
    HAS_RATINGS = True
