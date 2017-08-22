# ABA Schools (Python)

A source for data about law schools accredited by the [American Bar Association (ABA)](https://www.americanbar.org). Contains a comprehensive list of schools in machine-readable formats.

## Usage

Reference [`data/schools.csv`](https://raw.githubusercontent.com/data-creative/aba-schools-py/master/data/schools.csv) and/or [`data/schools.json`](https://raw.githubusercontent.com/data-creative/aba-schools-py/master/data/schools.json).

## Contributing

### Installation

```shell
git clone git@github.com:data-creative/aba-schools-py.git
cd aba-schools-py/
pip3 install -r requirements.txt
```

### Setup

First, ensure the file called `mocks/disclosures_div.html` contains an updated list of schools:

  + Visit the ABA's [Official Guide to ABA-Approved Law Schools](https://www.americanbar.org/groups/legal_education/resources/aba_approved_law_schools/official-guide-to-aba-approved-law-schools.html).
  + Download an HTML-only version of the page, and save it as `mocks/official_school_guide.html`.
  + Review the contents of that document to find JavaScript-generated HTML contents. Search for the text `"The ABA collects this quantitative data" ...` to find where jQuery generates the contents of a `p` tag.
  + Copy and paste the entire `p` tag contents to `mocks/disclosures_div.html`.

### Execution

Generate a CSV file containing the official list of schools:

```shell
python3 app/list_schools.py
```

This will update the contents of `data/schools.csv` and `data/schools.json`.

### Testing

Run tests:

```shell
python3 -m pytest
```
