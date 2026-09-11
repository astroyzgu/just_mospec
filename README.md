# justmospec
Spectroscopic Reduction Pipeline for JUST-MOS.

## Install

```bash
pip install -e .
```

Spectrum generation needs DESI templates. Install the [desihub](https://github.com/desihub) packages first (they are not on PyPI):

```bash
bash install_desihub.sh
pip install -e ".[specsimu]"
```

The script picks Python 3.12 and writes `desihub-env.sh` with `DESIMODEL`, `DESI_BASIS_TEMPLATES`, and `RR_TEMPLATE_DIR`. Source it before calling `SpectrumMaker`:

```bash
source desihub-env.sh
```

## Usage

```python
from justmospec.simulator import SpectrumMaker

maker = SpectrumMaker()
wave, flux, meta, objmeta = maker(z=0.1, Mr=-21.0, color=0.7, saveto='./mockspectra/')
```
