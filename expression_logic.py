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