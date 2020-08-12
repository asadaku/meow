from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import numpy as np
from PIL import Image
import io

def index(request):
    return render(request, 'app/index.html')


@require_http_methods(["GET"])
def get_a_cat(request):
    raw = np.random.randn(400,400,3)
    img = Image.fromarray(raw.astype(np.uint8)).convert('RGB')
    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        return HttpResponse(output.getvalue(), content_type="image/jpeg")