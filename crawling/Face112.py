import os
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import os.path as osp

os.environ['CUDA_VISIBLE_DEVICES']='1'

from face_test.model_zoo.model_common import load_onnx,load_tensorRT,load_tensorRT_multiple,load_openvino
from face_test.model_zoo.get_models import get_detection_model,get_landmark_model,get_recognition_model,get_ageGender_model
from face_test.face.get_result import get_detection, get_landmark, get_features,get_ageGender
from face_test.data import read_image,resize_image_multi

from face_test.utils.util_common import draw_result,draw_result_land,draw_result_sim

import os
import cv2


# In[21]:


detection_name='scrfd'
detection_path = '/data/notebook/NAS/PTAS_Shared/resource/model/face/detection/scrfd_10g_bnkps.onnx'
#detection_name='retinaface_torch'
#detection_path = '/data/notebook/NAS/FaceDetection/models/retinaface_torch/retinaface_r50_final_multiple.onnx'
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


def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image


def detection(img):
    faces = []
    try:
        faces = get_detection(detection_name,detection_model,img,thresh=detection_thresh)
    except:
        return False
    if faces == []:
        return False

    if landmark_name and landmark_path:
        faces, param_lst, roi_box_lst = get_landmark(landmark_name,landmark_model,img,faces)
        
    faces = get_features(recog_name,recog_model,img,faces,to_bgr=True)
    
    if faces == []:
        return False
    
    return faces

def main(args):
    url = args.input

    n=0
    nlst = os.listdir(url)
    nlst.sort()
    for img in nlst:
        image = cv2.imread(url+img)
        result = detection(image)
        if result!=False:
            img = img.replace("jpeg","png")
            cv2.imwrite(osp.join(args.result, img),result[0].aimg)
            
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Change size to 112*112 for face')

    parser.add_argument('--input', default='', type=str, help='')
    parser.add_argument('--result', default='', type=str, help='')
    
    args = parser.parse_args()
    main(args)