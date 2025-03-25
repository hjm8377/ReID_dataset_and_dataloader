import glob
import os
import re

import os.path as osp

from .bases import BaseImageDataset


class KnightC1C2(BaseImageDataset):
    """
    KnightC1C2 - cam1을 query, cam2를 gallery로 사용

    Reference:
    Zhang et al. Night Person Re-Identification and a Benchmark.

    Dataset statistics:
    # identities: 937
    # images: 31k
    """

    dataset_dir = 'NightPerson/Person'

    def __init__(self, root='C:/Users/JeongminHeo/JM/ReID/images', verbose=True, **kwargs):
        super(KnightC1C2, self).__init__()
        self.dataset_dir = osp.join(root, self.dataset_dir)
        self._check_before_run()

        train, query, gallery = self._process_dir(self.dataset_dir)

        if verbose:
            print("=> KnightC1C2 loaded")
            self.print_dataset_statistics(train, query, gallery)

        self.train = train
        self.query = query
        self.gallery = gallery

        self.num_train_pids, self.num_train_imgs, self.num_train_cams = self.get_imagedata_info(self.train)
        self.num_query_pids, self.num_query_imgs, self.num_query_cams = self.get_imagedata_info(self.query)
        self.num_gallery_pids, self.num_gallery_imgs, self.num_gallery_cams = self.get_imagedata_info(self.gallery)

    def _check_before_run(self):
        """Check if all files are available before going deeper"""
        if not osp.exists(self.dataset_dir):
            raise RuntimeError("'{}' is not available".format(self.dataset_dir))

    def _process_dir(self, dir_path, relabel=False):
        pattern = re.compile(r'.*cam(\d)_(\d+)\.jpg')

        # 짝수는 train, 홀수는 query & gallery
        train, query, gallery = [], [], []

        img_folders = os.listdir(dir_path) # 0001 ~ 0937

        pid_cam_dict = dict()  # {pid: {camid: [img_paths...]}}

        # pid_cam 사전 생성
        for img_dir in img_folders:
            pid = int(img_dir)
            img_paths = glob.glob(osp.join(dir_path, img_dir, '*.jpg'))

            for img_path in img_paths:
                match = pattern.search(img_path)
                if not match:
                    continue
                camid, _ = map(int, match.groups())

                if pid not in pid_cam_dict:
                    pid_cam_dict[pid] = dict()
                if camid not in pid_cam_dict[pid]:
                    pid_cam_dict[pid][camid] = []
                pid_cam_dict[pid][camid].append(img_path)
            
        for pid, cam_dict in pid_cam_dict.items():
            # if pid is even => train
            if pid % 2 == 0:
                if 1 in cam_dict and 2 in cam_dict:
                    for img_path in cam_dict[1]:
                        train.append((img_path, pid, 1))
                    for img_path in cam_dict[2]:
                        train.append((img_path, pid, 2))
            
            # if pid is odd => query & gallery
            else:
                # cam 1 & cam 2 가 모두 존재할때, 1은 query, 2는 gallery
                if 1 in cam_dict and 2 in cam_dict:
                    for img_path in cam_dict[1]:
                        query.append((img_path, pid, 1))
                    for img_path in cam_dict[2]:
                        gallery.append((img_path, pid, 2))


        return train, query, gallery


