import time
import json

from risk_mapper import map_finding


SAMPLE_FINDING = {
    "finding_id": "PERF-001",
    "finding_type": "excessive_privilege",
    "affected_identity": "performance_user",
    "affected_asset": "Performance Test System",
    "permission_or_privilege": "Admin Access",
    "technical_evidence": "Synthetic performance test finding",
    "source": "Performance Test",
    "business_scenario": "Controlled prototype performance test",
    "business_consequence": "Potential unauthorised system modification",
    "exposure_context": "Internal test environment",
    "existing_control": "Access review",
    "likelihood": "2",
    "impact": "3",
    "assessment_rationale": "Representative performance test case",
    "owner_context": "Test System Owner",
}


def main():
    with open("04_Source_Code/config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    iterations = 10000

    start = time.perf_counter()

    for i in range(iterations):
        finding = SAMPLE_FINDING.copy()
        finding["finding_id"] = f"PERF-{i:05d}"
        map_finding(finding, config)

    elapsed = time.perf_counter() - start

    average_ms = (elapsed / iterations) * 1000
    throughput = iterations / elapsed

    print(f"Iterations: {iterations}")
    print(f"Total time: {elapsed:.6f} seconds")
    print(f"Average processing time: {average_ms:.6f} ms/finding")
    print(f"Throughput: {throughput:.2f} findings/second")


if __name__ == "__main__":
    main()