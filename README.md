# release-evidence-repair

Intentionally broken DevOps Foundation Module 3 starter. Only documented faults/draft gaps require repair. Existing application/test is correct.

## Setup

Fork public repository and clone YOUR fork. Python 3.10+ and Git required; no packages, cloud account, Docker, Kubernetes cluster, credentials or paid services.

```bash
git clone https://github.com/YOUR-USERNAME/release-evidence-repair.git
cd release-evidence-repair
git switch -c fix/module3
python3 -m unittest -v
python3 check.py all
```

Initial app test passes; initial static contract check fails by design. Capture original failures before editing. Commands run from repository root. No inherited workflow runs required. Setup is outside assessment; report unrelated environment failures.

## Allowed edits

release.json, release-notes.md, recovery-review.md; create annotated release tag. Keep checker, application, tests and fixtures unchanged. No bypasses, removed checks or fabricated evidence.

## Required release record

Read fixtures/release-record.md. Fix three release.json fields: next PATCH version after v1.4.2, matching parcelboard image version, and change_type PATCH. Commit all completed repairs and written files, then create annotated candidate tag on final commit. Show tag type and tag-to-HEAD match. No registry/build claim is implied by an image string or Git tag.

Complete four release-note lines: specific scope and traceability (candidate tag, actual final commit, supplied issue reference); actual local test evidence and its limit; named operational risk with mitigation; known-good rollback target and required checks. For final commit ID, use `HEAD at annotated candidate tag` in committed note and show resolved hash in PDF, avoiding self-referential commit hash editing.

Complete five recovery lines using supplied hypothetical incident: signals, recovery decision/reason, known-good image/proposed kubectl command, post-recovery checks, honest production readiness/limits. Label scenario evidence separately from actual local test output. Do not execute Kubernetes commands or claim deployment.

## Evidence

Follow assessment's three tasks. Submit one PDF with real screenshots, original failure, corrected diff, passing static checks and requested reasoning. Grade only the three tasks and requested evidence; repository/fork URLs and branch names are not required or graded. Annotated-tag and matching-hash proof remain Task 1 technical evidence, not submission metadata. At least one screenshot per task. Written reports require manual grading. No PR or video. Do not run production workflows or expose secrets. Static PASS proves only exercise contract.
