__version__ = "1.1"

from meshroom.core import desc


class ImageProcessing(desc.CommandLineNode):
    commandLine = 'aliceVision_utils_imageProcessing {allParams}'
    size = desc.DynamicNodeSize('input')
    # parallelization = desc.Parallelization(blockSize=40)
    # commandLineRange = '--rangeStart {rangeStart} --rangeSize {rangeBlockSize}'

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='SfMData file.',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='extension',
            label='File Extension',
            description='File Extension.',
            value='',
            values=['', 'exr', 'jpg', 'tiff', 'png'],
            exclusive=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='reconstructedViewsOnly',
            label='Only Reconstructed Views',
            description='Process Only Reconstructed Views',
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='exposureCompensation',
            label='Exposure Compensation',
            description='Exposure Compensation',
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name='downscale',
            label='Downscale',
            description='Downscale.',
            value=1.0,
            range=(0.0, 1.0, 0.01),
            uid=[0],
        ),
        desc.FloatParam(
            name='contrast',
            label='Contrast',
            description='Contrast.',
            value=1.0,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.IntParam(
            name='medianFilter',
            label='Median Filter',
            description='Median Filter.',
            value=0,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='fillHoles',
            label='Fill holes',
            description='Fill holes.',
            value=False,
            uid=[0],
        ),
        desc.IntParam(
            name='sharpenWidth',
            label='Sharpen Width',
            description='Sharpen Width.',
            value=1,
            range=(1, 9, 2),
            uid=[0],
        ),
        desc.FloatParam(
            name='sharpenContrast',
            label='Sharpen Contrast',
            description='Sharpen Contrast.',
            value=1.0,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='sharpenThreshold',
            label='Sharpen Threshold',
            description='Sharpen Threshold.',
            value=0.0,
            range=(0.0, 1.0, 0.01),
            uid=[0],
        ),
        desc.BoolParam(
            name='bilateralFilter',
            label='Bilateral Filter',
            description='Bilateral Filter.',
            value=False,
            uid=[0],
        ),
        desc.IntParam(
            name='BilateralFilterDistance',
            label='Bilateral Filter Distance',
            description='Diameter of each pixel neighborhood that is used during bilateral filtering.\nCould be very slow for large filters, so it is recommended to use 5.',
            value=0,
            range=(0, 9, 1),
            uid=[0],
        ),
        desc.FloatParam(
            name='BilateralFilterSigmaSpace',
            label='Bilateral Filter Sigma Space',
            description='Bilateral Filter sigma in the coordinate space.',
            value=0.0,
            range=(0.0, 150.0, 0.01),
            uid=[0],
        ),
        desc.FloatParam(
            name='BilateralFilterSigmaColor',
            label='Bilateral Filter Sigma Color Space',
            description='Bilateral Filter sigma in the color space.',
            value=0.0,
            range=(0.0, 150.0, 0.01),
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='verbosity level (fatal, error, warning, info, debug, trace).',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        )
    ]

    outputs = [
        desc.File(
            name='outSfMData',
            label='Output sfmData',
            description='Output sfmData.',
            value=desc.Node.internalFolder + 'sfmData.abc',
            uid=[],
        ),
    ]
