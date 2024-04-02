# 예측하기 전에 모델이 필요함. -> Tensorflow에서 이미지모델을 다운 받아서 불러오기

from PIL.Image import Image # pip install pillow
import numpy as np # AI가 이해할 수 있는 데이터로 변경을 해줘야 한다 -> numpy 사용
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from model_loader import model


# 이미지를 예측해서 결과를 알려주는 함수
def predict(image: Image):
    image = np.asarray(image.resize((224, 224)))[..., :3] # RGB
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0 # Scaler(정규화) -> 이미지 데이터가 -1 ~ 1 형태의 값으로 정규화 됨.
    result = decode_predictions(model.predict(image), 3)[0] # 2: 상위 2개의 결과 반환

    result_list = []
    for res in result:
        print(res)
        result_list.append({"class": res[1], "confidence": f"{res[2]*100:0.2f} %"})

    return result_list