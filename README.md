# Analyze CIFAR-10's angle data

There are programs that analyse CIFAR-10's angle data

# How to use
## Download CIFAR-10 for python
Run the following script to download the data

```bash
bash download_cifar10.sh
```

## Analyze angle data
Run the following script to analyze angle data
```bash
python cifar10.py
```

### Options

- --seed : Random Seed (Default: 123456789)
- --num_image : The number of processing images (Default: 2)
- --save_image : If this option is true, save images (Default: false)
- --vizualize : If this option is true, visualize images (Default: false)

If you want to set the seed value to 0, 
the number of images to 3, not save images, 
and not visualize images, 
run the following script
```bash
python cifar10.py --seed 0 --num_image 3
```

If you want to set the seed value to 13, 
the number of images to 5, save images, and visualize image,
run the following script
```bash
python cifar10.py --seed 13 --num_image 5 --save_image --visualize
```

## Extra code
`calc_cor.py` calculates the correlation coefficient of cherry blossoms in Tokyo and Sapporo.

