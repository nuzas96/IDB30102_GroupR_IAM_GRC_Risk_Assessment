\# Preliminary Performance Results



\## Test Purpose



This preliminary test measures the processing performance of the IAM risk-mapping function implemented in the prototype.



The test evaluates the mapping engine only and does not represent complete end-to-end system performance.



\## Test Environment



\- Operating System: Windows-11-10.0.26200-SP0

\- Architecture / Processor: AMD64 Family 25 Model 68 Stepping 1, AuthenticAMD

\- Python Version: Python 3.14.0

\- Test Iterations: 10,000 synthetic IAM findings



\## Test Method



The `performance\_test.py` script repeatedly processes a representative synthetic IAM finding using the same rule-based mapping function implemented in `risk\_mapper.py`.



A total of 10,000 mapping operations were executed.



The test measures:



\- total processing time

\- average processing time per finding

\- approximate findings processed per second



\## Preliminary Result



\- Total processing time: 0.103109 seconds

\- Average processing time: 0.010311 ms per finding

\- Throughput: 96,984.65 findings per second



\## Interpretation



The preliminary result shows that the prototype mapping function can process the current project-defined mapping rules with low computational overhead in the tested environment.



The result provides preliminary evidence of technical feasibility for the mapping component.



It should not be interpreted as the final performance of the completed proposed system.



\## Limitations



This benchmark measures the in-memory risk-mapping function only.



It does not include:



\- CSV input loading time

\- JSON output writing time

\- database operations

\- user interface processing

\- network communication

\- authentication or access-control processing

\- analyst review and confirmation time



The performance result was also obtained from a single local test environment.



Therefore, the reported throughput should not be interpreted as final end-to-end system performance or as a general performance guarantee.



\## Reproducibility



The performance test can be executed from the repository root using:



```cmd

python 04\_Source\_Code\\performance\_test.py

