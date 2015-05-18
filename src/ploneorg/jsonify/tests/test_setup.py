# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ploneorg.jsonify.testing import PLONEORG_JSONIFY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that ploneorg.jsonify is properly installed."""

    layer = PLONEORG_JSONIFY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneorg.jsonify is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ploneorg.jsonify'))

    def test_uninstall(self):
        """Test if ploneorg.jsonify is cleanly uninstalled."""
        self.installer.uninstallProducts(['ploneorg.jsonify'])
        self.assertFalse(self.installer.isProductInstalled('ploneorg.jsonify'))

    def test_browserlayer(self):
        """Test that IPloneorgJsonifyLayer is registered."""
        from ploneorg.jsonify.interfaces import IPloneorgJsonifyLayer
        from plone.browserlayer import utils
        self.assertIn(IPloneorgJsonifyLayer, utils.registered_layers())
