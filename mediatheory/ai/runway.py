import base64
import os
import time

import requests
from runwayml import RunwayML

from mediatheory.decorator import staticwrite
from mediatheory.log import logging


class Runway:
    client = RunwayML(api_key=os.environ["RUNWAYML_API_SECRET"])

    @staticwrite
    def image_to_video(img, prompt, model, ratio, duration):
        if not img.startswith("http"):
            with open(img, "rb") as f:
                encoded = base64.b64encode(f.read())
                string = encoded.decode("utf-8")
                img = f"data:image/jpg;base64,{string}"

        submission = Runway.client.image_to_video.create(
            model=model,
            prompt_image=img,
            prompt_text=prompt,
            duration=duration,
            ratio=ratio,
        )

        logging.info(submission.id)

        while True:
            time.sleep(5)
            task = Runway.client.tasks.retrieve(submission.id)
            if task.status in ["RUNNING", "PENDING"]:
                time.sleep(5)
            elif task.status in ["SUCCEEDED"]:
                logging.info(task)
                return Runway.download_result(task.output[0], task.id)
            else:
                logging.info(task)
                return task

    @staticwrite
    def download_result(url, task_id):
        response = requests.get(url, stream=True)
        out = f"./media/out/runway/{task_id}.mp4"

        with open(out, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        return out
