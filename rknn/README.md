# rknn_toolkit

## rknn_toolkit2 


```
sudo apt-get install python3 python3-dev python3-pip
sudo apt-get install libxslt1-dev zlib1g zlib1g-dev libglib2.0-0 libsm6 \ libgl1-mesa-glx libprotobuf-dev gcc
```

<br>

https://github.com/rockchip-linux/rknn-toolkit2

> You can install rknn_toolkit2 from the link above

<br>

```
pip3 install -r doc/requirements*.txt

cd package/

sudo pip3 install rknn_toolkit2*.whl
```
 
 
## rknn model convert
Convert model to rknn format via attached build.py

<br>

```python
build.py --onnx ONNX_MODEL_TXT_PATH --platform TARGET_PLATFORM --mean MEAN_VALUE_TXT_PATH --std STD_VALUE_TXT_PATH --data DATASET_TXT_PATH
```

* ```mean_values, std_values``` : Set the std and mean value of the input.
* ```target_platform``` : Specify which target chip platform the RKNN model is based on.
"rk3566", "rk3568", "rk3588", "rv1103" and "rv1106" are currently supported.


* ```dataset``` : A input data set for rectifying quantization parameters. 

  ```
    a.jpg
    b.jpg
  ```
  Complete the text file in the format above.
  
  
## rknn inference
Convert rknn model via attached inference.py


<br>

```python
inference.py --rknn RKNN_MODEL_PATH --input INPUT_IMAGE_PATH
```
