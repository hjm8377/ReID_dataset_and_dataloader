import os
import re
import shutil
from tqdm import tqdm

def organize_dataset(root, base_output_path=''):
    """
    KnightReid 데이터셋을 논문 실험 방식에 맞춰
    카메라 페어별 train, query, gallery로 분할.
    """
    if not os.path.isdir(root):
        print(f"오류: '{root}' 디렉토리를 찾을 수 없습니다.")
        return

    person_ids = os.listdir(root)
    img_name_pattern = re.compile(r'cam(\d+)_(\d+).jpg')

    print("데이터셋 정리를 시작합니다...")

    for person_id in tqdm(person_ids, desc="Processing IDs"):

        id_folder = os.path.join(root, person_id)
        if not os.path.isdir(id_folder):
            continue

        images = os.listdir(id_folder)
        cameras_present = set()
        
        # 1. 이 인물이 어떤 카메라에서 촬영되었는지 확인
        for img in images:
            match = img_name_pattern.match(img)
            if match:
                cameras_present.add(int(match.group(1)))

        # 2. 인물이 속하는 카메라 페어 결정
        camera_pairs = []
        if 1 in cameras_present and 2 in cameras_present:
            camera_pairs.append(('NightPerson_C12_MT', [1, 2]))
        if 1 in cameras_present and 3 in cameras_present:
            camera_pairs.append(('NightPerson_C13_MT', [1, 3]))
        if 2 in cameras_present and 3 in cameras_present:
            camera_pairs.append(('NightPerson_C23_MT', [2, 3]))

        if not camera_pairs:
            continue

        # 3. 훈련용 ID인지 테스트용 ID인지 결정 (짝수 -> train, 홀수 -> test)
        is_train_id = int(person_id) % 2 == 0

        # 4. 각 해당 페어에 이미지 복사
        for pair_name, relevant_cams in camera_pairs:
            query_cam = min(relevant_cams)
            gallery_cam = max(relevant_cams)

            for img in images:
                match = img_name_pattern.match(img)
                if match:
                    cam_id = int(match.group(1))
                    
                    # 해당 페어와 관련된 카메라의 이미지만 처리
                    if cam_id not in relevant_cams:
                        continue

                    destination_subfolder = ''
                    if is_train_id:
                        destination_subfolder = 'bounding_box_train'
                    else:  # 테스트 ID인 경우, 쿼리와 갤러리로 분할
                        if cam_id == query_cam:
                            destination_subfolder = 'query'
                        else:
                            destination_subfolder = 'bounding_box_test'
                    
                    # 최종 경로 설정 및 폴더 생성
                    destination_folder = os.path.join(base_output_path, pair_name, destination_subfolder)
                    os.makedirs(destination_folder, exist_ok=True)
                    
                    # 파일 이름 변경 및 복사
                    frames = match.group(2)
                    new_name = f'{person_id}_c{cam_id}_{frames}.jpg'
                    old_path = os.path.join(id_folder, img)
                    new_path = os.path.join(destination_folder, new_name)
                    
                    shutil.copy(old_path, new_path)

    print(f"데이터셋 분할이 완료되었습니다.")


# 인물 ID 폴더들('0001', '0002', 등)이 들어있는 루트 디렉토리
root_dir = ''
output_dir = ''

# main
if __name__ == '__main__':
    organize_dataset(root_dir, output_dir)