
from utils.random_name_generator import get_random_names
from sklearn.datasets.samples_generator import make_blobs
import pickle
import os

def generate_student_data_for_clustering(samples,groups,feature_list):
    X, y = make_blobs(n_samples=samples, centers=groups, n_features=len(feature_list), random_state=0, center_box=(1,10))
    stu_objs = []
    for data_row in X:
        stu_obj = {}
        stu_obj["stu_name"] = get_random_names(1,None)[0]
        i = 0
        for feature in feature_list:
            stu_obj[feature] = data_row[i]
            i = i + 1
        stu_objs.append(stu_obj)
    pickle.dump(stu_objs, open("student_data_cluster.pkl", "wb"))



#Test code
generate_student_data_for_clustering(30,5,["past_perf","eng_level","stu_interest","sp_needs"])

student_list = pickle.load( open( "student_data_cluster.pkl", "rb" ))
print( '\n'.join('{}: {}'.format(*k) for k in enumerate(student_list)))