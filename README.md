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

Visit https://github.com/OurTask/task/settings/environments and choose **New Environment**. 

Name the new environment **Release** and click **Configure Environment**. 

**NOTE**:<br/>
- Environment names are not case sensitive. 
- An environment name may not exceed 255 characters and must be unique within the repository.

Specify at least yourself (the owner) as one of the **Required Reviewers**, but do **not** choose **Prevent self-review**.

Enable **Allow administrators to bypass configured protection rules**.

Limit which branches and tags can deploy to this environment based on rules or naming patterns. We choose **main** branch only.

For **Environment secrets** add the PyPI API Token taken from pypi.org. Name it "PYPI_API_TOKEN".

![Environment_Release-001](https://github.com/user-attachments/assets/46ecc414-73f1-4981-814e-1600adb25288)

## GitHub Actions

Make sure to have set "Read and write permissions" for the Workflow permissions for the Organization's Actions (https://github.com/organizations/OurTask/settings/actions) and save those settings. 

~See also [Create Python Package & Automate Publishing with GitHub Actions: A Quick Guide](https://medium.com/@pallavisinha12/create-python-package-automate-publishing-with-github-actions-a-quick-guide-35b82aa4684c).~

OpenID Connect (OIDC) provides a flexible, credential-free mechanism for delegating publishing authority for a PyPI package to a trusted third party service, like GitHub Actions.

PyPI users and projects can use trusted publishers to automate their release processes, without needing to use API tokens or passwords.

See [Publishing package distribution releases using GitHub Actions CI/CD workflows](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

![PyPI_Publishing-001](https://github.com/user-attachments/assets/b54c5eab-f6ab-414e-b358-9c5dcfa515ea)

If the projet exists already, you will see this warning:

![PyPI_Publishing-002](https://github.com/user-attachments/assets/b9aaa415-1bbe-4cc2-a100-ca459b09d182)

Follow the [link](https://pypi.org/manage/project/ourtask_task/settings/publishing/?project_name=ourtask_task&owner=OurTask&repository=task&workflow_filename=publish.yml&environment=release&provider=github) provided.

You'll continue within the specific project:

![PyPI_Publishing-003](https://github.com/user-attachments/assets/ebc88517-5b68-4318-8534-d3fffa1feaab)

Click **Add**.



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
