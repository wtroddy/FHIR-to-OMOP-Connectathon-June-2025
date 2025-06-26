from pathlib import Path
import json
import yaml

import tabulate


def main(test_config_path: Path):    
    # read the test case configuration 
    with open(test_config_path, "r") as f:
        test_config = yaml.safe_load(f)

    comparison_results = []

    for case in test_config["test_cases"]:
        # preset directories
        expected_output_dir = Path("expected-output")
        transformed_dir = Path("transformed-omop")

        with open((expected_output_dir).joinpath(f"{case['expected_output'][0]['resourceType']}_{case['test_id']}.json"), "r") as f:
            expected = json.load(f)

        with open((transformed_dir).joinpath(f"Output_{case['test_id']}.json"), "r") as f:
            transformed = json.load(f)

        # result 
        comparison_results.append(
            {
                "test_id": case["test_id"],
                "description": case["description"],
                "transform": case["transform"],
                "success": (expected==transformed)
            }
        )

    # print result
    header = comparison_results[0].keys()
    rows = [x.values() for x in comparison_results]
    print(tabulate.tabulate(rows, header, tablefmt="github"))

if __name__ == "__main__":
    main(test_config_path="test_conf.yml")
