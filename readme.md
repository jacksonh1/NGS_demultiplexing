**run in Python 2.**

### 1. Sort barcodes

The first and most time-intensive step, performed by `01_barcode_sort.py`, is simply to read the forward and reverse read files and sort the reads into the bins by their barcodes. Because this process is essentially limited by the machine's disk speed, this script may take up to about 30 hours to complete on a typical pair of Illumina fastq files (~60GB each). To run, simply call:

```
$ python ./src/01_barcode_sort.py ./data/sample_data_forward.fastq ./data/sample_data_forward.fastq /output/dir/
```

*Customization:* To adjust `01_barcode_sort.py` to fit a different barcoding scheme, the easiest approach is to change the `get_barcode_number` function or its associated constants. The current implementation computes a bin number based on the first five bases of the forward read and the first six bases of the reverse read, removing reads that do not meet a threshold of quality on these barcode regions.
