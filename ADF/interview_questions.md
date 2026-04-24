# Azure Data Factory (ADF) – Basics Interview Questions & Answers

## 1. What is Azure Data Factory?
Azure Data Factory (ADF) is a **cloud-based ETL/ELT service** used to **ingest, transform, and move data** between different data stores.

---

## 2. What are the main components of ADF?
- **Linked Service** – Connection information to data sources
- **Dataset** – Structure of the data
- **Pipeline** – Logical grouping of activities
- **Activity** – Actual task (Copy, Data Flow, Notebook, etc.)
- **Integration Runtime (IR)** – Compute used to move or transform data
- **Trigger** – Schedules or events that run pipelines

---

## 3. What is a Pipeline in ADF?
A pipeline is a **logical container** that groups multiple activities to perform a data integration task.

---

## 4. What is an Activity?
An activity defines **what action to perform** in a pipeline.

**Examples:**
- Copy Activity  
- Data Flow Activity  
- Lookup Activity  
- Web Activity  
- Databricks / Notebook Activity  

---

## 5. What is a Linked Service?
A linked service stores **connection details** such as:
- Server name
- Authentication method
- Credentials (often stored in Azure Key Vault)

---

## 6. What is a Dataset?
A dataset represents the **structure of the data** being used, such as:
- A table
- A file
- A folder

---

## 7. What is Integration Runtime (IR)?
Integration Runtime is the **compute infrastructure** used by ADF to:
- Move data
- Transform data
- Execute activities

---

## 8. Types of Integration Runtime
1. **Azure IR** – For cloud-based data movement and transformation  
2. **Self-hosted IR** – For on-premises or private network sources  
3. **Azure-SSIS IR** – To run SSIS packages in Azure  

---

## 9. What is Copy Activity?
Copy Activity is used to **copy data from a source to a destination** with minimal or no transformation.

---

## 10. What is Mapping Data Flow?
Mapping Data Flow is a **no-code, visual data transformation** feature in ADF that runs on **Azure Spark**.

---

## 11. Difference between Pipeline Parameters and Variables?

| Parameters | Variables |
|-----------|----------|
| Read-only | Read and write |
| Passed from trigger | Used inside pipeline logic |
| Immutable | Can be updated during execution |

---

