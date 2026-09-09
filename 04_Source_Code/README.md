\# Preliminary Source Code



This folder contains the preliminary technical components for the proposed Identity and Access Management risk-mapping prototype.



\## Prototype Processing Flow



The prototype follows the processing sequence:



1\. Validate the technical IAM finding and required context.

2\. Normalise the input.

3\. Assess likelihood and impact.

4\. Calculate the project-defined risk score and risk level.

5\. Map the finding to relevant organisational controls and proposed treatment.

6\. Propose a risk owner only when sufficient ownership context is available.

7\. Send the generated mapping for analyst review and confirmation.

8\. Generate the structured risk-register entry after confirmation.



\## Risk Rating



The prototype uses a project-defined 3 × 3 risk matrix:



`Risk Score = Likelihood × Impact`



Risk levels:



\- 1–2: Low

\- 3–4: Medium

\- 6–9: High



This scoring method is a prototype design choice and is not presented as an ISO-mandated formula.



\## Mapping Rules



The mapping rules are stored in `config.json`.



Supported finding types:



\- `excessive\_privilege`

\- `privilege\_creep`

\- `inappropriate\_permission`

\- `abnormal\_access`

\- `unowned\_account`



Unsupported finding types must be routed to analyst review.



\## Human Validation



The prototype does not make final organisational risk decisions automatically.



Risk ownership, control mapping, treatment and the final risk-register entry require analyst review and confirmation.



\## Traceability



Generated entries will preserve:



\- source finding identifier

\- evidence reference

\- rule version

\- review status

