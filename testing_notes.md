## Notes 

- Condition Era:
    - this should be computed after completing the mapping
    - needs to be done after all non-standard to standard conversion happens 
    - https://ohdsi.github.io/CommonDataModel/sqlScripts.html#Condition_Eras

- Type Alignment on ID's
    - Resource.id -> primary key id isn't valid 
    - Resource id's can be alphanumeric and include `-` or `.`
    - org.hl7.fhir.exceptions.FHIRException: Exception executing transform tgt.person_id = cast(id, 'integer') on Rule "PersonMap|Person|id": java.lang.NumberFormatException: For input string: "Patient1"

## Examples of complicated patterns:

Here's some more complicated examples of domain/concept id alignment:

- Verify Conditions Get Observations with Values & Conditions:
    - Source:
        - ICD-9-CM V23.42 Pregnancy with history of ectopic pregnancy
    - Target:
        - Condition
            - concept id 4299535 (Pregnancy)
                - vocabulary = SNOMED and concept code = 77386006 
        - Observation
            - concept id 1340204 (History of event)
                - vocabulary = OMOP Extension and concept code = OMOP5165859
            - value as concept id  437611 (Ectopic pregnancy)
                - vocabulary = SNOMED and concept code = 34801009

- Verify Conditions get Measurements with Values 
    - Source 
        - ICD-9-CM 018.94 Miliary tuberculosis, unspecified, tubercle bacilli not found (in sputum) by microscopy, but found by bacterial culture
    - Target
        - Measurement
            - concept id 4056128 (Sample organism cultured)
                - SNOMED:168190000
            - value as concept id: 434559 (Miliary tuberculosis)
                - SNOMED:47604008