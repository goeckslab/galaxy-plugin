# Running and troubleshooting

## Submission and progress

- `run_tool` accepts a request, not a completed analysis. Retain its handle for `get_tool_request_status`; use the invocation handle with `get_invocations` for workflows. Scheduling alone is not completed execution.
- Use `get_run_status` after submission or for requested visible progress. The card refreshes while visible and pauses after a failed check. Verify background progress with data-only status tools and returned job handles, not repeated cards.
- For requested execution, monitor to a terminal state using the client's waiting mechanism. For status-only requests, report the existing run. Invocation lookup requires its handle; the service cannot find invocations from a history alone.

| Observation | Next action |
| --- | --- |
| Accepted, queued or running | Continue checking the same run; outputs are not ready. |
| Status query fails | Preserve the last known state and handles, mark the current state unconfirmed, and retry the read. Do not blame Galaxy without evidence. |
| Submission times out without rejection | Outcome is unknown. Recover the original run if possible; if its existence cannot be established, report that blocker instead of resubmitting. |
| Run is `empty` | No jobs ran. Inspect inputs and request details, not an endless poll. |
| Run reports failure | Inspect its jobs; some may still be running. Do not restart the whole analysis. |
| Execution completed | Verify outputs against the scientific objective. |

## Diagnose before retrying

1. Read `get_job_details` and invocation messages. Use returned logs and exit information; if absent, refer to Galaxy's job details. An exit code alone does not establish a cause.
2. For paused or downstream failures, trace upstream inputs. Check readiness, format, reference compatibility and reported quota/resource limits. Do not relabel a genome build merely to hide a mismatch.
3. For empty or small outputs, compare actual records with inputs, filters and expected results. Zero records can be valid; distinguish that from an `empty` run that created no jobs. Do not change filters solely to produce nonempty output.
4. Retry execution only after confirming that the original run was not created, or that a diagnosed failure requires a corrected run within the user's scope. Account for still-running jobs first.

## Example: requested FastQC on two authorized FASTQ URLs

1. Resolve the site and R1/R2 pairing; create a history, upload both URLs and wait for ready datasets.
2. Find installed FastQC, inspect its schema and submit each HDA input once.
3. Monitor both tool-request handles to terminal states.
4. Read completed RawData and relevant HTML using [Reading results](reports.md); report measured metrics, warnings and source links. Existing QC reports require no new analysis.
