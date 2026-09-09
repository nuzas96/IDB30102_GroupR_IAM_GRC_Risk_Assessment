\# Preliminary Performance Results



\## Test Purpose



This preliminary test measures the processing performance of the IAM risk-mapping function implemented in the prototype.



The test evaluates the mapping engine only and does not represent complete end-to-end system performance.



\## Test Environment



\- Operating System: Windows-11-10.0.26200-SP0

\- Architecture / Processor: AMD64 Family 25 Model 68 Stepping 1, AuthenticAMD

\- Python Version: Python 3.14.0

\- Test Iterations: 10,000 synthetic IAM findings



\## Preliminary Result



\- Total processing time: 0.103109 seconds

\- Average processing time: 0.010311 ms per finding

\- Throughput: 96,984.65 findings per second



\## Interpretation



The preliminary result shows that the prototype mapping function can process the project-defined mapping rules with low computational overhead in the current test environment.



The result demonstrates preliminary technical feasibility only.



\## Limitation



This benchmark measures the in-memory risk-mapping function.



It does not include:



\- CSV input loading time

\- JSON output writing time

\- database operations

\- user interface processing

\- network communication

\- analyst review and confirmation time



Therefore, the reported throughput should not be interpreted as the final end-to-end performance of the proposed system.

