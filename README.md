# FHIR-to-OMOP-Connectathon-June-2025

## Download FHIR Java Validator 

```sh
wget https://github.com/hapifhir/org.hl7.fhir.core/releases/latest/download/validator_cli.jar
```

## Using this repo:

```sh
$ python src/generate_test_cases.py
$ source java_cmd.sh 
$ python src/compare_omop_resources.py 
```
Gives this output:

  test_id  description                                           transform     success
---------  ----------------------------------------------------  ------------  ---------
     0001  Alive male populates correctly                        PersonMap     False
     0002  Alive female populates correctly                      PersonMap     False
     0003  Populate Condition for verificationStatus==Confirmed  ConditionMap  False


## Sample command 

```sh 
java -jar validator_cli.jar fhir-examples/IPA-PatientExample1.json -transform PersonMap -ig https://build.fhir.org/ig/HL7/fhir-omop-ig -output test.json
```

```sh
java -jar validator_cli.jar fhir-examples/Condition03_Condition315586.json -transform ConditionMap -ig https://build.fhir.org/ig/HL7/fhir-omop-ig -output ConvertedCondition.json
```

-  ...Failure: Exception executing transform tgt.condition_start_datetime = cast(rd, 'datetime') on Rule "ConditionMap|ConditionOccurrence|recordedDate": cast to datetime not yet supported
org.hl7.fhir.exceptions.FHIRException: Exception executing transform tgt.condition_start_datetime = cast(rd, 'datetime') on Rule "ConditionMap|ConditionOccurrence|recordedDate": cast to datetime not yet supported

Running local:

```sh
java -jar validator_cli.jar patient-test-cases/Patient_0002.json -transform PersonMap -ig ./ig -output transformed-omop/Output_0002.json
```


## Notes 

- Condition Era:
    - this should be computed after completing the mapping
    - needs to be done after all non-standard to standard conversion happens 
    - https://ohdsi.github.io/CommonDataModel/sqlScripts.html#Condition_Eras

- Type Alignment on ID's
    - Resource.id -> primary key id isn't valid 
    - Resource id's can be alphanumeric and include `-` or `.`
    - org.hl7.fhir.exceptions.FHIRException: Exception executing transform tgt.person_id = cast(id, 'integer') on Rule "PersonMap|Person|id": java.lang.NumberFormatException: For input string: "Patient1"


## 
 ...Failure: Exception executing transform tgt.condition_start_date = cast(osd, 'date') on Rule "ConditionMap|ConditionOccurrence|onsetDateTime": Invalid date/time string (datatype DateType does not support SECOND precision): 1999-12-31T12:00:00