# Submission Instructions

- The submissions should be in **submission.zip** file format.
- The **zip** file should contain only the **submission.csv** file.
- The format of **submission.csv** file should be as described below. 

## Submission File Format

The **submission file** (`submission.csv`) should have the following headers:

- **filename**: The filename corresponding to the increasing order of timestamps.
- **Tx, Ty, Tz**: The Translation vector for the spacecraft at that timestamp.
- **Qx, Qy, Qz, Qw**: The Quaternion vector for the spacecraft's orientation.

### Example `submission.csv` File

| timestamp         | Tx   | Ty   | Tz    | Qx   | Qy   | Qz    | Qw   |
| ---------------- | ---- | ---- | ----- | ---- | ---- | ----- | ---- |
| RT901_001 | 1.23 | 0.45 | -0.67 | 0.12 | 0.34 | -0.56 | 0.78 |
| RT901_002 | 1.25 | 0.47 | -0.65 | 0.13 | 0.36 | -0.55 | 0.79 |
| ...              | ...  | ...  | ...   | ...  | ...  | ...   | ...  |


The timestamp naming "RT901_001" corresponds to trajectory sequence RT901 at the timestamp of 0.1s or 100 ms.