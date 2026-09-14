Download data/ and DESI_templates/ for this tutorial.

Source:
  https://github.com/nye17/just_specsim/tree/main/example/

Run from this directory (just_mospec/tutorial/specsimu):

# 1. line lists and mogs (example/data)
mkdir -p data
curl -L -o data/forbidden_lines.ecsv \
  https://raw.githubusercontent.com/nye17/just_specsim/main/example/data/forbidden_lines.ecsv
curl -L -o data/forbidden_mogs.fits \
  https://raw.githubusercontent.com/nye17/just_specsim/main/example/data/forbidden_mogs.fits
curl -L -o data/recombination_lines.ecsv \
  https://raw.githubusercontent.com/nye17/just_specsim/main/example/data/recombination_lines.ecsv

# 2. BGS templates (just_specsim looks for ./DESI_templates/bgs_templates_*.fits)
#    GitHub example/DESI_templates does not ship the FITS files.
#    Official copy: https://data.desi.lbl.gov/public/dr1/spectro/templates/basis_templates/v3.2/
mkdir -p DESI_templates
curl -L -o DESI_templates/bgs_templates_v2.3.fits \
  https://data.desi.lbl.gov/public/dr1/spectro/templates/basis_templates/v3.2/bgs_templates_v2.3.fits
