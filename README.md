# NonClassicalLightNesi


## How to run tests

In the top directory, type
```
pytest
```
If all tests pass you should see
```
tests/test_atoms_cavity.py .                                                                                                       [100%]

=========================================================== 1 passed in 2.20s ============================================================
```

## How to add new tests

Add your test scripts under the `tests/` directory. Each function should ideally test a feature. The name of the function 
should start with `test_`.

## Continuous integration

File `.github/workflows/ci.yml` instructs github to build the code (install Python and dependencies) and run the unit tests each time 
a change is pushed to the repository. The output of the tests can be found under the "Actions" tab, e.g. <https://github.com/aell060/NonClassicalLightNesi/actions>.

![CI results](https://github.com/aell060/NonClassicalLightNesi/actions/workflows/ci.yml/badge.svg)

