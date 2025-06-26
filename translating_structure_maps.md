# Using validator_cli.jar to translate FHIR resources 

It is possible to run transforms using the Java Validator Jar. See [the confluence docs](https://confluence.hl7.org/spaces/FHIR/pages/76158820/Using+the+FHIR+Mapping+Language#UsingtheFHIRMappingLanguage-runtransformsjavavalidator) for available arguments.

The `transform` argument appears to accept the name of the Map that you want to execute within an IG. 

For example, to apply the [`PersonMap` StructureMap](https://build.fhir.org/ig/HL7/fhir-omop-ig/StructureMap-PersonMap.html) you would use this command:

```sh 
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Patient-PatientExample1.json \
    -transform PersonMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output IPA-Person-PatientExample1.json
```

Or to apply the [`ConditionMap` StructureMap](https://build.fhir.org/ig/HL7/fhir-omop-ig/StructureMap-ConditionMap.html): 

```sh
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Condition-EncounterExample1.json \
    -transform ConditionMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output IPA-ConditionOccurrence-EncounterExample1.json
```

It's also possible to run the validator with locally defined resources and IG, for example:

```sh
java -jar validator_cli.jar patient-test-cases/Patient_0002.json -transform PersonMap -ig ./ig -output transformed-omop/Output_0002.json
```