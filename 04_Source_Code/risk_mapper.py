import argparse
import csv
import json
from pathlib import Path


REQUIRED_FIELDS = [
    "finding_id",
    "finding_type",
    "affected_identity",
    "affected_asset",
    "permission_or_privilege",
    "technical_evidence",
    "source",
    "business_scenario",
    "business_consequence",
    "exposure_context",
    "existing_control",
    "likelihood",
    "impact",
    "assessment_rationale",
]


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def normalise_value(value):
    if value is None:
        return ""
    return str(value).strip()


def validate_finding(finding):
    errors = []

    for field in REQUIRED_FIELDS:
        if not normalise_value(finding.get(field)):
            errors.append(f"Missing required field: {field}")

    for rating_field in ("likelihood", "impact"):
        value = normalise_value(finding.get(rating_field))

        if not value:
            continue

        try:
            rating = int(value)
        except ValueError:
            errors.append(
                f"Invalid {rating_field}: expected an integer from 1 to 3"
            )
            continue

        if rating not in (1, 2, 3):
            errors.append(
                f"Invalid {rating_field}: value must be between 1 and 3"
            )

    return errors


def calculate_risk(likelihood, impact):
    score = likelihood * impact

    if score <= 2:
        risk_level = "Low"
    elif score <= 4:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return score, risk_level


def build_risk_description(finding):
    finding_type = finding["finding_type"].replace("_", " ")
    asset = finding["affected_asset"]
    consequence = finding["business_consequence"]

    return (
        f"{finding_type.capitalize()} affecting {asset}. "
        f"Potential business consequence: {consequence}."
    )


def build_review_entry(finding, config, reason):
    finding_id = normalise_value(finding.get("finding_id")) or "UNKNOWN"

    return {
        "risk_id": f"RISK-{finding_id}",
        "source_finding_id": finding_id,
        "finding_type": normalise_value(finding.get("finding_type")),
        "risk_description": "Input requires analyst review before risk mapping.",
        "affected_asset": normalise_value(finding.get("affected_asset")),
        "likelihood": normalise_value(finding.get("likelihood")),
        "impact": normalise_value(finding.get("impact")),
        "risk_score": None,
        "risk_level": None,
        "priority": None,
        "risk_owner": (
            normalise_value(finding.get("owner_context"))
            or config["review_rules"]["missing_owner_context"]
        ),
        "control_mapping": [],
        "recommended_treatment": "Manual analyst review required.",
        "assessment_rationale": reason,
        "evidence_reference": normalise_value(finding.get("source")),
        "review_status": "Needs Review",
        "rule_version": config["rule_version"],
    }


def map_finding(finding, config):
    finding = {
        key: normalise_value(value)
        for key, value in finding.items()
    }

    validation_errors = validate_finding(finding)

    if validation_errors:
        return build_review_entry(
            finding,
            config,
            "; ".join(validation_errors),
        )

    finding_type = finding["finding_type"]

    mapping = config["finding_mappings"].get(finding_type)

    if mapping is None:
        return build_review_entry(
            finding,
            config,
            f"Unsupported finding type: {finding_type}",
        )

    likelihood = int(finding["likelihood"])
    impact = int(finding["impact"])

    risk_score, risk_level = calculate_risk(
        likelihood,
        impact,
    )

    risk_owner = (
        finding.get("owner_context")
        or config["review_rules"]["missing_owner_context"]
    )

    return {
        "risk_id": f"RISK-{finding['finding_id']}",
        "source_finding_id": finding["finding_id"],
        "finding_type": finding_type,
        "risk_description": build_risk_description(finding),
        "affected_asset": finding["affected_asset"],
        "likelihood": likelihood,
        "impact": impact,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "priority": risk_level,
        "risk_owner": risk_owner,
        "control_mapping": mapping["control_mapping"],
        "recommended_treatment": mapping["recommended_treatment"],
        "assessment_rationale": finding["assessment_rationale"],
        "evidence_reference": finding["source"],
        "review_status": config["review_rules"]["default_review_status"],
        "rule_version": config["rule_version"],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Preliminary IAM risk-mapping prototype"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the CSV file containing IAM findings",
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to the mapping configuration JSON file",
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to the generated JSON output file",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    config_path = Path(args.config)
    output_path = Path(args.output)

    config = load_json(config_path)
    findings = load_csv(input_path)

    results = [
        map_finding(finding, config)
        for finding in findings
    ]

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False,
        )

    print(f"[+] Processed findings: {len(results)}")
    print(f"[+] Output written to: {output_path}")


if __name__ == "__main__":
    main()