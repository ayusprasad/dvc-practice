# DVC Data Versioning Lab

[![CI](https://github.com/ayusprasad/dvc-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/dvc-practice/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![DVC](https://img.shields.io/badge/Data%20versioning-DVC-945DD6?logo=dvc&logoColor=white)

A compact demonstration of generating a reproducible CSV and tracking its data directory with DVC.

## Workflow

- mycode.py creates a small tabular dataset.
- data.dvc records the DVC-tracked data directory.
- The local DVC remote points to a sibling S3 directory for practice; configure a remote available to your environment before collaborating.

## Run locally

### Prerequisites

- Python 3.11 or newer
- Git
- DVC

### Install and run

~~~bash
git clone https://github.com/ayusprasad/dvc-practice.git
cd dvc-practice
python -m venv .venv
python -m pip install -r requirements.txt
python mycode.py
~~~

To inspect or retrieve DVC data, configure an accessible remote and run dvc pull. This repository's local remote is a learning setup, not a shared hosted service.

## Quality checks

~~~bash
pytest -q
ruff check --select E4,E7,E9,F mycode.py tests
~~~

CI checks the generator and tests without accessing a DVC remote. No environment variables are needed.
