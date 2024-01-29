# paddle-billing-client

<div align="center">

[![Build status](https://github.com/websideproject/paddle-billing-client/workflows/build/badge.svg?branch=main&event=push)](https://github.com/websideproject/paddle-billing-client/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/paddle-billing-client.svg)](https://pypi.org/project/paddle-billing-client/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/websideproject/paddle-billing-client/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/websideproject/paddle-billing-client/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/websideproject/paddle-billing-client/releases)
[![License](https://img.shields.io/github/license/websideproject/paddle-billing-client)](https://github.com/websideproject/paddle-billing-client/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)
![HitCount](https://img.shields.io/endpoint?url=https%3A%2F%2Fhits.dwyl.com%2Fwebsideproject%2Fpaddle-billing-client.json&label=Visitors&color=%23FF7F50&link=http%3A%2F%2Fhits.dwyl.com%2Fwebsideproject%2Fpaddle-billing-client)
![UniqueHitCount](https://img.shields.io/endpoint?url=https%3A%2F%2Fhits.dwyl.com%2Fwebsideproject%2Fpaddle-billing-client.json%3Fshow%3Dunique&label=Unique%20visitors&color=%23DC143C&link=http%3A%2F%2Fhits.dwyl.com%2Fwebsideproject%2Fpaddle-billing-client)
![Downloads](https://img.shields.io/pypi/dm/paddle-billing-client.svg)

Python wrapper around the new Paddle Billing API

</div>

## Paddle Classic vs Paddle Billing

- Paddle Classic is the original Paddle API, which is still in use by many merchants. More info can be found [here](https://developer.paddle.com/classic/api-reference/1384a288aca7a-api-reference)
  - If you are looking for the Paddle Classic API wrapper, please see [`paddle-client`](https://github.com/paddle-python/paddle-client)
- Paddle Billing is the new API, which is just launched at 2023, August. Paddle Billing is a complete rewrite of the Paddle Classic API, and is designed to be more flexible and easier to use. More info can be found [here](https://developer.paddle.com/api-reference/overview)

### Django Integration
- For Paddle Classic, there is a Django integration available at [`dj-paddle`](https://github.com/paddle-python/dj-paddle) and [`django-paddle`](https://github.com/kennell/django-paddle)
- For Paddle Billing, there is a Work In Progress Django integration available at [`django-paddle-billing`](https://github.com/websideproject/django-paddle-billing)
---
## 📦 Features

- Pydantic models for all API requests and responses
- Tests with [`pytest`](https://docs.pytest.org/en/latest/) and [`VCR.py`](https://vcrpy.readthedocs.io/en/latest/) for mocking HTTP requests
- [`Website stalker`](https://github.com/EdJoPaTo/website-stalker) Github Action to monitor any API changes
- Pagination support with generator to process pages one by one
- Helper function for signature validation for webhooks

### Tests

- [x] Products
- [x] Prices
- [x] Discounts
- [x] Customers
   - [ ] Customer Credit balances
- [x] Addresses
- [x] Businesses
- [x] Transactions
- [x] Subscriptions (except activate)
   - [x] Subscription Resume
   - [ ] Subscription Activate Trialing
- [x] Adjustments
- [x] Pricing Previews
- [ ] Reports
- [x] Event types
- [x] Events
- [x] Notification Settings
- [x] Notifications
- [ ] Notification logs

## Installation

```bash
pip install -U paddle-billing-client
```

or install with `Poetry`

```bash
poetry add paddle-billing-client
```

## Usage

```python
from paddle_billing_client.client import PaddleApiClient
from apiclient import HeaderAuthentication


client = PaddleApiClient(
    base_url="https://sandbox-api.paddle.com", 
    authentication_method=HeaderAuthentication(token="your-paddle-token")
)

# Create a product
product = client.create_product(
            ProductRequest(
                name="Test Product New",
                tax_category="standard",
                description="Test Product Description",
                image_url="https://example.com/image.png",
                custom_data=dict(foo="bar"),
            )
        )
                         
# Get all products
products = client.list_products()

# Get all prices
plans = client.list_prices()

# Pagination
from paddle_billing_client.pagination import paginate
from paddle_billing_client.models.notification import NotificationQueryParams

for notification in paginate(client.list_notifications, query_params=NotificationQueryParams(
        status="delivered",
        after='ntf_01hb1n6nw8yx1wwts2cyh632s9',
        per_page=10
    )):
        # Process notifications page by page
        print("Notification:")
        print(len(notification.data))
        print(notification.data[-1].id)
```

### Debugging

To print the raw exception response, you can use the `VerboseErrorHandler`:

  ```python
  from paddle_billing_client.client import PaddleApiClient
  from apiclient import HeaderAuthentication
  from paddle_billing_client.errors import VerboseErrorHandler
  
  client = PaddleApiClient(
      base_url="https://sandbox-api.paddle.com", 
      authentication_method=HeaderAuthentication(token="your-paddle-token"),
      error_handler=VerboseErrorHandler
  )
  ```

- Sandbox API url: `https://sandbox-api.paddle.com/`
- Live API url: `https://api.paddle.com/`

More usage examples can be found in **tests**.

### Helper functions

```python
from paddle_billing_client.helpers import validate_webhook_signature

# Validate webhook signature
is_valid = validate_webhook_signature(
    signature_header=request.headers.get("HTTP_PADDLE_SIGNATURE"),
    raw_body=request.data,
    secret_key="your-paddle-secret-key",
)
```

### Makefile usage

[`Makefile`](https://github.com/websideproject/paddle-billing-client/blob/main/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/websideproject/paddle-billing-client/tree/main/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/websideproject/paddle-billing-client/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/websideproject/paddle-billing-client/blob/main/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

## 🚀 Package Template Features

### Development features

- Supports for `Python 3.7` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/websideproject/paddle-billing-client/blob/main/pyproject.toml) and [`setup.cfg`](https://github.com/websideproject/paddle-billing-client/blob/main/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Ready-to-use [`.editorconfig`](https://github.com/websideproject/paddle-billing-client/blob/main/.editorconfig), [`.dockerignore`](https://github.com/websideproject/paddle-billing-client/blob/main/.dockerignore), and [`.gitignore`](https://github.com/websideproject/paddle-billing-client/blob/main/.gitignore). You don't have to worry about those things.

### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/websideproject/paddle-billing-client/blob/main/.github/workflows/build.yml) as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/websideproject/paddle-billing-client/blob/main/Makefile#L89). More details in [makefile-usage](#makefile-usage).
- [Dockerfile](https://github.com/websideproject/paddle-billing-client/blob/main/docker/Dockerfile) for your package.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).
- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/websideproject/paddle-billing-client/blob/main/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.

### Open source community features

- Ready-to-use [Pull Requests templates](https://github.com/websideproject/paddle-billing-client/blob/main/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/websideproject/paddle-billing-client/tree/main/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/websideproject/paddle-billing-client/blob/main/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## 🛡 License

[![License](https://img.shields.io/github/license/websideproject/paddle-billing-client)](https://github.com/websideproject/paddle-billing-client/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/websideproject/paddle-billing-client/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{paddle-billing-client,
  author = {Benjamin Gervan},
  title = {Python wrapper around the new Paddle Billing API},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/websideproject/paddle-billing-client}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
