import pandas as pd


# %%

# The possible index codes, found from the reverse complement of the first six bases
# of the reverse read.
INDEX_CODES = ["ATCACG","CGATGT","TTAGGC","TGACCA","ACAGTG","GCCAAT",
                "CAGATC","ACTTGA","GATCAG"]
# The possible barcodes, found from the first five bases of the forward read.
BARCODES = ["ACTCG","ACTGT", "AATGC", "AGTCA", "ATACG", "ATAGC",
                "CGATC", "CTAAG", "CTCGA", "CGAAT", "CTGGT", "CGGTT",
                "GACTT", "GTTCA", "GATAC", "GAGCA", "GATGA", "GTCTG",
                "TCGGA", "TGACC", "TACTG", "TCCAG", "TCGAC", "TAGCT"]

# %%

df = pd.DataFrame(columns=INDEX_CODES,index=BARCODES)

n_files=len(INDEX_CODES)*len(BARCODES)
ind=['barcode_{}'.format(str(i)) for i in range(n_files)]
df2 = pd.DataFrame(columns=['barcode','index'],index = ind)



# %%
for b,barcode in enumerate(BARCODES):
    for i,index in enumerate(INDEX_CODES):
        num = (i*len(BARCODES))+b
        filename = 'barcode_'+str(num)
        df.loc[barcode,index]=filename 
        df2.loc[filename,:] = [barcode,index]


df.to_csv('barcode_key-wide.csv')
df2 = df2.reset_index().rename(columns={'level_0':'filename'})
df2.to_csv('barcode_key-long.csv', index=False)

