# Multi-Source Candidate Data Transformer

## Overview

This project transforms candidate information from multiple sources into a single structured JSON profile.

Currently supported sources:

- Recruiter CSV
- Resume PDF

## Features

- Read candidate data from CSV
- Extract data from Resume PDF
- Merge information from multiple sources
- Normalize phone numbers (E.164)
- Track source of every field
- Assign confidence score
- Configurable JSON output
- Command Line Interface (CLI)

## Project Structure

```
eightfold-transformer/
│
├── input/
├── output/
├── src/
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
cd src

python main.py --csv ../input/candidates.csv --resume ../input/resume.pdf --config ../input/config.json
```

## Output

The transformed profile is generated in:

```
output/output.json
```

## Assumptions

- Only one structured source (CSV)
- Only one unstructured source (Resume PDF)
- CSV values are preferred during merge
- Basic confidence scoring is used

## Limitations

- LinkedIn not supported
- GitHub profile not supported
- ATS JSON not supported
- Basic merge strategy