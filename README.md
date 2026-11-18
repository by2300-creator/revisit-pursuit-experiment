# ReVISit pursuit experiment

GitHub Pages deployment repository for the six-dot pursuit experiment.

The Pages workflow publishes the production archive. Check the Actions tab for the latest deployment status.

Current study: **4.0.0**. Optional demographics, 20 practice trials, 30 formal trials, two additional attention checks after formal trials 10 and 20, debrief, and thank you. Confidence uses five labeled levels. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for detailed recordings and validation requirements. Launch a fresh participant after updates; do not mix incomplete sessions from different versions.

- Participant entry: https://by2300-creator.github.io/revisit-pursuit-experiment/six-dot-motion
- Experimenter dashboard: https://by2300-creator.github.io/revisit-pursuit-experiment/experimenter
- Calibration: https://by2300-creator.github.io/revisit-pursuit-experiment/six-dot-motion/reviewer-sixDotCalibration

## Current data mode

This initial deployment uses browser-local storage. It is for HTTPS camera testing and supervised pilots with manual data export. It does not upload participant results to the experimenter. Enable data collection in the browser's experimenter dashboard before collecting local results. Connect Firebase or Supabase before unattended remote recruitment.

Eye tracking is enabled in the published study configuration. Each participant must consent, allow the webcam, and calibrate individually. Webcam images and audio are not recorded or uploaded by the eye-tracking feature. Actual gaze accuracy and saved trial samples must be checked in a pilot.

## Deployment

`site.zip` contains the production website. Repository Settings > Pages > Source is set to GitHub Actions. The workflow in `.github/workflows/pages.yml` publishes updates when the archive or WebGazer source package changes.

Rebuild from the local ReVISit project using PowerShell 7:

```powershell
./scripts/prepare-github-pages.ps1
```

Upload the resulting `deployment/github-pages/site.zip` to this repository to update the site. The script builds for `/revisit-pursuit-experiment/` and includes only runtime assets, study configuration, and license notices. It omits local environment files, participant exports, calibration result archives, and development backups. Experimenter settings stored in localhost are not automatically transferred to this HTTPS origin; use an exported applied study config when publishing customized settings.

ReVISit and WebGazer retain their included license notices. WebGazer 3.5.3 source/package: https://registry.npmjs.org/webgazer/-/webgazer-3.5.3.tgz
