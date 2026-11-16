# Evaluation Method

For this stream, both position and orientation accuracies will be evaluated. The metric is largely inspired by the [SPEED+ Challenge](https://kelvins.esa.int/pose-estimation-2021/).

More precisely, we are going to sum the **relative position error** and **the geodesic orientation error** for each frame, then average these scores over all the frames and trajectories.