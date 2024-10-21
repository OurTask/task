task
# Task

> A simple Python package for processing JSON data.

## Installation

Use can install the package using pip:

```bash
$ pip install ourtask-task
```

It is stored at https://pypi.org/project/ourtask-task/

## GitHub Actions

Make sure to have set "Read and write permissions" for the Workflow permissions for the Organization's Actions (https://github.com/organizations/OurTask/settings/actions) and save those settings. 

See also [Create Python Package & Automate Publishing with GitHub Actions: A Quick Guide](https://medium.com/@pallavisinha12/create-python-package-automate-publishing-with-github-actions-a-quick-guide-35b82aa4684c).

## Test the Package

You can test your package in a Python environment:

```python
from ourtask-task import process_json

input_json = '{"a": 10, "b": 20, "c": 30}'
output_json = process_json(input_json)
print(output_json)
```
