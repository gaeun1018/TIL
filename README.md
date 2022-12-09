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

Run the following command for a c++ building

```
bazel build -c opt //tensorflow/lite:tensorflowlite
```

</br>

### 5.Result

You can get `libtensorflowlite.dylib` from the path `bazel-bin/tensorflow/lite/libtensorflowlite.dylib`



 <br/>  
 <br/> 
 
## Android build


