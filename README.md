# justmospec
Spectroscopic Reduction Pipeline for JUST-MOS. This pipeline is designed to from raw data to redshift,  including:  
- generating mock 1d spectra, 
- generating mock 2d raw spectra,  
- reducing 2d raw spectra to 1d spectra, 
- fitting 1d spectra to get spectroscopic redshifts
- ... 

## Install

Spectrum generation (`SpectrumMaker`) and redshift fitting need packages from
[desihub](https://github.com/desihub). 

```bash
pip install --no-build-isolation git+https://github.com/desihub/desiutil.git
pip install --no-build-isolation git+https://github.com/desihub/desimodel.git
install_desimodel_data  # install required desimodel data 
pip install --no-build-isolation git+https://github.com/desihub/desitarget.git
pip install --no-build-isolation git+https://github.com/desihub/desispec.git
pip install --no-build-isolation git+https://github.com/desihub/desisim.git
pip install --no-build-isolation git+https://github.com/desihub/redrock.git
git clone https://github.com/desihub/redrock-templates
pip install -e ".[specsimu]"
```

- `desisim` (and its desihub dependencies above) is required by `SpectrumMaker`
- `redrock` and `redrock-templates` are required to fit spectroscopic redshifts

Set these environment variables before running `SpectrumMaker` or `rrdesi`:

```bash
export DESIMODEL=/path/to/desimodel          # directory that contains desimodel data/
export DESI_BASIS_TEMPLATES=/path/to/v3.1    # directory that contains DESI basis-templates
export RR_TEMPLATE_DIR=/path/to/redrock-templates # directory that contains redrock-templates 
```

## Usage

```python
from justmospec.simulator import SpectrumMaker

maker = SpectrumMaker()
wave, flux, meta, objmeta = maker(z=0.1, Mr=-21.0, color=0.7, saveto='./mockspectra/')
```
