# python_cli_template

## setup

```shell
% export PIPENV_IGNORE_VIRTUALENVS=1
% export PIPENV_VENV_IN_PROJECT=true
% pipenv install
```

## usage

- プログラムの起動

```shell
% pipenv run python -m package huga
param='huga'
SAMPLE_STATES='hogehoge'
sample_function=Hello sample function!!!
```

- テスト

```shell
% pipenv run python -m unittest
+ sample_functionをテストします
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```