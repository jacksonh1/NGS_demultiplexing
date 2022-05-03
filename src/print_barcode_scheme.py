import pandas as pd


# %%

# The possible index codes, found from the reverse complement of the first six bases
# of the reverse read.
index_codes = ["ATCACG","CGATGT","TTAGGC","TGACCA","ACAGTG","GCCAAT",
                "CAGATC","ACTTGA","GATCAG"]
# The possible barcodes, found from the first five bases of the forward read.
barcodes = ["ACTCG","ACTGT", "AATGC", "AGTCA", "ATACG", "ATAGC",
                "CGATC", "CTAAG", "CTCGA", "CGAAT", "CTGGT", "CGGTT",
                "GACTT", "GTTCA", "GATAC", "GAGCA", "GATGA", "GTCTG",
                "TCGGA", "TGACC", "TACTG", "TCCAG", "TCGAC", "TAGCT"]

# %%

df = pd.DataFrame(columns=index_codes,index=barcodes)

n_files=len(index_codes)*len(barcodes)
ind=['barcode_{}'.format(str(i)) for i in range(n_files)]
df2 = pd.DataFrame(columns=['barcode','index'],index = ind)



# %%
for b,barcode in enumerate(barcodes):
    for i,index in enumerate(index_codes):
        num = (i*len(barcodes))+b
        filename = 'barcode_'+str(num)
        df.loc[barcode,index]=filename 
        df2.loc[filename,:] = [barcode,index]


df.to_csv('full_nt_key.csv')
df2.to_csv('barcode_nt_key.csv')

