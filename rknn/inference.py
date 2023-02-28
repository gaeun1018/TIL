import os
import urllib
import urllib.request
import traceback
import time
import sys
import numpy as np
import cv2
from rknnlite.api import RKNNLite


def inference(input, RKNN_MODEL):

    # Create RKNN object
    rknn_lite = RKNNLite(verbose=True)

    
   # load RKNN model
    print('--> Load RKNN model')
    ret = rknn_lite.load_rknn(RKNN_MODEL)
    if ret != 0:
        print('Load RKNN model failed')
        return 0;
    print('done')

    # Init runtime environment
    print('--> Init runtime environment')
    ret = rknn_lite.init_runtime()
    if ret != 0:
        print('Init runtime environment failed!')
        return 0;
    print('done')

    outputs = rknn_lite.inference([input])
    
    return outputs


def main(args):
    img = cv2.imread(args.input)
    rknn = args.rknn
    inference(img,rknn)
    
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='rknn inference')
    
    parser.add_argument('--rknn', default='', type=str, help='rknn model path list')
    parser.add_argument('--input', default='', type=str, help='input image path')

    args = parser.parse_args()
    main(args)
