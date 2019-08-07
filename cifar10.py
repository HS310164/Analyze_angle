import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import argparse


def opt():
    args = argparse.ArgumentParser()
    args.add_argument('--seed', default=123456789, type=int, help='Random seed')
    args.add_argument('--save_image', action='store_true', help='If true, save images')
    args.add_argument('--num_image', default=2, type=int, help='The number of processing images')
    arguments = args.parse_args()
    return arguments


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def main(args):
    label_names = unpickle("cifar-10-batches-py/batches.meta")[b"label_names"]
    d = unpickle("cifar-10-batches-py/data_batch_1")
    data = d[b"data"]
    labels = np.array(d[b"labels"])
    print(label_names)
    print(args)

    targets = np.where(labels == 5)[0]
    np.random.seed(args.seed)
    np.random.shuffle(targets)
    for pos, idx in enumerate(targets[:2]):
        print("image{}".format(pos + 1))
        plt.subplot(1, 2, pos+1)
        img = data[idx]
        img = img.reshape(3, 32, 32).transpose(1, 2, 0)
        if args.save_image:
            save_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imwrite(save_img, 'img{}.jpg'.format(pos+1))
        plt.imshow(img)
        plt.axis('off')
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        sum_sin = 0
        sum_cos = 0
        data_size = hsv[:, :, 0:1].size
        for i in hsv[:, :, 0:1].reshape(-1):
            # OpenCVではデータを8bitに収めるため，0<=H<=180になっているため2倍
            sum_sin += math.sin(math.radians(i * 2))
            sum_cos += math.cos(math.radians(i * 2))
        Sin = sum_sin
        Cos = sum_cos
        if Cos < 0:
            cent = math.atan(Sin / Cos) + np.pi
        elif Sin < 0:
            cent = math.atan(Sin / Cos) + 2 * np.pi
        else:
            cent = math.atan(Sin / Cos)
        R = math.sqrt(Cos ** 2 + Sin ** 2) / data_size

        print("平均方向(rad)：", cent)
        print("平均合成ベクトル長：", R)
        print("円周分散：", 1 - R)
        print("円周標準偏差：", -2 * (np.log(1 - R)))
    plt.show()


if __name__ == '__main__':
    args = opt()
    main(args)
