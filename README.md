task
# Task

> A simple Python package for processing JSON data.

## Installation

Use can install the package using pip:

```bash
$ pip install ourtask-task
```

It is stored at https://pypi.org/project/ourtask-task/

## Formatting Python files

To (re-)format any Python files, run:

```
$ black .
```

## GitHub Environment

For "release" of this package, we create a dedicated Environment in [GitHub](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#creating-an-environment).

## GitHub Actions

Make sure to have set "Read and write permissions" for the Workflow permissions for the Organization's Actions (https://github.com/organizations/OurTask/settings/actions) and save those settings. 

~See also [Create Python Package & Automate Publishing with GitHub Actions: A Quick Guide](https://medium.com/@pallavisinha12/create-python-package-automate-publishing-with-github-actions-a-quick-guide-35b82aa4684c).~

OpenID Connect (OIDC) provides a flexible, credential-free mechanism for delegating publishing authority for a PyPI package to a trusted third party service, like GitHub Actions.

PyPI users and projects can use trusted publishers to automate their release processes, without needing to use API tokens or passwords.

See [Publishing package distribution releases using GitHub Actions CI/CD workflows](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

Create a Personal Access Token to store the PyPI API Token. Visit https://github.com/settings/tokens?type=beta and choose **Generate New Token**.

## Build the Package

You can build the package in a Python environment:

```
$ pip wheel --no-deps -w dist .
```

**NOTE**: [Calling setup.py directly is being deprecated](https://stackoverflow.com/questions/73257839/setup-py-install-is-deprecated-warning-shows-up-every-time-i-open-a-terminal-i)

## Test the Package

You can test the package in a Python environment:

```python
from ourtask-task import process_json

input_json = '{"a": 10, "b": 20, "c": 30}'
output_json = process_json(input_json)
print(output_json)
```

## TOML files

Working with the ```TOML``` files is a trend that allows better integration with many software languages. Reference: [Overview of Packaging for Python](https://packaging.python.org/en/latest/overview/)