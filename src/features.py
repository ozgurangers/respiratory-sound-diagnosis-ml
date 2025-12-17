import numpy as np

def extract_feature_vector(corr_map):
    return corr_map[0, :]

def build_feature_matrix(corr_maps):
    return np.array([extract_feature_vector(cm) for cm in corr_maps])
