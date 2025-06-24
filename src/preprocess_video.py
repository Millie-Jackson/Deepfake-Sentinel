# src/preprocess_video.py

import cv2, os, glob


RAW_DIR = "data/video_raw"
OUT_DIR = "data video_sample"
TARGET_SIZE = (256, 256)

os.makedirs(OUT_DIR, exist_ok=True)

for vid_path in glob.glob(f"{RAW_DIR}/*.mp4"):
    name = os.path.splitext(os.path.basename(vid_path))[0]
    out_sub = os.path.join(OUT_DIR, name)
    os.makedirs(out_sub, exist_ok=True)

    cap = cv2.VideoCapture(vid_path)
    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Resize & center-crop
        h, w = frame.shape[:2]
        # Resize preserving aspect ratio & crop
        scale = max(TARGET_SIZE[0]/h, TARGET_SIZE[1]/w)
        new_h, new_w = int(h*scale), int(w*scale)
        frame_resized = cv2.resize(frame, (new_w, new_h))
        # Center crop
        y0 = (new_h - TARGET_SIZE[0])//2
        x0 = (new_w - TARGET_SIZE[1])//2
        crop = frame_resized[y0:y0+TARGET_SIZE[0], x0:x0+TARGET_SIZE[1]]

        # Save
        out_file = os.path.join(out_sub, f"frame_{idx:04d}.jpg")
        cv2.imwrite(out_file, crop)
        idx += 1
    cap.release()
