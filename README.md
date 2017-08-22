


### Installation

```shell
git clone ______
cd ______
pip3 install -r requirements.txt
```

### Usage

First, ensure the file called `mocks/disclosures_div.html` contains an updated list of schools:

  + Visit the ABA's [Official Guide to ABA-Approved Law Schools](https://www.americanbar.org/groups/legal_education/resources/aba_approved_law_schools/official-guide-to-aba-approved-law-schools.html).
  + Download an HTML-only version of the page, and save it as `mocks/official_school_guide.html`.
  + Review the contents of that document to find JavaScript-generated HTML contents. Search for the text `"The ABA collects this quantitative data" ...` to find where jQuery generates the contents of a `p` tag.
  + Copy and paste the entire `p` tag contents to `mocks/disclosures_div.html`.

Generate a CSV file containing the official list of schools:

```shell
python3 app/list_schools.py
```

This will update the contents of `data/schools.csv`.

### Testing

Run tests:

```shell
python3 -m pytest
```
