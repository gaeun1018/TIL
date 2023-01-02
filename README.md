# Android tensorflow-lite(C++)




## Build tensorflow-lite for C++
### 1. Download tensorflow-lite

You can download tensorflow-lite from the link below.


https://github.com/tensorflow/tensorflow/releases  
  
 <br/> 

### 2. Download bazel

You can download bazel by following the link below(Mac OS)

https://bazel.build/install/os-x

 <br/> 

### 3. Configure

Run the following command at the top of the downloaded tensorflow folder

```
./configure
```

 <br/> 
 
1. Python Option
<img width="1749" alt="image" src="https://user-images.githubusercontent.com/90126829/206641189-e869c16e-8b1d-40b4-a44c-2fa86c67262c.png">

Ask for the path to Python and Python libraries  
Press Enter to automatically enter the default value

 <br/> 
2. Library, Compiler Option
<img width="747" alt="image" src="https://user-images.githubusercontent.com/90126829/206642138-26e41904-05ca-468c-ac77-4ec76316f204.png">

Ask if you want to build ROCm, the library when using GPU acceleration on AMD  
Ask if you want to build CUDA, the library used to use NVIDIA's GPU acceleration  
Ask if you want to download Clang compiler   
 <br/> 

3. Compile Option
<img width="1059" alt="image" src="https://user-images.githubusercontent.com/90126829/206643821-0f2d1307-4030-4038-b1ed-209de78e2db0.png">

Ask for the compile flag  
Press Enter to automatically enter the default value

 <br/> 
4. Android/iOS Option
<img width="831" alt="image" src="https://user-images.githubusercontent.com/90126829/206644187-f3d0a9ac-5a96-4f0f-b61a-4fc7589400bb.png">
<img width="598" alt="image" src="https://user-images.githubusercontent.com/90126829/206644244-1221ca5b-4619-44d9-9be4-6e0cbdaa0e0b.png">

Ask about android/iOS build  

</br>

### 4. Build

arm64-v8a
```
--config=android_arm64 --cpu=arm64-v8a
```

armeabi-v7a
```
--config=android_arm --cpu=armeabi-v7a
```
</br>

CPU(default)
```
bazel build -c opt --config=android_arm64 --cpu=arm64-v8a //tensorflow/lite:tensorflowlite
```

GPU
```
bazel build -c opt --config=android_arm64 --cpu=arm64-v8a //tensorflow/lite/delegates/gpu:libtensorflowlite_gpu_delegate.so
```

NNAPI
```
bazel build -c opt --config=android_arm64 --cpu=arm64-v8a //tensorflow/lite/delegates/nnapi:nnapi_delegate_no_nnapi_implementation
bazel build -c opt --config=android_arm64 --cpu=arm64-v8a //tensorflow/lite/nnapi:nnapi_implementation
bazel build -c opt --config=android_arm64 --cpu=arm64-v8a //tensorflow/lite/nnapi:nnapi_uti
```

 <br/>  
 <br/> 
 
## Opencv import 


### 1. Download Opencv library

You can download opencv from the link below.

https://opencv.org/releases/

</br>

### 2. Import module

In Android Studio ```File > New > Import Module```

Select ```${OpenCVpath}/sdk```  
</br>

The opencv folder would have been added to your project

Clear the ```apply plugin: 'kotlin-android'``` part of the build.gradle file in the opencv folder

</br>

```File > Project Structure > Dependencies```

![image](https://user-images.githubusercontent.com/90126829/207540935-9ace93c3-1fe1-4c9e-b7f2-9efddcd6c6ca.png)


You can add opencv module

</br>

```
set(pathOPENCV ~/AndroidStudioProjects/(project name)/opencv)
set(path_OPENCV ${pathOPENCV}/native/libs/${ANDROID_ABI}/libopencv_java4.so)

include_directories(~/AndroidStudioProjects/(project name)/opencv/native/jni/include)

add_library(lib_opencv SHARED IMPORTED)
set_target_properties(lib_opencv PROPERTIES IMPORTED_LOCATION ${path_OPENCV})

target_link_libraries(
        (project name)
        lib_opencv
        ${log-lib})
```

Add the code above to the CMAkeLists file
</br>
