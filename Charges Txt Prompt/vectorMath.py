# Decided not to finish out for the charges prompt
import numpy as np
import numpy.linalg as npl


# Given a vector of from [n1, n2, ... n] returns the input vector normalized (unit vector)
def normalize_vector(vector):
    normalized_vector = vector
    magnitude = npl.norm(vector)

    for i in range(vector.size + 1):
        normalized_vector[i] = (vector[i] / magnitude)

    return normalized_vector


# Normalizes an array of vectors
def normalize_vectors(vectors):
    normalized_vectors = vectors
    num_rows , num_columns = vectors.shape

    for i in range(num_rows):
        vectors[i , :] = normalize_vector(vectors[i , :])

    return normalized_vectors