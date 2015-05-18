# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import ploneorg.jsonify


class PloneorgJsonifyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            ploneorg.jsonify,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneorg.jsonify:default')


PLONEORG_JSONIFY_FIXTURE = PloneorgJsonifyLayer()


PLONEORG_JSONIFY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONEORG_JSONIFY_FIXTURE,),
    name='PloneorgJsonifyLayer:IntegrationTesting'
)


PLONEORG_JSONIFY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONEORG_JSONIFY_FIXTURE,),
    name='PloneorgJsonifyLayer:FunctionalTesting'
)


PLONEORG_JSONIFY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONEORG_JSONIFY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneorgJsonifyLayer:AcceptanceTesting'
)
