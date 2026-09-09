# Sample IAM Findings

This folder contains representative technical Identity and Access Management findings used as sample input for the proposed risk-mapping prototype.

The prototype does not detect these findings. The findings are treated as already-identified technical inputs.

## Data Origin

The sample records are researcher-created synthetic IAM scenarios informed by the IAM and access-control issues identified in the literature review.

The scenarios are designed for controlled prototype demonstration and evaluation and are not presented as real organisational data.

The exact identities, assets, permissions, business scenarios and other values contained in the sample records were created specifically for this project.

## Purpose of the Sample Data

The synthetic findings are used to demonstrate whether the proposed prototype can:

- validate required technical and business context
- normalise IAM findings
- process likelihood and impact values
- determine a project-defined risk level and priority
- map supported findings to relevant control categories
- propose treatment actions
- handle risk-owner context
- preserve traceability
- route incomplete or unsupported findings for analyst review

## Required Input Fields

The prototype currently requires:

- `finding_id`
- `finding_type`
- `affected_identity`
- `affected_asset`
- `permission_or_privilege`
- `technical_evidence`
- `source`
- `business_scenario`
- `business_consequence`
- `exposure_context`
- `existing_control`
- `likelihood`
- `impact`
- `assessment_rationale`

## Optional Context Field

- `owner_context`

The system may use `owner_context` to propose a risk owner.

If ownership context is unavailable, the system must not guess the final organisational risk owner.

The preliminary prototype instead uses:

`TBD - analyst assignment required`

## Supported Finding Types

The current project-defined mappings support:

- `excessive_privilege`
- `privilege_creep`
- `inappropriate_permission`
- `abnormal_access`
- `unowned_account`

Unsupported finding types must be sent for analyst review instead of being automatically mapped.

## Project-Defined Risk Ratings

Likelihood:

- `1` = Rare
- `2` = Possible
- `3` = Likely

Impact:

- `1` = Low
- `2` = Moderate
- `3` = High

The prototype calculates:

`Risk Score = Likelihood × Impact`

Risk levels:

- `1–2` = Low
- `3–4` = Medium
- `6–9` = High

The 3 × 3 rating approach is a project-defined prototype design choice and is not presented as an ISO-mandated scoring formula.

## Validation Behaviour

Incomplete or invalid input must not automatically receive a low-risk rating.

Examples of validation cases include:

- missing required fields
- likelihood outside the range `1–3`
- impact outside the range `1–3`
- malformed rating values
- unsupported finding types

Missing or invalid technical or business context results in a review state so that the information can be corrected before finalisation.

## Files

### `sample_iam_findings.csv`

Contains representative synthetic IAM findings covering the currently supported finding categories.

### `validation_test_cases.csv`

Contains deliberately invalid or unsupported inputs used to demonstrate prototype validation behaviour.

The validation cases include:

- a missing required field
- an out-of-range likelihood value
- a malformed likelihood value
- an unsupported finding type