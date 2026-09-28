import numpy as np


def filter_peaks(mz, intensity, min_intensity=0.01):
    """Remove peaks below a normalized-intensity threshold."""

    mz = np.asarray(mz)
    intensity = np.asarray(intensity)

    mask = intensity >= min_intensity

    return mz[mask], intensity[mask]


def spectral_cosine_similarity(
    mz1,
    intensity1,
    mz2,
    intensity2,
    tolerance=0.01,
    min_intensity=0.01,
):
    """Calculate one-to-one intensity-weighted cosine similarity."""

    mz1, intensity1 = filter_peaks(
        mz1,
        intensity1,
        min_intensity,
    )

    mz2, intensity2 = filter_peaks(
        mz2,
        intensity2,
        min_intensity,
    )

    possible_matches = []

    for i in range(len(mz1)):
        differences = np.abs(mz2 - mz1[i])

        for j in np.where(differences <= tolerance)[0]:
            possible_matches.append(
                (differences[j], i, j)
            )

    possible_matches.sort(key=lambda x: x[0])

    used_1 = set()
    used_2 = set()

    numerator = 0.0

    for difference, i, j in possible_matches:

        if i in used_1 or j in used_2:
            continue

        used_1.add(i)
        used_2.add(j)

        numerator += intensity1[i] * intensity2[j]

    denominator = np.sqrt(
        np.sum(intensity1 ** 2)
        * np.sum(intensity2 ** 2)
    )

    if denominator == 0:
        return 0.0

    return numerator / denominator