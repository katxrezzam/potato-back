from rest_framework.response import Response
from rest_framework import viewsets
from .models import ImagePredictModel
from .serializer import ImagePredictSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .tensorflow_utils import predict
import uuid
import os


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImagePredictSerializer
    queryset = ImagePredictModel.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        try:
            image = request.data['image']
            if image:
                random_filename = str(uuid.uuid4()) + os.path.splitext(image.name)[-1]
                image.name = random_filename
                ImagePredictModel.objects.create(image=image)
                disease, score = predict(image.name)
                print(disease, score)
                return Response({
                    'disease': disease,
                    'score': score
                })
        except Exception as e:
            print(e)
            return Response({
                'Error': 'Un hubo un error en el servidor'
            })
