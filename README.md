# Development of an Identity and Access Management Risk Mapping System for Organisational Risk Registers

**Course:** IDB30102 Research Methodology  
**Group:** R  
**Stage:** Research proposal with preliminary proof of concept

## Research overview

This project concerns Governance, Risk and Compliance (GRC), with a focus on risk assessment in Identity and Access Management (IAM). It proposes an IAM-specific, traceable implementation for translating previously identified access-control findings into structured organisational risk information.

Established standards and risk-register guidance already exist. The project does not claim to invent organisational risk registers or replace professional risk judgement. Its contribution is the proposed implementation and evaluation of the mapping workflow for the selected IAM scenarios.

The prototype does **not** discover attacks, scan systems, detect excessive privileges or automatically determine organisational consequences. It receives already-identified findings and supplied business context. Likelihood, impact and their rationale are provided as inputs, not inferred by a detection model.

## Research problems

1. A technical IAM finding alone does not supply the organisational context needed for justified likelihood, impact, priority and ownership. The proposed implementation combines these evidence types and retains the assessment rationale.
2. The selected technical and practitioner studies do not by themselves establish a complete, tested IAM-to-risk-register workflow. The project investigates a bounded implementation whose mappings, traceability and implemented safeguards can be checked and reproduced.

The literature comparison and its limitations must be supported by the cited studies; a lack of general risk-register guidance is not the claimed gap.

## Research aim

To develop an Identity and Access Management risk mapping system for converting technical access-control findings into structured and prioritised organisational risk-register entries.

## Research objectives

1. To study existing Identity and Access Management risk-assessment methods for organisational risk management.
2. To develop a prototype Identity and Access Management risk mapping system for structured and prioritised organisational risk-register entries.
3. To test the functionality and security of the prototype using defined risk-mapping and performance criteria.

## Methodology

- Research methodology: **Design Science Research**.
- Supporting technique: **Risk Assessment**.
- Development model: **Prototyping**.
- Standards direction: ISO/IEC 27005:2022 for risk assessment; ISO/IEC 27001:2022 and ISO/IEC 27002:2022 for management-system context and control guidance.

The scoring matrix is a project-defined design choice, not an ISO-mandated formula. The current mappings use general control categories, not a verified implementation of individual ISO control identifiers or a claim of certification.

See [methodology and standards](03_Architecture_and_Flowchart/Research_Methodology_and_Standards.md) and [proposed architecture](03_Architecture_and_Flowchart/README.md).

## Current implementation and limitations

The preliminary Python command-line mapper implements:

- CSV input loading and whitespace normalisation;
- validation of required fields and integer likelihood/impact values from 1 to 3;
- five supported finding categories;
- risk scoring, risk-level labels and matching priority labels;
- rule-based control-category and treatment mapping;
- proposed ownership from supplied context, or a clearly unresolved owner;
- source finding, evidence source, review status and rule-version fields;
- JSON output containing candidate mappings or records needing review.

The interactive analyst review, revision and final approval workflow remains **proposed**, not implemented. Valid mappings are marked `Pending Confirmation`; invalid or unsupported inputs are marked `Needs Review`. Generated JSON is not an approved organisational risk register. The current command-line prototype does not implement a user interface, application authentication, a database or an immutable audit trail.

Risk ownership must still be confirmed by an analyst. The prototype does not verify residual risk after treatment, execute treatments or modify access permissions.

## Supported findings

- `excessive_privilege`
- `privilege_creep`
- `inappropriate_permission`
- `abnormal_access`
- `unowned_account`

The five control/treatment mappings are recorded in [config.json](04_Source_Code/config.json).

## Input and scoring

Required fields:

```text
finding_id, finding_type, affected_identity, affected_asset,
permission_or_privilege, technical_evidence, source,
business_scenario, business_consequence, exposure_context,
existing_control, likelihood, impact, assessment_rationale
```

`owner_context` is optional. If it is absent, the candidate owner is `TBD - analyst assignment required`.

Likelihood values are 1 (Rare), 2 (Possible) and 3 (Likely). Impact values are 1 (Low), 2 (Moderate) and 3 (High).

**Risk score = likelihood × impact.**

| Attainable scores | Risk level / current priority label |
|---|---|
| 1, 2 | Low |
| 3, 4 | Medium |
| 6, 9 | High |

The code currently sets `priority` equal to `risk_level` and preserves input order; it does not separately rank or sort entries. Thresholds are implemented in `calculate_risk` in [risk_mapper.py](04_Source_Code/risk_mapper.py). The matching JSON matrix documents them; changing the JSON matrix alone does not reconfigure that function.

Missing required information or unsupported finding types do not receive an automatic Low rating. Their risk score, level and priority remain null pending review.

## Output schema

```text
risk_id, source_finding_id, finding_type, risk_description,
affected_asset, likelihood, impact, risk_score, risk_level,
priority, risk_owner, control_mapping, recommended_treatment,
assessment_rationale, evidence_reference, review_status, rule_version
```

