"""Test setup for integration and functional tests."""
import unittest

from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

import plone.app.tinymce

@onsetup
def setup_product():
    """Set up the package and its dependencies."""

    zcml.load_config('configure.zcml', plone.app.tinymce)
    
setup_product()
ptc.setupPloneSite(extension_profiles=['plone.app.tinymce:default'])

functional_tests = (
    'installation.txt',
    )

def test_suite():
    """This sets up a test suite that actually runs the tests"""
    return unittest.TestSuite(
        [ztc.FunctionalDocFileSuite(
            'tests/%s' % f, package='plone.app.tinymce',
            test_class=ptc.FunctionalTestCase)
            for f in functional_tests]
        )
