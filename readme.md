# NGS data demultiplexing scripts

This repository contains scripts associated with the manuscript entitled: **Molecular determinants of TRAF6 binding specificity suggest that native interaction partners are not optimized for affinity**. [BioRxiv link](https://www.biorxiv.org/content/10.1101/2022.05.08.491058v3). The code here was used to perform the analysis detailed in the manuscript and not intended to be released as a software/tool for general use. You are welcome to adapt it for your own use and if you do have questions you are encouraged to contact Jackson Halpin (jhalpin@mit.edu) and/or Amy Keating (keating@mit.edu). However, please note that we provide this software "as is" and do not guarantee any support or warrenty (see LICENSE).

## setup
**run this script in Python 2.**
python2 is no longer supported. There are currently no plans to convert this script 
into python 3.
If you are using conda, you can create an environment with the same
modules that I used to run the scripts:<br>
`conda env create -f py2_traf6_NGS_full.yml`<br>
then:<br>
`conda activate py2_traf6_NGS`<br>
to use the environment.<br>

if you are on linux or windows, you should probably use:<br>
`conda env create -f ./py2_traf6_NGS_compatible.yml`<br>
then:<br>
`conda activate py2_traf6_NGS`<br>
instead.<br>
`py2_traf6_NGS_full.yml` is the exact environment I used on mac but the dependencies and their versions will probably be different on other operating systems. The "compatible" version (`py2_traf6_NGS_compatible.yml`) was generated with `conda env export --from-history` and should work for any operating system
<br>



## run scripts

`./src/01_barcode_sort.py` simply reads the forward and reverse read files and sorts the reads into the bins by their barcodes. Because this process is essentially limited by the machine's disk speed, this script may take up to about 30 hours to complete on a typical pair of Illumina fastq files (~60GB each). To run, simply call:

```bash
$ python ./src/01_barcode_sort.py ./data/sample_data_forward.fastq ./data/sample_data_forward.fastq /output/dir/
```

*Customization:* To adjust `./src/01_barcode_sort.py` to fit a different barcoding scheme, the easiest approach is to change the `get_barcode_number` function or its associated constants.<br> 
The current implementation computes a bin number based on the first five bases of the forward read and the first six bases of the reverse read. If any position in the first 5 nucleotides of the forward read has a quality score less than 20, the read is discarded. Reads that do not exactly match one of the barcode/index pairs (first 5 nts of the forward read and first 6 nts of the reverse read, respectively) are discarded.<br>
To change the barcode/index sequences used, change the `BARCODES` and `INDEX_CODES` variables in `./src/01_barcode_sort.py`. (Note: The order of the lists determines the barcode numbering).<br>
<br>
You can use `./src/print_barcode_scheme.py` to view which barcode/index pairs correspond with which output file name. This script outputs two files: `barcode_key-long.csv` and `barcode_key-wide.csv`
<br>

The majority of these scripts were written by Venkat Sivaraman and slightly modified by Jackson Halpin.

