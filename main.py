from transformer.asteroids_transformer import AsteroidsTransformer
from client.storage_client import GCSClient
from utils.logger import logger
from utils.settings import settings

def main(request):
    request_json = request.get_json(silent=True)
    file_path = request_json.get("file_path")

    if not file_path:
        return {"error": "file_path is required"}, 400

    try:
        gcs = GCSClient()
        raw_data = gcs.download(file_path)

        transformer = AsteroidsTransformer()
        df = transformer.transform_asteroids_data(raw_data)

        output_path = settings.OUTPUT_PATH
        if not output_path:
            logger.info("There is no path")
            return {"error": "filepath does not exist"}
        logger.info("Uploading transform data to GCS")
        gcs.upload(df, output_path)
        logger.info("Uploaded successfully")

        return {"message": "Transform complete", "file_path": output_path}

    except Exception as e:
        return {"error": str(e)}, 500
