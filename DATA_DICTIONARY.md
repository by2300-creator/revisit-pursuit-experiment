# Pursuit pilot v4 data

The complete ReVISit JSON download is the authoritative export. Preserve it alongside any flattened CSV. Fields containing JSON strings need JSON parsing; nested arrays should not be discarded during analysis. Data remains in the participant browser until manually exported and returned.

## Study flow

Registration → optional demographics → instructions → 20 training trials → break → 30 formal trials with extra attention checks immediately after formal trial 10 and 20 → debrief → thank you → Finish and download data.

Confidence: 1 not confident; 2 slightly confident; 3 moderately confident; 4 confident; 5 very confident. This differs from earlier 4-point pilot data; use the recorded study version and `dataVersion=pursuit-detailed-v2` to separate versions.

## Participant records

- `participantAssignment`: participant number, A–F tag/cohort, seed/order assignment. ReVISit also stores its generated participant identifier.
- `demographics` (JSON): optional age, gender, current vision correction, known color-vision difficulty, handedness and input device. Blank age is null; skipped categorical questions are `prefer_not_to_answer`. Includes update time, elapsed time, and browser/display environment. No name or contact information is requested.
- `debriefViewedAt`: ISO timestamp when the participant reaches the debrief; camera is stopped here.
- ReVISit answer records retain component identifiers and step start/end timestamps. Use endTime for the Next/Continue submission boundary; the custom interaction log is captured through the latest response change, not a separate timestamp for the framework's Next click.

## Every stimulus response

- `selectedChaserId`, `selectedPreyId`, `confidence`, `confidenceLabel`.
- `trialMetadata`: trial index, phase, training/check flags, separate attention-check index and position, formal-analysis exclusion flag, feedback status, correct identities, separate/pair correctness, participant allocation and seed/order details.
- Full condition settings: prey angle, trace type/duration, all dot colors, fixation duration, applied motion speeds, pursuit fraction, subtlety and update interval; calibration profile/ID and protocol/appearance versions. `appliedMotionControls` records the actual overrides used in attention checks.
- `responseRtMs`: first accepted dot response since freeze. `pairRtMs`: latest completed pair since freeze. Confidence-change timing and every selection/revision are in the event log.
- `motionDiagnostics` (JSON): distances, overlap diagnostics, buffer/turn events, wall hits, heading-update counts, random-turn counts, final dot positions/velocities/headings, effective motion settings and stationary-distractor flag.
- Attention checks: four distractors remain exactly stationary; only chaser/prey move. Pursuit fraction is 1, subtlety 0°, heading updates every simulation step (16 ms requested, 60 Hz integrator). No traces or private invisible chasers. Pass means both identities are correct, irrespective of confidence. Check trials are additional to the 30 formal trials and are not automatically used to exclude a participant.

## Display and interaction log

`trialTelemetry` (JSON) stores:

- UTC start and performance time origin, viewport/screen size, pixel ratio, color depth, browser user agent, language, timezone offset, secure-context status, touch support and canvas dimensions/bounds.
- Every animation callback reported by the stimulus: phase, wall clock, simulation clock, all visible dot positions, page visibility and window focus. These are reported display frames, not a guarantee of physical monitor presentation. Fixation frames contain no visible dots.
- Pointer coordinates and input type, hit-test candidates (including misses), color-button selections, role changes, rejected same-dot attempts, clear actions, confidence changes, feedback requests, visibility/focus/resize/fullscreen events.
- Mean/max frame interval and counts over 50 ms; data caps and dropped-record counts are explicit (20,000 frames, 5,000 interaction events per trial).

Coordinates are CSS viewport pixels or 900 × 560 logical canvas pixels as labeled. Performance clocks are milliseconds, simulation clocks are milliseconds, and motion diagnostics use seconds where labeled. Use the logged coordinate conventions rather than assuming device pixels or visual degrees.

## Eye tracking

`eyeTracking` (JSON) includes provider, status, calibration validation targets/errors/sample counts, all calibration attempts for that camera session, startup error, timing origin and events. Studies 4.1.0 and 4.2.0 use RealEye Webcam Eye Tracker Light Open 1.1.0. Participants click 17 calibration targets and then follow five validation targets. Study 4.2.0 records the calibration protocol, accepted training frame counts, and validation counts, duration and median error at each target. Each of the five targets requires at least eight valid estimates and a median error no greater than 15% of the shorter viewport dimension. Study 4.0.0 used WebGazer.

All provider gaze callbacks during fixation and motion are retained (no artificial 20 Hz downsampling), including null/invalid gaze. Samples include viewport/canvas coordinates, inside-canvas status, visibility, frame age, simulation time and displayed dot coordinates. A 20,000-sample cap has an explicit dropped-sample count. Response-screen gaze is not recorded. Quality summaries include valid/missing/inside counts, valid fraction and maximum inter-callback gap. Callback absence cannot be interpreted as zero error or valid fixation.

Tracking resumes for every tracked trial; the training-to-formal break pauses prediction but retains calibration. A viewport change or a trial with no valid samples invalidates calibration. Startup times out with a visible error instead of waiting indefinitely. The debrief and study exit stop the camera. Gaze estimates are approximate: validation passing does not establish dot-level precision. No webcam images, audio, face embeddings, IP addresses or global keystrokes are included in the experiment export.

## Pilot validation still required

With a real participant, grant the webcam, calibrate, complete at least two training trials, cross the formal break, complete the study and inspect the downloaded JSON. Check nonempty motion gaze, distinct per-trial timestamps, confidence values 1–5, demographic answers, two correctly placed attention checks and the terminal pages. Frame/model unit tests cannot establish real-person webcam accuracy. Never treat mock gaze as participant data.
