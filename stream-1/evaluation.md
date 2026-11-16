# 🏆 Evaluation Metrics

The final leaderboard ranking is determined by a comprehensive score that balances **Model Accuracy (70%)** and **Model Efficiency (30%)**. This ensures that the winning solutions are not only precise but also optimized for real-world deployment.

## 1. Final Score Calculation ($S_{final}$)

The **Final Score** is a weighted sum of accuracy and computational efficiency:

$$S_{final} = (0.70 \times S_{acc}) + (0.15 \times S_{flops}) + (0.15 \times S_{params})$$

| Component | Weight | Metric |
| :--- | :---: | :--- |
| **Accuracy ($S_{acc}$)** | 70% | Combined score across Classification, Detection, and Segmentation. |
| **FLOPS ($S_{flops}$)** | 15% | Efficiency score based on Giga-FLOPS. |
| **Parameters ($S_{params}$)** | 15% | Efficiency score based on total Parameters (Millions). |

---

## 2. Accuracy Score Detail ($S_{acc}$)

The accuracy score is determined by a weighted multi-task evaluation:

$$S_{acc} = (0.20 \times S_{cls}) + (0.40 \times S_{det}) + (0.40 \times S_{seg})$$

### A. Image-Level Classification ($S_{cls}$) — **20% Weight**
While each image belongs to exactly **one ground truth class**, your model may predict multiple objects.
*   **Selection Rule:** The evaluator identifies the predicted bounding box with the **largest area**. The class label of this largest box is used as the final prediction for the image.
*   **Tie-breaking:** If multiple boxes have the same maximum area, the first occurrence is prioritized.
*   **Scoring:** Calculated as the percentage of images where the largest predicted box matches the ground truth label. Images with no predictions receive a score of zero.

### B. Object Detection ($S_{det}$) — **40% Weight**
This evaluates the precision and localization of all predicted bounding boxes.
*   **Matching:** Predicted boxes are matched to Ground Truth (GT) boxes using **COCO Multi-Thresholding**.
*   **Constraint:** A match is only valid if the predicted label matches the GT label.
*   **Thresholding:** For every GT box, the score is calculated across 10 IoU thresholds:  
    `[0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]`
*   **Metric:** $S_{det}$ is the mean success rate across all thresholds and all GT boxes.

### C. Semantic Segmentation ($S_{seg}$) — **40% Weight**
Evaluates pixel-level masks for the **Body** (Channel 0) and **Panel** (Channel 2).
*   **Adaptive Evaluation:** To ensure fairness regarding component size, a **5% pixel ratio rule** is applied:
    *   If **Panel** pixels < 5% of **Body** pixels: Only the **Body** mask is evaluated.
    *   If **Body** pixels < 5% of **Panel** pixels: Only the **Panel** mask is evaluated.
    *   **Otherwise:** Both masks are evaluated and the results are averaged.
*   **Metric:** The IoU for required channels is compared against 10 thresholds (`0.50` to `0.95`). The final score is the mean performance across all thresholds and images.

---

## 3. Efficiency & Performance Evaluation

To encourage lightweight models, 30% of the total score is dedicated to efficiency. Scores are normalized from 0 to 1.

### Efficiency Scoring Logic
If a model's complexity exceeds the maximum constraints, the score drops toward zero.

*   **FLOPS Score ($S_{flops}$):**
    $$S_{flops} = \max\left(0, 1 - \frac{\text{Model FLOPS (B)}}{100.0}\right)$$
    > **Target:** Under 100 B-FLOPs.

*   **Parameters Score ($S_{params}$):**
    $$S_{params} = \max\left(0, 1 - \frac{\text{Model Parameters (M)}}{30.0}\right)$$
    > **Target:** Under 30 Million parameters.

⚠️ Solutions with the smallest footprint and highest accuracy rank highest.

---

## 📋 Submission Requirements

### Phase 1: Evaluation Files

#### 1. Detection & Classification (`detection.csv`)
Submit a single CSV file containing all detected instances for every image:
*   `image_id`: Image filename (e.g., `img_001.jpg`).
*   `class`: Predicted label.
*   `bbox`: Bounding box coordinates in format `[x1, y1, x2, y2]`.

#### 2. Segmentation (`.npz` files)
Submit one compressed numpy file per image containing a `data` key:
*   **Format:** Boolean array of shape `(H, W, 3)`.
*   **Channel 0:** "Body" binary mask.
*   **Channel 2:** "Panel" binary mask.
*   **Resolution:** Must match the original image dimensions exactly.

### Phase 2: Verification
*   **Efficiency Verification:** Participants must provide their **evaluation code** and **model weights** for offline verification of FLOPS and Parameter counts as part of the final documentation.
  
---