import argparse

from mediatheory.ai.runway import Runway


def create_parser():
    parser = argparse.ArgumentParser(
        description="Process a path with an optional renderer."
    )

    parser.add_argument(
        "img",
        type=str,
        help="https URL or local path of the input image",
    )

    parser.add_argument(
        "--prompt",
        type=str,
        default="",
        help="Prompt for the generative AI model"
    )

    parser.add_argument(
        "--model",
        type=str,
        choices=["gen3a_turbo"],
        default="gen3a_turbo"
    )

    parser.add_argument(
        "--ratio",
        type=str,
        choices=["1280:768", "768:1280"],
        default="1280:768"
    )

    parser.add_argument(
        "--duration",
        type=str,
        choices=["5", "10"],
        default="5"
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()


    Runway.image_to_video(
        img=args.img,
        prompt=args.prompt,
        model=args.model,
        ratio=args.ratio,
        duration=args.duration,
    )
