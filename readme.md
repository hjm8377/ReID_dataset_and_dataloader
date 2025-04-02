<strong>📁 ReID_datasets 디렉토리 구조</strong>
``` yaml
ReID_datasets/
├── images/
│   ├── Night600/
│   │   ├── bounding_box_train/
│   │   └── ...
│   └── NightPerson/
│       ├── Person/
│       │   ├── 0001/
│       │   ├── 0002/
│       │   └── ...
│       └── readme.txt
└── data/
    ├── __init__.py
    └── datasets/
        ├── __init__.py
        ├── bases.py
        ├── dataset_loader.py
        ├── knight.py           # For NightPerson
        ├── night600.py
        └── ...
```
