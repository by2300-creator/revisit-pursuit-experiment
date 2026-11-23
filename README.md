# ReVISit pursuit experiment

GitHub Pages deployment repository for the six-dot pursuit experiment.

The Pages workflow publishes the production archive. Check the Actions tab for the latest deployment status.

Current study: **4.3.0**. Optional demographics, 20 practice trials, 30 formal trials, two additional attention checks after formal trials 10 and 20, debrief, and thank you. Confidence uses five labeled levels. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for detailed recordings and validation requirements. Launch a fresh participant after updates; do not mix incomplete sessions from different versions.

- Participant entry: https://by2300-creator.github.io/revisit-pursuit-experiment/six-dot-motion
- Experimenter dashboard: https://by2300-creator.github.io/revisit-pursuit-experiment/experimenter
- Calibration: https://by2300-creator.github.io/revisit-pursuit-experiment/six-dot-motion/reviewer-sixDotCalibration

## Current data mode

This initial deployment uses browser-local storage. It is for HTTPS camera testing and supervised pilots with manual data export. It does not upload participant results to the experimenter. Enable data collection in the browser's experimenter dashboard before collecting local results. Connect Firebase or Supabase before unattended remote recruitment.

RealEye Webcam Eye Tracker Light Open 1.1.0 is enabled in the published study configuration. Each participant must consent, allow the webcam, and calibrate individually. Webcam images and audio are not recorded or uploaded by the eye-tracking feature. Actual gaze accuracy and saved trial samples must be checked in a pilot.

## Deployment

GitHub Pages uses GitHub Actions. The workflow unpacks both release archives into the same directory. `site.zip` contains the ReVISit study and RealEye integration. `realeye-runtime.zip` contains the face landmark model and WebAssembly runtime. Commit both archives together when a release changes both components.

The published site includes build instructions and tracker source under `six-dot-motion/realeye/source/` and license notices under `six-dot-motion/realeye/notices/`.
