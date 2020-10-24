# Script for thesis presentation


## Slide 1 : Introduction


Hi, I'm Mattia and I'm going to present my thesis titled Optimization and applications of Deep learning algortithms for Super Resolution in MRI. The objectives of this work is to test two pre-trained Neural Networks and their generalization abilities on a dataset of NMR images of the brains, which are never used during the training phase.

## Slide 2 : Super Resolution

SR is divided into two main groups of tech, the hardware SR microscopy, that requires a complex laboratory setup and "software" SR, that is the focus of this work and which aim is to ehance the spatial resolution of an image to improve further analysis. A standard procedure consists in donwsampling a known High Resolution image in order to obtain its Low Resolution counterpart, and feed DL models with low res images trying to reconstruct the high res version.

## Slide 3 : DL

Neural Networks are essentially a series of non-linear multi parametric functions and during the training phase the parameters of those functions are tuned in order to create a map between input an desired output.

Normally in a supervised environment the training happens by showing the network many couples of input and desired output.

Commonly neural network are used to map a large feature space (for exampe an image) into a smaller one such as classification labels, but in super-resolution we start from an image and we end up with a more resoluted one.

## Slide 4 : Libraries

For the purposes of this work I implemented two libraries for Deep Learning Applications, the first one is called NumPyNet, is written in pure python and tries to overcome the common "black box" idea of Neural Network using simple and readable code. I wrote it to rapidly test more complex code, experiment with DL models and Learn a variety of algorithms to develop the second library: Byron, which, on the other hand, is written in pure C++, optimized for image processing, one of the most common task in the Biomedical field
Differently from most famous frameworks such as tensorflow, pytorch and darknet which focus on GPU usage, Byron it's written keeping CPU effiency in mind, to target all the research fields excluded from DL analysis by lack of powerful GPU.

## Slide 5 : Image quality

in order to evaluate the quality of reconstructions, while the human eye is a good qualitative evaluator for Image quality, we can also define two different quantitative metrics:

* **PSNR**: the Peak Signal to Noise Ratio, which is most commonly used to measure the quality of recontructions of a lossy compression.
*  **SSIM**: The Structural SIMilarity index, used to measure the similarity between two images considering also luminance, contrast and dependencies between spatially close pixels.

## Slide 6 : Models:

To test super-resolution I implemented two models in Byron:
the first one is called EDSR or Enhanced Deep Super Resolution and it has more the 40 million parameters while the second one is called WDSR and it has about 3 million trainable weights, which make it 10 times faster than EDSR.
They both are trained on 3 channel Natural Images of landscapes, animals and other subjects but never saw anything like a gray-scale picture of a brain. In this sense, I'm applying the knowledge of shapes and textures previously acquired by the networks to solve a different problem: this procedure is called Transfer Learning.

## Slide 7 : Dataset

The test dataset is publicy available and comes from the NAMIC composed by 5 patient weighted T1 and T2: those are the originals HR images.
They have been blurred with a gaussian kernel and then downsampled with two different scale factors, 2 and 4, using a bicubic downsampling. The gaussian blurring is done to better resemble a LR acquisition, as if the images where directly acquired in LR instead of coming from a downsampling.

The LR slices are then re-upsampled using 20 different angles of rotations by the models and the bicubic algorithm, in this way is possible to compare the reconstructions with the originals images by means of PSNR and SSIM.

## Results 1 : Upsample Comparisons

I divided the results on T1 and T2 samples: in the graphs I show the two scores divided by channels (Red, Green and Blue) for EDSR and Bicubic in yellow, averged for all patient and angles: we can see that the three channels performs very differently and the BLUE one performs consistently better that the bicubic. Though, on the other hand, on t2 weighted samples the results for SR and Bicubic are comparable only on the central slices, where is contained the most relevant information.

## Results 2: WDSR

For the WDSR instead we notice much less variance between RGB performances and at the same time both SSIM and PSNR are consistently better if compared with the bicubic algorithm.

## Results 3 : Error Localizations

If we visualize the images of pixel-by-pixel absolute differences between reconstructions and originals, we can see how the higher values are located around the scalps of subjects. Another thing we notice is the background different from zero: this can be explained if wwe consider that the models are not trained on such uniform backgrounds. Indeed by plotting the histograms of those differences:

## Results 4 : histograms

we can clearly distinguish between two components: an heavy background and the subject for both reconstructions method. In both cases, the distributions show that the pixel values are overestimated for both algorithm.

## Results 5 : BET

I order to remove the background component that can spoil the results, I used a Brain Extraction tool which is a standard in MRI analysis: this tool allow the extraction of binary mask used to cut irrelvant information from the slices as shown in the figure. I opted for two approaches:

## Results 6 : IoU

In the first approach I extracted 3 different masks from originals, reconstructions and compare them directly by using the Intersection Over Union Score, which is the ratio between the area of overlap and the area of union. In this way I could evaluate how well a standard software in MRI analysis works on SR reconstructions.
In any cases the IoU shows high similarity between masks, but the WDSR seems to be slghtly outperformed by the bicubic mask, which may indicate that BET couldn't catch all the relevant informations.

## Results 7 : Mask Comparisons:

In the second approach I applied the same mask extracted from the originals to all the reconstructions in order evaluate only the relevant ppixels: in the graphs i show a pre and post Brain extraction evaluation: indeed we see that three channels are much more consistent between each othe and the Super Resolutios shows sliglthly better results if compared with the bicubic.

## Conclusions and future Develop

Just read slides.
