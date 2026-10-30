# Supplied teaching record, not live deployment evidence

Previous known-good version: v1.4.2; image parcelboard:v1.4.2.
Candidate fixes incorrect basket totals without adding API features or breaking compatibility. Candidate must be next PATCH release. Issue reference: fixtures/release-record.md#basket-total-fix (local evidence reference, not an invented GitHub issue).

## Basket total fix

Application total(25,3) now returns 75. Existing local test checks this behaviour. No production deployment has taken place. Production approval is NOT REQUESTED. No staging validation or image provenance verification supplied.

## Hypothetical incident

A supplied incident scenario AFTER a hypothetical deployment reports HTTP 5xx rising from 0.2% to 12% for five minutes. Previous image v1.4.2 is available according to this scenario. No database/schema changes. Team policy: rollback when 5xx exceeds 5% for five minutes and known-good compatible image exists. Health, total calculation and errors returning below 1% for five minutes must be checked after rollback. These are scenario criteria, not observations from your run.

Proposed command shape: kubectl set image deployment/parcelboard app=parcelboard:<known-good-version>. Do not execute; no cluster required. Current production decision must reflect missing approval, staging proof and artifact verification. Passing one local test is not release readiness.
