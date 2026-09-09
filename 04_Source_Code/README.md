# Preliminary Source Code

This folder contains the preliminary technical components for the proposed Identity and Access Management risk-mapping prototype.

## Prototype Processing Flow

The proposed prototype follows the processing sequence:

1. Validate the technical IAM finding and required context.
2. Normalise the input.
3. Assess likelihood and impact.
4. Calculate the project-defined risk score and risk level.
5. Map the finding to relevant organisational controls and proposed treatment.
6. Propose a risk owner only when sufficient ownership context is available.
7. Present the generated mapping for analyst review and confirmation.
8. Generate the structured risk-register entry after confirmation in the proposed final workflow.

## Risk Rating

The preliminary prototype uses a project-defined 3 × 3 risk matrix.

`Risk Score = Likelihood × Impact`

Likelihood:

- `1` = Rare
- `2` = Possible
- `3` = Likely

Impact:

- `1` = Low
- `2` = Moderate
- `3` = High

Risk levels:

- `1–2` = Low
- `3–4` = Medium
- `6–9` = High

This scoring method is a prototype design choice and is not presented as an ISO-mandated scoring formula.

## Mapping Rules

The rule-based mapping configuration is stored in `config.json`.

The current prototype supports the following finding types:

- `excessive_privilege`
- `privilege_creep`
- `inappropriate_permission`
- `abnormal_access`
- `unowned_account`

Each supported finding type is mapped to relevant organisational control categories and a proposed treatment.

Unsupported finding types are not automatically mapped and are instead routed to analyst review.

## Risk Owner Handling

The prototype may use the `owner_context` field to propose a risk owner.

If sufficient ownership context is unavailable, the prototype uses:

`TBD - analyst assignment required`

The prototype does not automatically invent or confirm the final organisational risk owner.

## Validation Behaviour

The preliminary prototype validates required technical and business-context fields before risk mapping.

Examples of invalid input include:

- missing required fields
- likelihood values outside the range `1–3`
- impact values outside the range `1–3`
- malformed likelihood or impact values
- unsupported finding types

Invalid or incomplete findings are assigned the review status:

`Needs Review`

The prototype does not automatically assign a low-risk rating when required information is missing.

## Human Validation

Organisational risk decisions require human review.

The proposed system architecture includes an Analyst Review and Confirmation stage in which the analyst reviews the proposed:

- likelihood
- impact
- risk level
- risk owner
- control mapping
- treatment

before the result is treated as an approved organisational risk-register entry.

## Traceability

Generated mappings preserve the following traceability information:

- source finding identifier
- evidence reference
- rule version
- review status

The `source_finding_id` links the generated mapping to the original technical IAM finding.

## Current Prototype Scope

The current preliminary proof of concept implements:

- CSV input loading
- required-field validation
- input normalisation
- likelihood and impact validation
- project-defined risk scoring
- risk-level determination
- rule-based control mapping
- proposed treatment mapping
- risk-owner handling
- traceability fields
- review-status generation
- JSON output generation

Generated mappings are currently marked as `Pending Confirmation` when processing valid supported findings.

The analyst review and final approval workflow is part of the proposed system design and is not yet implemented as an interactive component in this preliminary proof of concept.

Therefore, the generated JSON output should be treated as a candidate risk-register mapping rather than a final approved organisational risk-register entry.

## Files

- `risk_mapper.py` — preliminary IAM risk-mapping implementation
- `config.json` — project-defined risk matrix and mapping rules
- `performance_test.py` — preliminary mapping-engine performance test
- `README.md` — technical documentation and execution instructions

## Running the Preliminary Prototype

### Requirements

- Python 3
- No external Python packages are required

Run the following command from the repository root:

```cmd
python 04_Source_Code\risk_mapper.py --input 05_Data_or_Sample_Input\sample_iam_findings.csv --config 04_Source_Code\config.json --output 06_Results_or_Expected_Output\illustrative_risk_register_output.json
```

The generated output will be saved in:

`06_Results_or_Expected_Output/illustrative_risk_register_output.json`

## Running the Validation Test Cases

Run:

```cmd
python 04_Source_Code\risk_mapper.py --input 05_Data_or_Sample_Input\validation_test_cases.csv --config 04_Source_Code\config.json --output 06_Results_or_Expected_Output\validation_test_results.json
```

The validation results will be saved in:

`06_Results_or_Expected_Output/validation_test_results.json`

## Running the Preliminary Performance Test

Run from the repository root:

```cmd
python 04_Source_Code\performance_test.py
```

The performance test measures the in-memory mapping function only and should not be interpreted as complete end-to-end system performance.