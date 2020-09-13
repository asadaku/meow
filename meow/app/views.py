import io
import random
import uuid

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from google.cloud import storage
from PIL import Image

from meow.settings import GCLOUD_UNVERIFIED_BUCKET_NAME


def index(request):
    return render(request, 'app/index.html')


@require_http_methods(["GET"])
def get_a_cat(request):
    # For now, pulls a random image from the unverified bucket and displays it
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCLOUD_UNVERIFIED_BUCKET_NAME)
    return JsonResponse({"image_url": random.choice(list(bucket.list_blobs())).public_url})


@require_http_methods(["POST"])
def post_a_cat(request):
    # Convert bytes to image
    img = Image.open(request.FILES['cat_image'].file)

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCLOUD_UNVERIFIED_BUCKET_NAME)
    filename = "kitty_" + str(uuid.uuid1()) + ".JPEG"
    blob = bucket.blob(filename)

    with io.BytesIO() as output:
        # Assumes images fit in memory
        img.save(output, format="JPEG")
        output.seek(0)
        blob.upload_from_file(output)

    return JsonResponse({"status": "ok"})
