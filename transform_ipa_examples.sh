# Patient to Person 
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Patient-PatientExample1.json \
    -transform PersonMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/PatientExample1.json

# Condition to Condition Occurrence 
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Condition-EncounterExample1.json \
    -transform ConditionMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/Condition-EncounterExample1.json

# Condition (Problem List) to Condition Occurrence
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Condition-ProblemExample1.json \
    -transform ConditionMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/Condition-ProblemExample1.json

# Allergy to Observation Map 
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/AllergyIntolerance-AllIntExample1.json \
    -transform AllergyMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/AllergyIntolerance-AllIntExample1.json


# Immunization to Drug Exposure 
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Immunization-ImmExample1.json \
    -transform ImmunizationMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/Immunization-ImmExample1.json

# Medication Statement to Drug Exposure
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/MedicationStatement-MedStatementExample1.json \
    -transform MedicationMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/MedicationStatement-MedStatementExample1.json

# Observation to Observation 
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Observation-SmokingExample1.json \
    -transform ObservationMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/Observation-SmokingExample1.json

# Observation to Measurement - Lab
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Observation-LabExample1.json \
    -transform MeasurementMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/Observation-LabExample1.json

# Observation to Measurement - Vitals
java -jar validator_cli.jar https://build.fhir.org/ig/HL7/fhir-ipa/Observation-VitalSignsExample1.json \
    -transform MeasurementMap \
    -ig https://build.fhir.org/ig/HL7/fhir-omop-ig \
    -output ipa-omop/Observation-VitalSignsExample1.json

