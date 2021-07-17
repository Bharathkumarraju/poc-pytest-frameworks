# poc-python-testing-frameworks
Poc on python testing frame works "unittest" and "pytest"

## unittest framework
unitest is by default included in pythons library

### testing unitteest framework example1
```buildoutcfg
C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\unittest>python -m unittest test_area_of_circle.py -v
test_if_radius_greaterthan_one (test_area_of_circle.cirlcleArea) ... ok
test_if_radius_is_boolean (test_area_of_circle.cirlcleArea) ... ok
test_if_radius_is_complex (test_area_of_circle.cirlcleArea) ... ok
test_radius_is_negative (test_area_of_circle.cirlcleArea) ... ok
test_radius_is_one (test_area_of_circle.cirlcleArea) ... ok
test_radius_is_string (test_area_of_circle.cirlcleArea) ... ok
test_radius_is_zero (test_area_of_circle.cirlcleArea) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.003s

OK

C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\unittest>

```


### testing unitteest framework example2
```buildoutcfg
C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\unittest>python -m unittest test_phonebook.py -v
test_empty_phonebook_is_consistent (test_phonebook.PhoneBookTest) ... ok
test_inconsistent_with_duplicate_entries (test_phonebook.PhoneBookTest) ... ok
test_inconsistent_with_duplicate_prefix (test_phonebook.PhoneBookTest) ... ok
test_is_consistent_with_different_entries (test_phonebook.PhoneBookTest) ... ok
test_lookup_by_name (test_phonebook.PhoneBookTest) ... ok
test_missing_name (test_phonebook.PhoneBookTest) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.003s

OK

C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\unittest>

```

## pytest framework
to install pytest run `pip install pytest`

### testing pytest framework example1
```buildoutcfg
C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\pytest>python -m pytest test_area_of_circle.py -v
================================================================================================================================================== test session starts ===================================================================================================================================================
platform win32 -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- C:\Users\P1326210\AppData\Local\Programs\Python\Python39\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\pytest
collected 4 items                                                                                                                                                                                                                                                                                                         

test_area_of_circle.py::test_radius_is_zero PASSED                                                                                                                                                                                                                                                                  [ 25%]
test_area_of_circle.py::test_radius_is_string PASSED                                                                                                                                                                                                                                                                [ 50%]
test_area_of_circle.py::test_radius_is_negative PASSED                                                                                                                                                                                                                                                              [ 75%]
test_area_of_circle.py::test_radius_is_morethan_one PASSED                                                                                                                                                                                                                                                          [100%]

=================================================================================================================================================== 4 passed in 0.13s ====================================================================================================================================================

C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\pytest>



```


### testing pytest framework example2
```buildoutcfg
C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\pytest>python -m pytest test_wallet.py -v
================================================================================================================================================== test session starts ===================================================================================================================================================
platform win32 -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- C:\Users\P1326210\AppData\Local\Programs\Python\Python39\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\pytest
collected 15 items                                                                                                                                                                                                                                                                                                        

test_wallet.py::test_get_the_current_balance PASSED                                                                                                                                                                                                                                                                 [  6%]
test_wallet.py::test_add_to_the_current_balance[10] PASSED                                                                                                                                                                                                                                                          [ 13%]
test_wallet.py::test_add_to_the_current_balance[20] PASSED                                                                                                                                                                                                                                                          [ 20%]
test_wallet.py::test_add_to_the_current_balance[10.5] PASSED                                                                                                                                                                                                                                                        [ 26%]
test_wallet.py::test_add_to_the_current_balance[20.5] PASSED                                                                                                                                                                                                                                                        [ 33%]
test_wallet.py::test_remove_from_the_current_balance[10] PASSED                                                                                                                                                                                                                                                     [ 40%]
test_wallet.py::test_remove_from_the_current_balance[11] PASSED                                                                                                                                                                                                                                                     [ 46%]
test_wallet.py::test_remove_from_the_current_balance[10.5] PASSED                                                                                                                                                                                                                                                   [ 53%]
test_wallet.py::test_remove_from_the_current_balance[11.5] PASSED                                                                                                                                                                                                                                                   [ 60%]
test_wallet.py::test_subtract_higher_value_from_current_balance PASSED                                                                                                                                                                                                                                              [ 66%]
test_wallet.py::test_initial_balance PASSED                                                                                                                                                                                                                                                                         [ 73%]
test_wallet.py::test_adding_negative_ints_floats[-5] PASSED                                                                                                                                                                                                                                                         [ 80%]
test_wallet.py::test_adding_negative_ints_floats[-6.5] PASSED                                                                                                                                                                                                                                                       [ 86%]
test_wallet.py::test_removing_negative_ints_floats[-10] PASSED                                                                                                                                                                                                                                                      [ 93%]
test_wallet.py::test_removing_negative_ints_floats[-11.5] PASSED                                                                                                                                                                                                                                                    [100%]

=================================================================================================================================================== 15 passed in 0.11s ===================================================================================================================================================

C:\Users\P1326210\Documents\git\poc-python-testing-frameworks\pytest>


```

## Conclusion:
We can use `pytest` for our TDD in python using pulumi as it has more features than unittest(which is jUnit based and old)
Even pulumi recommends to use `pytest` see here: https://www.youtube.com/watch?v=wH6WpiLrEdc

