import logging

import requests

logger = logging.getLogger("App")


def send_image_to_brickognize(filename: str):
    # Send the image to the Brickognize API
    try:
        with open(filename, 'rb') as image_file:
            files = {'query_image': (filename, image_file, 'image/jpeg')}
            response = requests.post(
                'https://api.brickognize.com/predict/',
                files=files,
                headers={'accept': 'application/json'}
            )
            response.raise_for_status()
            json_response = response.json()
            logger.info(f"Image sent to Brickognize API. Response: {json_response}")
            return json_response
    except Exception as e:
        logger.error(f"Error sending image to Brickognize API: {str(e)}")