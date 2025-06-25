from pathlib import Path 
import json 
import yaml 

def generate_fhir_resource(resource_data, description=None):

    if description:
        # add the text programmatically 
        resource_data["text"] = {
            "status": "generated",
            "div": f"<div xmlns='http://www.w3.org/1999/xhtml'>{description}</div>"
        }

    return resource_data

def get_output_file(output_parent_dir, test_id, resource_type):
    # output_path = output_parent_dir.joinpath(f"test-{test_id}")
    output_path = output_parent_dir
    output_path.mkdir(parents=True, exist_ok=True)

    output_file = output_path.joinpath(f"{resource_type}_{test_id}.json")

    return output_file

def save_resource(output_file, resource_data):

    with open(output_file, "w") as f:
        json.dump(resource_data, f, indent=4)

def get_java_cmd(input_fhir_file, structure_map_name, test_id):

    java_output_file = get_output_file(Path("transformed-omop"), test_id, resource_type="Output") 

    cmd = (
        f"java -jar validator_cli.jar {input_fhir_file}" \
        f" -transform {structure_map_name}" \
        " -ig https://build.fhir.org/ig/HL7/fhir-omop-ig" \
        f" -output {java_output_file}"
    )

    return cmd 

def main(test_config_path: Path):

    # read the test case configuration 
    with open(test_config_path, "r") as f:
        test_config = yaml.safe_load(f)

    java_cmds = []

    # iterate over the input 
    for case in test_config["test_cases"]:
        input_fhir = generate_fhir_resource(resource_data=case["fhir_input"], description=case["description"])

        input_fhir_file = get_output_file(
            output_parent_dir=Path("patient-test-cases"),
            test_id=case["test_id"],
            resource_type=input_fhir["resourceType"]
        )

        save_resource(output_file=input_fhir_file, resource_data=input_fhir)

        java_cmds.append(get_java_cmd(input_fhir_file=input_fhir_file, structure_map_name=case["transform"], test_id=case["test_id"]))

        for expected_output in case["expected_output"]:
            output_fhir = generate_fhir_resource(resource_data=expected_output)
            
            output_expected_file = get_output_file(
                output_parent_dir=Path("expected-output"),
                test_id=case["test_id"],
                resource_type=output_fhir["resourceType"]
            )

            save_resource(output_file=output_expected_file, resource_data=output_fhir)

    # save the java cmd 
    with open("java_cmd.sh", "w") as f:
        f.writelines("\n".join(java_cmds))


if __name__ == "__main__":

    main(test_config_path="test_conf.yml")