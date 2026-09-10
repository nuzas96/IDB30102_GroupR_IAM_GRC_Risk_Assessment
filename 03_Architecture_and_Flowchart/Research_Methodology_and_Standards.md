# Research Methodology and Standards

## Research Context

This research focuses on developing and testing a prototype Identity and Access Management risk mapping system. The prototype will receive previously identified technical access-control findings and convert them into structured and prioritised organisational risk-register entries. The prototype does not detect Identity and Access Management issues. Its purpose is to map technical findings to organisational risk information such as likelihood, impact, risk level, priority, proposed risk owner, relevant controls and proposed treatment.

## Selected Research Methodology

The selected research methodology is **Design Science Research**. This methodology is suitable because the research aims to solve an identified organisational problem by designing, developing and evaluating a practical artefact. The artefact produced by this research will be a prototype Identity and Access Management risk mapping system.

Risk Assessment will be used as a supporting technique to assess and prioritise representative technical access-control findings.

Supported finding types include:

* Excessive privilege
* Privilege creep
* Inappropriate permission
* Abnormal access
* Unowned account

## Development Model

The selected development model is **Prototyping**.

The Prototyping model will guide the incremental construction, testing and refinement of the proposed system. An initial prototype will be developed to accept representative technical access-control findings and map them to structured risk-register information. Testing feedback will be used to refine the input structure, validation rules, mapping logic and generated outputs.

## Methodology Justification

Design Science Research is suitable because the study aims to solve an identified organisational problem by developing and testing a practical artefact. The literature review shows that existing approaches can identify excessive privileges, suspicious access and other identity-related risks, but their technical outputs are not consistently converted into formal organisational risk-register information through an IAM-specific, traceable and tested implementation. Design Science Research provides a structured process for defining this problem, establishing solution objectives, developing the prototype and evaluating its performance. The Prototyping model complements this methodology by allowing the system to be constructed incrementally, tested using representative scenarios and refined according to the identified requirements. Together, Design Science Research and the Prototyping model support all three research objectives and enable the proposed system to be assessed using measurable functionality, security, risk-mapping and performance criteria.

## Design Science Research Phases

### Phase 1: Problem Identification and Motivation

Define the problem identified through the literature review: technical Identity and Access Management findings are not consistently translated into structured organisational risk information through an IAM-specific, traceable and tested implementation. The importance of connecting technical findings to formal organisational risk registers will also be established.

### Phase 2: Define Objectives of a Solution

Determine the requirements and objectives of the proposed system. The system must convert previously identified technical access-control findings into structured and prioritised risk-register entries containing relevant organisational risk information.

### Phase 3: Design and Development

Design the system architecture, process flow, input and output structures, validation rules and risk-mapping logic. A prototype will then be developed to process representative Identity and Access Management findings and generate the required risk-register output.

### Phase 4: Demonstration

Process representative scenarios through the prototype, including excessive privilege, privilege creep, inappropriate permission, abnormal access and unowned account. The generated entries will demonstrate how technical findings are mapped to organisational risk information.

### Phase 5: Evaluation

Test the prototype using defined functionality, security, risk-mapping and performance criteria. The evaluation will examine whether the generated entries are complete, consistent, prioritised and traceable to the original technical findings and relevant controls.

### Phase 6: Communication

Document the research process, prototype design, demonstration scenarios, evaluation results and limitations. The work will be communicated through the final report, GitHub repository and project presentation.

## Risk Assessment as a Supporting Technique

Risk Assessment will provide the logic used to assess and prioritise technical access-control findings. For each representative finding, the prototype will use predefined likelihood and impact criteria to determine its risk score, risk level and priority. The finding will then be mapped to a proposed risk owner, relevant controls and proposed treatment.

The prototype will use the following project-defined scoring method:

**Risk Score = Likelihood × Impact**

Likelihood and impact will each use a three-point scale:

* 1 = Rare or Low
* 2 = Possible or Moderate
* 3 = Likely or High

The resulting risk levels are:

* 1–2 = Low
* 3–4 = Medium
* 6–9 = High

This is a project-defined 3 × 3 risk matrix and is not presented as an ISO-mandated scoring formula. A generated entry must undergo analyst review before it can be treated as final. Residual risk will not be presented as a verified output unless treatment has been implemented and the risk has been reassessed.

## Standards

The proposed system will be guided by the following standards:

* **ISO/IEC 27005:2022** – Guides the identification, analysis, evaluation and treatment of information security risks.
* **ISO/IEC 27001:2022** – Provides the Information Security Management System context for documenting risks and selecting appropriate controls.
* **ISO/IEC 27002:2022** – Provides guidance for mapping Identity and Access Management findings to relevant information security controls.

These standards provide a recognised foundation for connecting technical access-control findings with organisational risk-management and control practices. Specific ISO control identifiers will not be used until they have been verified using authorised standard text.

## Alignment with Research Objectives

| Research Objective                                                                                                                                      | Supporting Methodology Activities                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **RO1:** To study existing Identity and Access Management risk-assessment methods for organisational risk management.                                   | Design Science Research Phases 1 and 2: identify the problem, review existing methods and define the system requirements.            |
| **RO2:** To develop a prototype Identity and Access Management risk mapping system for structured and prioritised organisational risk-register entries. | Design Science Research Phase 3 and the Prototyping model: design, develop and refine the proposed system.                           |
| **RO3:** To test the functionality and security of the prototype using defined risk-mapping and performance criteria.                                   | Design Science Research Phases 4 and 5: demonstrate the prototype using representative scenarios and evaluate the resulting outputs. |

## References

* International Organization for Standardization. (2022a). *Information security, cybersecurity and privacy protection—Guidance on managing information security risks (ISO/IEC Standard No. 27005:2022).* https://www.iso.org/standard/80585.html
* International Organization for Standardization. (2022b). *Information security, cybersecurity and privacy protection—Information security controls (ISO/IEC Standard No. 27002:2022).* https://www.iso.org/standard/75652.html
* International Organization for Standardization. (2022c). *Information security, cybersecurity and privacy protection—Information security management systems—Requirements (ISO/IEC Standard No. 27001:2022).* https://www.iso.org/standard/27001.html
* Peffers, K., Tuunanen, T., Rothenberger, M. A., and Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302
* UniKL MIIT. (2026). *Research methodology selection handbook* [Course handbook].
