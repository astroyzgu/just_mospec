# Licensed under a 3-clause BSD style license - see LICENSE
# -*- coding: utf-8 -*-
"""Test justmospec.simulator
"""
import os
import tempfile
import unittest

import numpy as np
from astropy.io import fits
from astropy.table import Table

from ..simulator import save_spectra


class TestSaveSpectra(unittest.TestCase):
    """Test FITS output from :func:`save_spectra`.
    """

    def test_save_spectra_writes_files(self):
        wave = np.linspace(3600.0, 10000.0, 11)
        flux = np.ones((2, 11))
        meta = Table({'REDSHIFT': [0.1, 0.2]})
        objmeta = Table({'TEMPLATEID': [1, 2]})
        with tempfile.TemporaryDirectory() as tmp:
            outdir = save_spectra(tmp, wave, flux, meta, objmeta)
            specfile = os.path.join(outdir, 'spectra.fits')
            self.assertTrue(os.path.exists(specfile))
            self.assertTrue(os.path.exists(os.path.join(outdir, 'meta.fits')))
            self.assertTrue(os.path.exists(os.path.join(outdir, 'objmeta.fits')))
            with fits.open(specfile) as hdul:
                self.assertEqual(hdul['WAVELENGTH'].header['EXTNAME'], 'WAVELENGTH')
                self.assertEqual(hdul['FLUX'].data.shape, (2, 11))


class TestSpectrumMaker(unittest.TestCase):
    """Test :class:`SpectrumMaker` when desisim is available.
    """

    def test_import_or_skip(self):
        try:
            from ..simulator import SpectrumMaker  # noqa: F401
        except ImportError:
            self.skipTest('desisim is not installed')
