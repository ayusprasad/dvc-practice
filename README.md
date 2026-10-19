# 📦 DVC (Data Version Control) Hands-On Lab

A practical laboratory demonstrating **Data Version Control (DVC)** workflows, remote S3/local data storage tracking, dataset versioning across Git commits, and reproducible data pipelines.

---

## 🌟 Concepts Demonstrated
- `dvc init`: Setting up DVC repository tracking.
- `dvc add data/sample_data.csv`: Decoupling large datasets from Git history into `.dvc` pointer files.
- `dvc push` / `dvc pull`: Synchronizing versioned data artifacts with remote storage.
- Git & DVC alignment: Switching branches and checking out corresponding dataset versions (`dvc checkout`).

---

## 🚀 Quickstart

```bash
# Install dependencies
pip install -r requirements.txt

# Run data generator
python mycode.py

# Track dataset with DVC
dvc add data/sample_data.csv
git add data/sample_data.csv.dvc .gitignore
git commit -m "Track dataset version"
```