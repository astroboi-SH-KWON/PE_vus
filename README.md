# PE_vus
Find brcd and umi from FASTQ. Goosang's project in 2021. 03. 25.

    [PE vus sub-pool]
![PE vus sub-pool](./PE_vus_sub_pool.PNG)

    [barcode file]
![PE vus sub-pool](./barcode.PNG)

    [procedure]
        win_size = 3
        1. get "T"*6 + barcode sequence after (18 + 19 + 76)nt
        2. find RP_binding_site_2 sequnce after (target seq length + win_size)nt
        3. get 8nt UMI after RP_binding_site_2


result form
![tsv file result](./result_example.PNG)
