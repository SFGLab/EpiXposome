# Data Download and Processing

## Prerequisites - Installation

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the following scripts in order to download and process the data and generate the concatenated TSV files:

1. **CTPAC2 data**

   ```bash
   python3 cptac2/download_and_concat_ctpac2.py
   python3 cptac2/download_and_melt_cptac2_mirna.py
   ```

2. **TARGET miRNA data**

   ```bash
   python3 target/download_and_concat_target_mirna.py
   ```

The generated TSV files will be output in the respective folders.

> **Note:** The TSV files are currently available on [Google Drive](https://drive.google.com/drive/folders/1aGPg6hM5spdGACS-6wneKl2N1DHL2uOZ).

3. **Exposome data**

   
demographic data
```bash
wget -P ~/Downloads/nhanes https://wwwn.cdc.gov/Nchs/Nhanes/2017-2020/P_DEMO.xpt.txt
```

physical activity data
```bash
wget -P ~/Downloads/nhanes https://wwwn.cdc.gov/Nchs/Nhanes/2017-2020/P_PAQ.xpt.txt
```

diet data
```bash
wget -P ~/Downloads/nhanes https://wwwn.cdc.gov/Nchs/Nhanes/2017-2020/P_DR1IFF.xpt.txt
```