class KnightC1C3(BaseImageDataset):
    """
    KnightC1C3 - cam1을 query, cam3를 gallery로 사용

    Reference:
    Zhang et al. Night Person Re-Identification and a Benchmark.

    Dataset statistics:
    # identities: 937
    # images: 31k
    """

    dataset_dir = 'NightPerson/Person'

    def __init__(self, root='C:/Users/JeongminHeo/JM/ReID/images', verbose=True, **kwargs):
        super(KnightC1C3, self).__init__()
        self.dataset_dir = osp.join(root, self.dataset_dir)
        self._check_before_run()

        train, query, gallery = self._process_dir(self.dataset_dir)

        if verbose:
            print("=> KnightC1C3 loaded")
            self.print_dataset_statistics(train, query, gallery)

        self.train = train
        self.query = query
        self.gallery = gallery

        self.num_train_pids, self.num_train_imgs, self.num_train_cams = self.get_imagedata_info(self.train)
        self.num_query_pids, self.num_query_imgs, self.num_query_cams = self.get_imagedata_info(self.query)
        self.num_gallery_pids, self.num_gallery_imgs, self.num_gallery_cams = self.get_imagedata_info(self.gallery)

    def _check_before_run(self):
        """Check if all files are available before going deeper"""
        if not osp.exists(self.dataset_dir):
            raise RuntimeError("'{}' is not available".format(self.dataset_dir))

    def _process_dir(self, dir_path, relabel=False):
        pattern = re.compile(r'.*cam(\d)_(\d+)\.jpg')

        # 짝수는 train, 홀수는 query & gallery
        train, query, gallery = [], [], []

        img_folders = os.listdir(dir_path) # 0001 ~ 0937

        pid_cam_dict = dict()  # {pid: {camid: [img_paths...]}}

        # pid_cam 사전 생성
        for img_dir in img_folders:
            pid = int(img_dir)
            img_paths = glob.glob(osp.join(dir_path, img_dir, '*.jpg'))

            for img_path in img_paths:
                match = pattern.search(img_path)
                if not match:
                    continue
                camid, _ = map(int, match.groups())

                if pid not in pid_cam_dict:
                    pid_cam_dict[pid] = dict()
                if camid not in pid_cam_dict[pid]:
                    pid_cam_dict[pid][camid] = []
                pid_cam_dict[pid][camid].append(img_path)
            
        for pid, cam_dict in pid_cam_dict.items():
            # if pid is even => train
            if pid % 2 == 0:
                if 1 in cam_dict and 3 in cam_dict:
                    for img_path in cam_dict[1]:
                        train.append((img_path, pid, 1))
                    for img_path in cam_dict[3]:
                        train.append((img_path, pid, 3))
            
            # if pid is odd => query & gallery
            else:
                # cam 1 & cam 3 가 모두 존재할때, 1은 query, 3는 gallery
                if 1 in cam_dict and 3 in cam_dict:
                    for img_path in cam_dict[1]:
                        query.append((img_path, pid, 1))
                    for img_path in cam_dict[3]:
                        gallery.append((img_path, pid, 3))


        return train, query, gallery


class KnightC2C3(BaseImageDataset):
    """
    KnightC2C3 - cam2을 query, cam3를 gallery로 사용

    Reference:
    Zhang et al. Night Person Re-Identification and a Benchmark.

    Dataset statistics:
    # identities: 937
    # images: 31k
    """

    dataset_dir = 'NightPerson/Person'

    def __init__(self, root='C:/Users/JeongminHeo/JM/ReID/images', verbose=True, **kwargs):
        super(KnightC2C3, self).__init__()
        self.dataset_dir = osp.join(root, self.dataset_dir)
        self._check_before_run()

        train, query, gallery = self._process_dir(self.dataset_dir)

        if verbose:
            print("=> KnightC2C3 loaded")
            self.print_dataset_statistics(train, query, gallery)

        self.train = train
        self.query = query
        self.gallery = gallery

        self.num_train_pids, self.num_train_imgs, self.num_train_cams = self.get_imagedata_info(self.train)
        self.num_query_pids, self.num_query_imgs, self.num_query_cams = self.get_imagedata_info(self.query)
        self.num_gallery_pids, self.num_gallery_imgs, self.num_gallery_cams = self.get_imagedata_info(self.gallery)

    def _check_before_run(self):
        """Check if all files are available before going deeper"""
        if not osp.exists(self.dataset_dir):
            raise RuntimeError("'{}' is not available".format(self.dataset_dir))

    def _process_dir(self, dir_path, relabel=False):
        pattern = re.compile(r'.*cam(\d)_(\d+)\.jpg')

        # 짝수는 train, 홀수는 query & gallery
        train, query, gallery = [], [], []

        img_folders = os.listdir(dir_path) # 0001 ~ 0937

        pid_cam_dict = dict()  # {pid: {camid: [img_paths...]}}

        # pid_cam 사전 생성
        for img_dir in img_folders:
            pid = int(img_dir)
            img_paths = glob.glob(osp.join(dir_path, img_dir, '*.jpg'))

            for img_path in img_paths:
                match = pattern.search(img_path)
                if not match:
                    continue
                camid, _ = map(int, match.groups())

                if pid not in pid_cam_dict:
                    pid_cam_dict[pid] = dict()
                if camid not in pid_cam_dict[pid]:
                    pid_cam_dict[pid][camid] = []
                pid_cam_dict[pid][camid].append(img_path)
            
        for pid, cam_dict in pid_cam_dict.items():
            # if pid is even => train
            if pid % 2 == 0:
                if 2 in cam_dict and 3 in cam_dict:
                    for img_path in cam_dict[2]:
                        train.append((img_path, pid, 2))
                    for img_path in cam_dict[3]:
                        train.append((img_path, pid, 3))
            
            # if pid is odd => query & gallery
            else:
                # cam 1 & cam 3 가 모두 존재할때, 1은 query, 3는 gallery
                if 2 in cam_dict and 3 in cam_dict:
                    for img_path in cam_dict[2]:
                        query.append((img_path, pid, 2))
                    for img_path in cam_dict[3]:
                        gallery.append((img_path, pid, 3))


        return train, query, gallery

if __name__ == "__main__":
    dataset = KnightC2C3()
