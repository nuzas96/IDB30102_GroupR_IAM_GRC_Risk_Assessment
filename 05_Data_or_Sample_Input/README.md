## Data Origin

The sample records are researcher-created synthetic IAM scenarios informed by the IAM and access-control issues identified in the literature review. They are designed for controlled prototype demonstration and evaluation and are not presented as real organisational data.

# Sample IAM Findings

This folder contains representative technical Identity and Access Management findings used as sample input for the proposed risk-mapping prototype.

The prototype does not detect these findings. The findings are treated as already-identified technical inputs.

## Required Input Fields

- `finding\_id`

- `finding\_type`

- `affected\_identity`

- `affected\_asset`

- `permission\_or\_privilege`

- `technical\_evidence`

- `source`

- `business\_scenario`

- `business\_consequence`

- `exposure\_context`

- `existing\_control`

- `likelihood`

- `impact`

- `assessment\_rationale`

## Optional Context Field

- `owner\_context`

The system may use `owner\_context` to propose a risk owner. If ownership context is unavailable, the system must not guess the final organisational risk owner.

## Supported Finding Types

- `excessive\_privilege`

- `privilege\_creep`

- `inappropriate\_permission`

- `abnormal\_access`

- `unowned\_account`

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

The 3 × 3 rating approach is a project-defined prototype design choice and is not presented as an ISO-mandated scoring formula.

## Validation Behaviour

Incomplete or invalid input must not automatically receive a low-risk rating.

Missing technical or business context should result in a validation error or review state so that the required information can be completed before finalisation.
