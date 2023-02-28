import os
import urllib
import urllib.request
import traceback
import time
import sys
import numpy as np
import cv2
from rknn.api import RKNN
import argparse
from argparse import ArgumentParser, Namespace

def build_rknn(ONNX_MODEL,RKNN_MODEL,pf,mean,std,data):
    # Create RKNN object
    rknn = RKNN(verbose=True)

    # pre-process config
    print('--> config model')
    rknn.config(mean_values=mean, std_values=std,target_platform=pf)
    print('done')  

    # Load model
    print('--> Loading model')
    ret = rknn.load_onnx(model=ONNX_MODEL)
    if ret != 0:
        print('Load model failed!')
        return 0;
    print('done')

    # Build model
    print('--> Building model')
    ret = rknn.build(do_quantization=True, dataset=data)
    if ret != 0:
        print('Build model failed!')
        return 0;
    print('done')

    # Export rknn model
    print('--> Export rknn model')
    ret = rknn.export_rknn(RKNN_MODEL)
    if ret != 0:
        print('Export rknn model failed!')
        return 0;
    print('done')
    
def main(args):
#     build_rknn(args.onnx,args.rknn,args.platform,args.mean,args.std,args.data)
    print(args.mean)
    
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='rknn convert')
    
    parser.add_argument('--onnx', default='', type=str, help='onnx model path')
    parser.add_argument('--rknn', default='', type=str, help='rknn model path')
    parser.add_argument('--platform', default='rk3588', type=str, help='target platform')
    parser.add_argument('--mean', default=[127.5,127.5,127.5], type=float, help='mean value')
    parser.add_argument('--std', default=[127.5,127.5,127.5], type=float, help='std value')
    parser.add_argument('--data', default='dataset.txt', type=str, help='dataset path')

    args = parser.parse_args()
    main(args)
