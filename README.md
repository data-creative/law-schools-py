# ABA Law Schools (Python)

A source for data about law schools accredited by the [American Bar Association (ABA)](https://www.americanbar.org). Contains a comprehensive list of schools in machine-readable formats.

## Usage

Reference [`data/schools.csv`](https://raw.githubusercontent.com/data-creative/aba-schools-py/master/data/schools.csv) and/or [`data/schools.json`](https://raw.githubusercontent.com/data-creative/aba-schools-py/master/data/schools.json).

## Contributing

### Prerequisites

Install Python and Pip 3.x:

```shell
brew install python3
```

Install a web driver to facilitate automated browsing:

```shell
brew install geckodriver
# then append to your bash config file (e.g., `~/.bashrc`)
export PATH=$PATH:/path/to/geckodriver # enable use of selenium for python
```

Ensure your user has access to a directory called `/usr/local/selenium`:

```shell
mkdir /usr/local/selenium # you might have to sudo this. if so, afterwards `chown your_username /usr/local/selenium`
```

### Installation

Install source code:

```shell
git clone git@github.com:data-creative/law-schools-py.git
cd law-schools-py/
```

Install package dependencies:

```shell
pip3 install -r requirements.txt
```

### Execution

Update the list of schools:

```shell
python3 app/list_schools.py
```

This will update the contents of `mocks/schools_tbody.html` and `data/schools.csv` and `data/schools.json` for further reference. If the contents change, please commit and push and release a new version.

Download employment summary reports for each school:

```shell
python3 app/download_reports.py
```

This will update the contents of `reports/` and `data/reports.csv` and `data/reports.json` for further reference. If the contents change, please commit and push and release a new version.

### Testing

Run tests:

```shell
python3 -m pytest
```

## [License](LICENSE)
