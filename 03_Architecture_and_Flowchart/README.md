# Proposed System Architecture and Flowchart

This folder contains the proposed architecture and process flow for the Identity and Access Management risk-mapping prototype.

## System Boundary

The prototype does not detect Identity and Access Management or access-control issues directly.

Instead, it receives technical findings that have already been identified through technical assessment activities and transforms them into structured organisational risk-register information.

## Proposed System Architecture

The proposed architecture follows the process:

Technical IAM / Access-Control Findings  
→ IAM Finding Input  
→ Validation and Normalisation  
→ Risk Assessment  
→ GRC Mapping  
→ Analyst Review and Confirmation  
→ Risk Register Generator  
→ Structured Organisational Risk-Register Entry

The system requires relevant technical and business context before organisational risk information is finalised.

The analyst review stage confirms the proposed risk level, ownership, control mapping and treatment before the risk-register entry is approved.

## Proposed System Flow

The flowchart represents the following sequence:

1. Receive a technical IAM finding.
2. Validate the required fields.
3. Request missing information if the input is incomplete.
4. Normalise the finding.
5. Assess likelihood and impact.
6. Determine the risk level and priority.
7. Map the finding to organisational risk information.
8. Perform analyst review and confirmation.
9. Revise the mapping if it is not approved.
10. Generate the structured risk-register entry.
11. Export or store the result.

## Files

- `proposed_system_architecture.png` — Proposed System Architecture
- `proposed_system_flowchart.png` — Proposed System Flowchart
- `Research_Methodology_and_Standards.md` — Research methodology and standards documentation

## Traceability

The architecture and flowchart in this folder are aligned with Chapter 3 of the Research Proposal.