# FHIR-to-OMOP-Connectathon-June-2025

This repo includes a simple method to define and run test cases for the FHIR-to-OMOP structure maps. The process includes:

- define test cases in `test_conf.yml`
- generate the test FHIR resources for input and the expected output resources
- run the FHIR Java Validator to transform the FHIR resources
- run a python script to compare the resources

There may be better and more robust mechanisms for defining the test cases, but this lightweight setup helps support quick/easy development.

This code is not thoroughly tested and was prototyped in an afternoon for the FHIR-to-OMOP connectathon. 

## Setup:

1. Download FHIR Java Validator  

```sh
$ wget https://github.com/hapifhir/org.hl7.fhir.core/releases/latest/download/validator_cli.jar
```

2. Create your venv and install requirements  

```sh 
$ python -m venv venv
$ pip install -r requirements.txt
```

## Using this repo:

Here's the example commands to use this repo:

```sh
$ python src/generate_test_cases.py
$ source java_cmd.sh 
$ python src/compare_omop_resources.py 
```

The comparison script will give an output like this: 

  test_id  description                                           transform     success
---------  ----------------------------------------------------  ------------  ---------
     0001  Alive male populates correctly                        PersonMap     True
     0002  Alive female populates correctly                      PersonMap     True
     0003  Populate Condition for verificationStatus==Confirmed  ConditionMap  False

