# btcpay-django

A Django app for working with [BTCPayServer](https://btcpayserver.org/)

## Installation

```bash
pip install btcpay-django
```

## Developers

### Release

To cut a release, run `bumpversion`, push the changes, and push the newly created tag
for auto deployment from the pipeline.

```bash
bumpversion part 
```

E.g.

```bash
bumpversion patch
git push
git push --tags
```