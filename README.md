# DiLo Code and Pretrained Models



**Distilling Localization for Self-Supervised Representation Learning**  
Nanxuan Zhao*	Zhirong Wu*	Rynson W.H. Lau	Stephen Lin



## Dataloader

`saliency_dataset.py`  is an example dataloader for adding the DiLo copy-and-paste augmentation. 

The saliency estimation models can be found:

+ GS:    [paper](http://jiansun.org/papers/ECCV12_GeodesicSaliency.pdf) , [code](https://github.com/MCG-NKU/SalBenchmark/tree/master/Code/matlab/RBD)
+ MC:    [paper](https://openaccess.thecvf.com/content_iccv_2013/papers/Jiang_Saliency_Detection_via_2013_ICCV_paper.pdf) , [code](https://github.com/MCG-NKU/SalBenchmark/tree/master/Code/matlab/MC)
+ RBD:     [paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1002.8179&rep=rep1&type=pdf) , [code](https://github.com/MCG-NKU/SalBenchmark/tree/master/Code/matlab/RBD) 
+ BASNet:    [code](https://github.com/NathanUA/BASNet) , [model](https://frontiers.blob.core.windows.net/pretraining/checkpoints/pil_pretrained_models/DiLo/basnet_scratch.pth) pretrained from scratch trained on [DUTS dataset](http://saliencydetection.net/duts/) for 150 epochs.



## Pretrained Models

| Base Model                                          | Saliency Estimation Model | download                                                     |
| --------------------------------------------------- | ------------------------- | ------------------------------------------------------------ |
| [MoCo](https://github.com/facebookresearch/moco)    | RBD                       | [model](https://frontiers.blob.core.windows.net/pretraining/checkpoints/pil_pretrained_models/DiLo/moco_v1_RBD.pth) |
| MoCo                                                | BASNet                    | [model](https://frontiers.blob.core.windows.net/pretraining/checkpoints/pil_pretrained_models/DiLo/moco_v1_BasNet.pth) |
| [MoCo v2](https://github.com/facebookresearch/moco) | RBD                       | [model](https://frontiers.blob.core.windows.net/pretraining/checkpoints/pil_pretrained_models/DiLo/moco_v2_RBD.pth) |
| MoCo v2                                             | BASNet                    | [model](https://frontiers.blob.core.windows.net/pretraining/checkpoints/pil_pretrained_models/DiLo/moco_v2_BasNet.pth) |



## Citation

Please cite our paper if you use DiLo in your research or wish to refer to the results published in the paper.

```
@inproceedings{ZhaoAAAI2021, 
    author = {Nanxuan Zhao and Zhirong Wu and Rynson W.H. Lau and Stephen Lin}, 
    title = {Distilling Localization for Self-Supervised Representation Learning}, 
    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence}, 
    year = {2021} 
}
```



