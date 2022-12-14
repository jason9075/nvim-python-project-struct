# Nvim lsp config for Python

## Pyright Setting

在主目錄下，pyrightconfig.json定義好src與tests兩個資料夾的相依性後，pyright就可以在tests資料夾底下去import src/底下的function。

```
  "executionEnvironments": [
    {
      "root": "tests",
      "extraPaths": [
        "src"
      ]
    },
    {
      "root": "src"
    }
  ]
```

## Pytest Setting 

在主目錄下定義好pytest.ini，pytest就可以讀取到src底下的python function。

```
pytest -v --cov=src/ tests/
```

Result:
```
platform darwin -- Python 3.7.0, pytest-7.2.0, pluggy-1.0.0 -- /Users/astra-jason-kuan/miniconda3/envs/pytest/bin/python
cachedir: .pytest_cache
rootdir: /Users/astra-jason-kuan/workspace/nvim-python-struct, configfile: pytest.ini
plugins: cov-4.0.0
collected 2 items                                                                                                                     

tests/test_main.py::test_main PASSED                                                                                            [ 50%]
tests/test_text.py::test_get_text PASSED                                                                                        [100%]

---------- coverage: platform darwin, python 3.7.0-final-0 -----------
Name              Stmts   Miss  Cover
-------------------------------------
src/__init__.py       0      0   100%
src/main.py           4      0   100%
src/text.py           2      0   100%
-------------------------------------
TOTAL                 6      0   100%
```

## Ref

https://github.com/microsoft/pyright/blob/main/docs/configuration.md#sample-pyprojecttoml-file

