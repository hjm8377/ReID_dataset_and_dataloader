## ReID 데이터 셋 정리 및 데이터 로더더

### Daytime ReID datasets
* [Market1501](https://www.kaggle.com/datasets/pengcw1/market-1501) - [reference](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zheng_Scalable_Person_Re-Identification_ICCV_2015_paper.pdf)

* DukeMTMC - retracted - [reference](https://arxiv.org/pdf/1609.01775)

* MSMT17 - can be requested at [here](http://www.pkuvmc.com/dataset.html) - [reference](https://openaccess.thecvf.com/content_cvpr_2018/papers/Wei_Person_Transfer_GAN_CVPR_2018_paper.pdf)



### NightTime ReID datasets
* [KnightReid](https://github.com/Alexadlu/IDF) - [reference](https://ieeexplore.ieee.org/document/8766119)

* [RGBNT201](https://drive.google.com/drive/folders/1EscBadX-wMAT56_It5lXY-S3-b5nK1wH?usp=sharing) -[reference](https://ojs.aaai.org/index.php/AAAI/article/view/16467)

* [Night600](https://github.com/Alexadlu/IDF) - [reference](https://ieeexplore.ieee.org/document/10098634)

* [NightReID](https://github.com/msm8976/NightReID) - [reference](https://ojs.aaai.org/index.php/AAAI/article/view/33142)

</br>

### split_knightreid.py
Knightreid의 원본 폴더가 ID 별로 구분되어있어, 논문에서 언급하는 cam 세팅을 포함해 train, query, gallery로 분할.

```yaml
Origin structure of Knightreid

NightPerson
├── 001/
├── 002/
├── 003/   
├── 004/
└── ...
```

<!-- <strong>📁 ReID_datasets 디렉토리 구조</strong>
``` yaml
ReID_datasets/
└── data/
    ├── __init__.py
    ├── datasets/
    │   ├── __init__.py
    │   ├── bases.py
    │   ├── dataset_loader.py
    │   ├── knight.py           # For NightPerson
    │   ├── night600.py
    │   └── ...
    ├── market1501/
    │   ├── bounding_box_train/
    │   └── ...
    ├── Night600/
    │   ├── bounding_box_train/
    │   └── ...
    ├── NightPerson/
    │   ├── Person/
    │   │   ├── 0001/
    │   │   ├── 0002/
    │   │   └── ...
    │   └── readme.txt
    ...
``` -->
