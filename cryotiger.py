import argparse
from utils import prepareData, interpolate, generateOutputMRCTiltSeries, cryotiger

def cryoTygerMain():
    parser = argparse.ArgumentParser(
        description="CryoTyger: a deep learning-based frame interpolation to generate intermediate tilt images"
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Tilt series to be interpolated. Usually a mrc file."
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Output interpolated tilt series. Usually a mrc file."
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="This is the model to be used for interpolating the tilt series"
    )
    parser.add_argument(
        "--interpolations",
        type=int,
        required=True,
        help="Number of interpolated tilt images between two consecutive tilts."
    )

    args = parser.parse_args()

    tsPath = args.input
    outPath = args.output
    modelPath = args.model
    timesToInterpolate = args.interpolations

    print("Executing cryoTyger with the next parameters:")
    print(f"  --input: {tsPath}")
    print(f"  --output: {outPath}")
    print(f"  --model: {modelPath}")
    print(f"  --interpolations: {timesToInterpolate}")

    cryotiger(tsPath, outPath, modelPath, timesToInterpolate)


if __name__ == "__main__":
    cryoTygerMain()
