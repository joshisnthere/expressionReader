"""
Pure geometry, no trained model: distances between mediapipe face-mesh
landmarks decide a rough expression label. Not clinically accurate, just a
fun heuristic.
"""

import math

LEFT_EYE = [386, 385, 387, 373, 380, 362]
RIGHT_EYE = [159, 158, 160, 144, 153, 133]
MOUTH_TOP = 13
MOUTH_BOTTOM = 14
MOUTH_LEFT = 61
MOUTH_RIGHT = 291
LEFT_EYEBROW = 105
LEFT_EYE_TOP = 159


def _dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)


def _eye_aspect_ratio(landmarks, idxs):
    p = [landmarks[i] for i in idxs]
    vertical = _dist(p[1], p[5]) + _dist(p[2], p[4])
    horizontal = _dist(p[0], p[3])
    return vertical / (2.0 * horizontal + 1e-6)