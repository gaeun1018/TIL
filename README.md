# REC2REC

You can easily add a rec file and add a mask parameter to the rec file.

If you add a rec file to the rec file, you can enter ```20000``` sheets per second.

If you add a mask parameter, ```5``` sheets per second are added.



# SETUP
### 1. Install Requirements

1. Please make sure that the following packages are installed:

```
Pip install numpy, cython, onnxruntime, mxnet 
```
  
2. ```Pip install insightface```


### 2. Download Models
  ```insightface-cli model.download antelope```
  or [antelope](https://onedrive.live.com/?authkey=%21ADJ0aAOSsc90neY&cid=4A83B6B633B029CC&id=4A83B6B633B029CC%215837&parId=4A83B6B633B029CC%215834&action=locate)
  
  model will be located at ```~/.insightface/models/antelope```
  
  <br>
  
  Please ensure the files are extracted to these locations within your local copy of the repository:
  ```
  ~/.insightface/models/antelope/buffalo_l/BFM.mat
  ~/.insightface/models/antelope/buffalo_l/BFM_UV.mat
  ```

# Working

1. Open terminal. Go into the cloned project directory and type the following command:
```
python rec2rec.py --input inputpath --plus pluspath --mask


--input => Put the path that contains the original train.rec

--plus => Put the path that contains the train.rec that you want to add.

--mask => To add a mask parameter, add this command
```



The ```complete.rec, complete.idx / complete_m.rec, complete_m.idx``` file will be created in the input path
