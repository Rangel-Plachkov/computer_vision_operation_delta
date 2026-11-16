# 📤 Submission Instructions

To ensure your results are processed correctly, please follow the formatting guidelines below.

## Phase 1: Accuracy Scoring

### 📦 Recommended Submission Structure
Your submission must be a single `.zip` file. **Do not zip a folder;** select the files directly and compress them.

```yaml
submission.zip
├── detection.csv           # Required for Detection & Classification
├── test_00000_layer.npz    # Segmentation mask for image 00000
├── test_00001_layer.npz    # Segmentation mask for image 00001
└── ...                     # Remaining .npz files
```

---

### 🛰️ Task: Spacecraft Classification & Detection

The scoring program specifically looks for a file named **`detection.csv`** at the root of your zip file.

#### CSV Format Requirements
The file must include a header row and follow this structure:

| filename | class | bbox |
| :--- | :--- | :--- |
| `test_00000_img.jpg` | `VenusExpress` | `(100, 200, 300, 400)` |
| `test_00001_img.jpg` | `Cheops` | `(120, 240, 310, 420)` |

**Column Definitions:**
*   **`filename`**: The exact filename of the test image.
*   **`class`**: The predicted class label (**Case Sensitive**).
*   **`bbox`**: Bounding box coordinates in the format `(x_min, y_min, x_max, y_max)`.

---

### 🛰️ Task: Spacecraft component segmentation

The scoring program identifies masks by scanning for `.npz` files.

#### Naming Convention
The `.npz` filename must correspond exactly to the image it represents:

| Test Image | Required NPZ Filename |
| :--- | :--- |
| `test_00000_img.jpg` | `test_00000_layer.npz` |
| `test_00001_img.jpg` | `test_00001_layer.npz` |

#### How to Generate
We provide a `submission.py` script to help convert your binary mask images (JPG/PNG) into the required compressed NumPy format.

```bash
# Example usage:
python submission.py --input_dir predicted_masks/ --output_dir submission_folder/
```

---

### 🛑 Submission Rules & Limits

*   **Submission Frequency:** Maximum of **4 submissions per day** (200 total per team).
*   **Zipping Method:** Select the `detection.csv` and all `.npz` files together and zip them directly. 
    *   ❌ *Do not* zip a folder containing the files.
    *   ✅ *Do* zip the files themselves so they appear at the "root" of the archive.

---

## Phase 2: Model Evaluation & Final Scoring

After the leaderboard phase, qualifying participants must undergo verification to calculate the final efficiency scores.

*   **Requirements:** You must provide your **evaluation code** and **model weights** in a single `.zip` file.
*   **Purpose:** This allows the organizers to verify the $S_{flops}$ and $S_{params}$ metrics used in the final $S_{final}$ calculation.
  
---