# 🌐 Team7_EpiXposome
## 🧬 Epigenomics_Harmonization_Exposome

## 🔍 Key Features

EpiXposome aims to decode the impact of environmental exposures on epigenetic changes using advanced machine learning. Our goal is to predict disease risks by revealing how exposome variables interact with epigenetic markers. This project promises to deliver actionable insights that could revolutionize disease prevention and treatment.

## 📂 Datasets

- **JPSS (NOAA)**: [NOAA Joint Polar Satellite System (JPSS)](https://registry.opendata.aws/noaa-jpss)
- **TARGET**: [Therapeutically Applicable Research to Generate Effective Treatments (TARGET)](https://registry.opendata.aws/target)
- **C-PTAC-2**: [Clinical Proteomic Tumor Analysis Consortium 2 (CPTAC-2)](https://registry.opendata.aws/cptac-2)
- **TCGA**: [The Cancer Genome Atlas - Registry of Open Data on AWS](https://registry.opendata.aws/tcga)
- **ENCODE**: [Encyclopedia of DNA Elements (ENCODE)](https://registry.opendata.aws/encode-project)

## 🔧 Parameter Usage

### **Data Preprocessing Parameters**
- `missing_data_threshold`
- `normalization_method`
- `batch_size`

### **Model Training Parameters**
#### **Bidirectional RNNs (BRNNs) / BiLSTMs / GRUs**
- `sequence_length` 
- `hidden_units`
- `dropout_rate`  
- `learning_rate`
- `epochs`

## 💻 System Requirements


- OS: Linux (Ubuntu, CentOS, Amazon Linux), macOS, or Windows 10 with WSL2.
- CPU: Intel i5/i7 or AMD equivalent; multi-core recommended.
- RAM: 16 GB minimum, 32 GB+ recommended.
- Storage: 256 GB SSD minimum; more for large datasets.
- Software: Python 3.6+, key libraries (numpy, pandas, scikit-learn), Jupyter.


## 🔗 Dependencies

- Python
- BRNNs
- Bidirectional LSTMs (BiLSTMs)
- GRUs
- RNNs
- XGBoost
- Genetic algorithm
- Logistic regression models
- JSSS
- AWS CLI

## 📥 Example Inputs
`geneexp` `mirna exp` `tccga`


## 📤 Example Outputs
`.csv` `.json`

## Steps

1. **Step 1: Data Collection**
   - Data Sources:
     - miRNA expression data from CPTAC2 and TARGET
     - DNA methylation data from TCGA, ENCODE, TARGET, and TCGA
     - Exposome data from NOAA Joint Polar Satellite System (JPSS)

2. **Step 2: Data Preprocessing**
   - Clean and impute missing data for robust analysis.
   - Prepare the data by addressing any quality control issues.
  
3. **Step 3: Dimensionality Reduction and Data Integration**
   - Use PCA to reduce dimensions down to three.
   - Use Non-Negative Matrix Factorization (NMF) to integrate disparate data sets and find underlying relationships.
  
NMF formula:

<img width="739" alt="Screenshot 2025-05-15 at 11 34 57 AM" src="https://github.com/user-attachments/assets/0b854790-48f7-4e67-bca8-5b370bc565c5" />


4. **Step 4: Data Splitting**
   - Randomly split the dataset into training (80%) and testing (20%) sets.

5. **Step 5: Bidirectional Recurrent Neural Networks (BiRNNs)**
   - Run Bidirectional Recurrent Neural Networks (BiRNNs) model to determine dependencies between exposome variables,
     methylation and microRNA data sets.

![image](https://github.com/user-attachments/assets/06db20f6-dea6-4817-b1b2-13e05dd4c721)


6. **Step 6: Model Training**
   - Train the selected machine learning model using the training dataset.

7. **Step 7: Model Testing**
   - Assess the model's performance using the testing dataset to validate its accuracy.

8. **Step 8: Experimentation**
   - Investigate the effects of different exposome variables on mRNA and methylation activity.
   - Determine if there are specific genes or pathways involved.

9. **Step 9: Results Interpretation**
   - Use bioinformatics analyses (like GSEA, GO) to interpret the model's findings.

10. **Step 10: Visualization**
   - Develop visualizations to represent the results clearly (e.g., time-altered line plots).

## 🌐 Process Flowchart


![Team 7 Flow- (4)](https://github.com/user-attachments/assets/15bfaca4-d279-435f-9249-db929101838b)


## 🔮 Future Aims

- **Standardization and Packaging**
  - Package the model into a standardized, reusable module.
  - Prepare a Python package for easy distribution and use.

- **Publication and Sharing**
  - Publish the findings and the Python package for the broader research community.

- **Documentation and Reproducibility**
  - Ensure all steps are well-documented to allow for reproducibility of the results.
  - Include instructions for setting up the computational environment and running the analysis.


## 👤 Contributors

- Halina Krzystek
- Kirtan Dave
- Paul Kao
- Macciej Kowalski
- Aung Myat Phyo
- Diya
- Alishba Nadeem

## 🔗 References

- [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Exposome: Epigenetics and autoimmune diseases - PubMed](https://pubmed.ncbi.nlm.nih.gov/39097180/)
- [Mutual regulation of microRNAs and DNA methylation in human cancers](https://pmc.ncbi.nlm.nih.gov/articles/PMC5406215/)
- https://academic.oup.com/bioinformatics/article/41/2/btaf066/8005856
