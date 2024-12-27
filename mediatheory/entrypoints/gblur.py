import argparse

from mediatheory.ffmpeg import FFmpeg


def create_parser():
    parser = argparse.ArgumentParser(
        description="Process a path with an optional renderer."
    )

    parser.add_argument("path", type=str, help="The path to process")
    parser.add_argument("sigma", type=str, default="5")

    parser.add_argument(
        "--renderer",
        "-r",
        type=str,
        default="ffmpeg",
        help="Specify the renderer to use (default: %(default)s)",
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.renderer == "ffmpeg":
        FFmpeg.gblur(args.path, args.sigma)


if __name__ == "__main__":
    main()
