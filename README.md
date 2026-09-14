# just_mospec
Spectroscopic Reduction Pipeline for JUST-MOS. This pipeline is designed to from raw data to redshift,  including:  
- generating mock 1d spectra, 
- generating mock 2d raw spectra,  
- reducing 2d raw spectra to 1d spectra, 
- fitting 1d spectra to get spectroscopic redshifts
- ... 

## Install

Spectrum generation (`SpectrumMaker`) needs
[just_etc](https://github.com/RainW7/just_etc) and
[just_specsim](https://github.com/nye17/just_specsim).
Redshift fitting needs packages from [desihub](https://github.com/desihub).

```bash
pip install git+https://github.com/RainW7/just_etc.git
pip install git+https://github.com/nye17/just_specsim.git
pip install --no-build-isolation git+https://github.com/desihub/redrock.git
git clone https://github.com/desihub/redrock-templates
pip install -e ".[specsimu]"
```

- `just_etc` and `just_specsim` are required by `SpectrumMaker`
- `redrock` and `redrock-templates` are required to fit spectroscopic redshifts

Set these environment variables before running `SpectrumMaker` or `rrdesi`:

```bash
export DESIMODEL=/path/to/desimodel          # directory that contains desimodel data/
export DESI_BASIS_TEMPLATES=/path/to/v3.1    # directory that contains DESI basis-templates
export RR_TEMPLATE_DIR=/path/to/redrock-templates # directory that contains redrock-templates 
```
