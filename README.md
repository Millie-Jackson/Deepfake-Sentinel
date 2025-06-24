# Deepfake Sentinel

Deepfake Sentinel is a cross-modal desktop monitoring service that continuously watches video sources (folder drops, screen capture, webcam) and audio streams to detect AI-generated content in real-time. It leverages deep learning models for both video and speech, logs all detections, issues live desktop notifications, and provides a Streamlit dashboard for reviewing alerts. Built with end-to-end MLOps in mind, it features data ingestion, model training, serving, logging, CI/CD pipelines, and Docker-based deployment on Linux.

# 🚀 MVP Features

Below are the core MVP features and their current status (Sprint 1 in progress):

- Initialize repo structure & CI templates (GitHub Actions for lint/test) -> Complete
- Configure local MLflow server & logging -> Complete
- 
- Data EDA & preprocessing notebooks (FaceForensics++ video) -> In Progress
- Data EDA & preprocessing notebooks (ASVspoof audio) -> In Progress
- 
- Baseline PyTorch training scripts (video & audio) -> Planned
- Hyperparameter tuning integration (Optuna) -> Planned
- FastAPI detection services for video & audio -> Planned
- Folder watcher & screen grabber ingestion services -> Planned
- Audio listener ingestion service -> Planned
- Detection result logging & Linux desktop notifications -> Planned
- Streamlit dashboard for real-time alerts -> Planned
- Dockerization & CI/CD pipeline setup ->  Planned

# 🛠 Post-MVP Feature Ideas

- Detection Accuracy
- Cross-modal fusion of audio + video confidences
- Ensemble of multiple deepfake detectors
- Model drift detection & scheduled retraining
- Performance & Scale
- GPU acceleration with TorchScript/ONNX + CUDA
- High-frame-rate real-time screen capture
- Batch-mode processing of archived video files
- Platform Support
- Windows & macOS native installers (NSIS, pkgbuild)
- Android companion app or background service
- Browser extension to flag deepfakes on web pages
- UI/UX Enhancements
- React-based dashboard with filter/search & history playback
- Electron wrapper for a native desktop application
- Email / Slack alerts for high-severity detections
- Monitoring & Metrics
- Prometheus exporter & Grafana dashboard for system metrics
- Log aggregation (ELK Stack or Loki)
- Usage analytics (e.g., which detectors trigger most frequently)
- Auto-Updates & Operations
- Auto-update logic: check for new models and download automatically
- Automated package builds on Docker Hub / GitHub Packages with release tags

Feature ideas above are intended for v2.0 and beyond. The initial 3‑month MVP focuses on core detection, notifications, and dashboard functionality.

# 📊 EDA Findings & Limitations

![image](https://github.com/user-attachments/assets/b269bce6-1974-49d8-a559-bc838e8cf79c)

## Sample Size Comparison

50-frame sample: quick initial plot with visible dual peaks (~0–30 and ~150–220).

200-frame sample: smoother but nearly identical distribution.

500-frame attempt: crashed laptop (500 frames × ~6 MB each ≈ 3 GB), so limited to 200 frames for MVP.

## Key Insights
### Normalisation

Contrast bias: Pixel intensities cluster around very dark (0–50) and very bright (150–220) ranges, with fewer mid-tones (80–120). This indicates high-contrast scenes dominate the dataset.

std (Standard Deviation): quantifies spread of intensity values around the mean—a larger std means more variability in brightness.

### Augmentation Strategy

Random brightness/contrast jitter: during model training, apply random brightness shifts (e.g. ±20 %) and contrast adjustments (e.g. ±30 %) to simulate varied lighting and improve robustness.

### Sampling Notes

Representativeness: 200 frames sample ~6 % of videos. It aligns with smaller samples but may miss rare outliers; post-MVP we’ll batch-histogram larger subsets or full dataset.
