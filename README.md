# python_package_template

## usage

- `cd sample_package_template`

- プログラムの起動
  - `python -m sample_package huga`
- テスト
  - `python setup.py test`

```sh
$cd package/
$python -m package huga
param='huga'
SAMPLE_STATES='hogehoge'
sample_function=Hello sample function!!!

$python setup.py test
running test
Searching for setuptools~=49.2.1
Best match: setuptools 49.2.1
Processing setuptools-49.2.1-py3.8.egg

Using /Users/satoru/go/src/github.com/nokonoko1203/python_package_template/package/.eggs/setuptools-49.2.1-py3.8.egg
running egg_info
writing package.egg-info/PKG-INFO
writing dependency_links to package.egg-info/dependency_links.txt
writing requirements to package.egg-info/requires.txt
writing top-level names to package.egg-info/top_level.txt
reading manifest file 'package.egg-info/SOURCES.txt'
writing manifest file 'package.egg-info/SOURCES.txt'
running build_ext
*** 全体前処理 ***
test_sample_function (tests.test_sample_module.TestSampleModules)
/modules/sample_module/sample_functionのテスト ... + テスト前処理
+ テスト後処理
ok
*** 全体後処理 ***

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```