MODEL_NAMES=(
    "cmt_aug_mbf_arcface_20220712"
    "3ddfa_v2"
    "glint360k-r50-arcface"
    "scrfd_10g_bnkps"
)

MODEL_PATH = "/data/notebook/notebook/rknn-toolkit2/examples/nse/"
RESULT_PATH = "/data/notebook/notebook/rknn-toolkit2/examples/nse/"
FLATFORM = "rk3588"
MEAN = "[127.5,127.5,127.5]"
STD = "[127.5,127.5,127.5]"
IMAGE_PATH = "/data/notebook/notebook/rknn-toolkit2/examples/nse/ptas_img"


DATASET_NAMES=(
    "arcface"
    "ddfa_v2"
    "glint360k"
    "scrfd"
)

for (( j = 0 ; j < ${#DATASET_NAMES[@]} ; j++ )) ; do
    for (( i = 0 ; i < ${#MODEL_NAMES[@]} ; i++ )) ; do
        echo "Start ${MODEL_NAMES[$i]}"

        CUDA_VISIBLE_DEVICES=1 \
        python build.py \
            --onnx MODEL_PATH+"${DATASET_NAMES[$j]}/${MODEL_NAMES[$i]}.onnx" \
            --rknn RESULT_PATH
            --platform FLATFORM \
            --mean MEAN \
            --std STD \
            --data IMAGE_PATH
    
        echo "Finish ${MODEL_NAMES[$i]}"
    done
    echo "Finish ${DATASET_NAMES[$j]}"
done