`source_finding_id` links to the supplied finding. `evidence_reference` preserves its `source` value. These fields support traceability but do not themselves verify evidence integrity.

## Repository contents

| Location | Current content |
|---|---|
| [01_Research_Papers](01_Research_Papers/) | Research-paper records with methods, findings, limitations, relevance and article links |
| [02_Literature_Review](02_Literature_Review/) | Literature review, thematic comparison and research-gap discussion |
| [03_Architecture_and_Flowchart](03_Architecture_and_Flowchart/) | Proposed architecture, flowchart, methodology and standards |
| [04_Source_Code](04_Source_Code/) | Python mapper, mapping configuration, preliminary benchmark and run instructions |
| [05_Data_or_Sample_Input](05_Data_or_Sample_Input/) | Five synthetic sample findings and four invalid/unsupported validation inputs |
| [06_Results_or_Expected_Output](06_Results_or_Expected_Output/) | Illustrative mappings, validation outputs and a preliminary benchmark report |
| [07_References](07_References/) | APA reference records and notes on data sources and standards |

Upload publisher PDFs only where redistribution is permitted; otherwise supply verified citations and lawful links. Final citations and claims must remain consistent between the proposal and these supporting records.

### Research objective to repository mapping

| Objective | Supporting evidence |
|---|---|
| RO1 | Paper analysis in 01 and literature comparison/gap in 02 inform the requirements and mapping rules. |
| RO2 | Architecture and methodology in 03 guide the preliminary implementation and configuration in 04. |
| RO3 | Sample/validation inputs in 05 and illustrative outputs and preliminary timing evidence in 06 support evaluation preparation; they do not establish completion of the full proposed evaluation. |

## Requirements and execution

Python 3 is required. The present scripts use only Python standard-library modules; no external Python packages are required. The committed preliminary benchmark records its author's Python 3.14.0 environment, not a minimum supported version.

From the repository root, generate sample mappings:

```powershell
python 04_Source_Code/risk_mapper.py --input 05_Data_or_Sample_Input/sample_iam_findings.csv --config 04_Source_Code/config.json --output generated/sample_output.json
```

Generate outputs for the supplied validation cases:

```powershell
python 04_Source_Code/risk_mapper.py --input 05_Data_or_Sample_Input/validation_test_cases.csv --config 04_Source_Code/config.json --output generated/validation_output.json
```

These commands write under `generated/` to preserve the committed illustrative files. They generate output, not an automated pass/fail comparison against an independent evaluation baseline. Do not commit generated files containing confidential data.

Run the preliminary performance benchmark from the repository root:

```powershell
python 04_Source_Code/performance_test.py
```

## Demonstration and evaluation status

The sample inputs are researcher-created synthetic scenarios, not production logs or real organisational findings. The current validation dataset contains four cases: missing affected asset, out-of-range likelihood, malformed likelihood and an unsupported finding type.

The committed performance report describes 10,000 repeated mapping operations using one representative synthetic finding. It measures the in-memory mapping component, excluding CSV loading, JSON writing, authentication and analyst review. It is preliminary evidence, not final end-to-end performance or 10,000 distinct test scenarios. See [benchmark scope and limitations](06_Results_or_Expected_Output/preliminary_performance_results.md).

The proposal specifies a future evaluation batch of 14 synthetic findings: five valid finding types and nine validation/security cases. It also sets an average in-memory mapping target of no more than 1 ms per finding. The currently committed sample and validation CSVs contain nine records in total; the proposed 14-case evaluation batch is not yet represented by those files.

The full evaluation will compare outputs against an independently prepared manual baseline and assess correctness, completeness, traceability, repeatability, processing time and implemented security safeguards. The independent baseline, final case manifest, repetitions and test procedure must be documented before reporting that evaluation as completed. Sample JSON and preliminary timing results must not be presented as proof that all research objectives have been achieved.

## Group responsibilities

This table records the responsibility allocation, not evidence that every task is complete. Actual contributions are documented in the proposal's compulsory contribution table and the repository history.

| Member | Student ID | Allocated responsibilities |
|---|---|---|
| Muhammad Zariff Wildan bin Mohd Nazri | 52215124871 | Chapter 1, final cross-chapter integration and root README |
| Airil Amman bin Mohd Arif | 52215225384 | Literature review, comparison/synthesis and research-paper evidence |
| Muhammad Hazim bin Hazri | 52215124373 | Research methodology, development model and standards documentation |
| Muhammad Nuzhmi Asyraf bin Rozali | 52215124424 | Architecture, process flow, preliminary code and sample-input coordination |
| Zuhairah Yasmin binti Jamal | 52215225108 | Data procedures, ethics, evaluation, baseline, timeline and reference coordination |

All members share responsibility for the abstract, verified references, formatting, presentation and meaningful contributions to the repository.

## Data and responsible use

Use only synthetic or appropriately authorised data. Do not commit credentials, confidential access logs or identifiable personal information. Control/treatment suggestions are candidates for authorised analyst review, not instructions for automatically changing live accounts or permissions. This repository does not assert verified legal compliance or ISO certification.
