import os
import numpy as np
import cv2
import urllib
os.environ['CUDA_VISIBLE_DEVICES']='1'
from face_test.model_zoo.get_models import get_detection_model,get_landmark_model, get_ageGender_model,get_recognition_model
from face_test.face.get_result import *
from face_test.utils.util_common import draw_result,draw_result_sim, draw_result_land
from face_test.data.image import read_image
import matplotlib.pyplot as plt
from numpy import dot
from numpy.linalg import norm


# In[21]:


# detection_name='scrfd'
# detection_path = '/data/notebook/NAS/PTAS_Shared/resource/model/face/detection/scrfd_10g_bnkps.v8.4.trt'

detection_name='scrfd'
detection_path = '/data/notebook/NAS/PTAS_Shared/resource/model/face/detection/scrfd_10g_bnkps.onnx'
detection_thresh = 0.3 # detection threshold set

# landmark (None is landmark_name='')
landmark_name='3ddfa'
landmark_path = '/data/notebook/NAS/PTAS_Shared/resource/model/face/landmark/3ddfa_v2.onnx'

# recognition
recog_name = "arcface"
recog_path = "/data/notebook/NAS/PTAS_Shared/resource/model/face/embedding/res50_arcface_20220210.onnx"
recog_out_size=112
recog_num_features=512
recog_network='r50'
recog_fp16=True


# In[22]:


# 1. load models
detection_model = get_detection_model(detection_name,detection_path)
landmark_model = get_landmark_model(landmark_name,landmark_path)
recog_model = get_recognition_model(recog_name,recog_path,out_size=recog_out_size,num_features=recog_num_features,network=recog_network,fp16=recog_fp16)


from urllib.request import Request, urlopen

def detection(img,compare,combool):
    faces = []
    try:
        faces = get_detection(detection_name,detection_model,img,thresh=detection_thresh)
    except:
        return "False"
    if landmark_name and landmark_path:
        faces, param_lst, roi_box_lst = get_landmark(landmark_name,landmark_model,img,faces)

    faces = get_features(recog_name,recog_model,img,faces,to_bgr=True)
    
    if faces == []:
        return "False"
    if combool == False:
        if faces[0].pose[0]<5 and faces[0].pose[2]<5: #and faces[0].det_size > 80000:
            return faces
        else:
            #os.remove(input_path)
            return "False"
    else:  
        result = dot(faces[0].feat, compare[0].feat)/(norm(faces[0].feat)*norm(compare[0].feat))
        if result < 0.3:
            return "False"
            
        else:
            return faces
