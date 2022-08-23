import io
import requests
from PIL import Image as im
import torch
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import BurnPic, BurnInfo, BurnDegree, Result, AddressInfo
from .serializers import BurnInfoSerializer, BurnPicSerializer
from rest_framework.response import Response


# Create your views here.

#화상 종류 고르기
'''
def index(request):
    burntypes = BurnInfo.objects.all() # burn_info에 있는 모든 개체를 불러오겠다
    context = {
        'burntypes' : burntypes,
    }
    
    return #Serializer 생성 후 시리얼라이저 사용하기!
'''
'''
class Index(self, request):
    burntypes = BurnInfo.objects.all()
    context = {
    	'burntypes' : burntypes,
    }
'''

'''
#화상 사진 올리기
def picupload(request):
    if request.method == "POST":
        burnpic = BurnPic()
        burnpic.photo = request.FILES['photo']
        burnpic.save()
    else:
        burnpics = BurnPic.objects.all()
    return render(request, 'picupload.html', {'burnpics':burnpics}) #render는 이 형식들이 표시되는 지금 페이지
'''



#화상 종류 불러오기 #post
@api_view(['GET'])
def burninfo(request):
    qs = BurnInfo.objects.all()
    burn_info = BurnInfoSerializer(qs, many = True)
    return Response(burn_info.data)

'''
@api_view(['POST'])
def burninfo(request):
    # qs = BurnInfo.objects.all()
	# burn_info = BurnInfoSerializer(snippets, many = True)
    if request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(burn_info.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

'''
#화상 사진 불러오기
@api_view(['GET'])
def burnpic(request):
    qs = BurnPic.objects.all()
    burn_pics = BurnPicSerializer(qs, many = True)
    return Response(burn_pics.data)
'''


'''
** 스택오버플로우에서 긁은 ,YOLO-Django / Views.py

from .models import ImageModel
from .forms import ImageUploadForm


class UploadImage(CreateView):
    model = ImageModel
    template_name = 'image/imagemodel_form.html'
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.get('image')
            img_instance = ImageModel(
                image=img
            )
            img_instance.save()

            uploaded_img_qs = ImageModel.objects.filter().last()
            img_bytes = uploaded_img_qs.image.read()
            img = im.open(io.BytesIO(img_bytes))

            # Change this to the correct path
            path_hubconfig = "absolute/path/to/yolov5_code"
            path_weightfile = "absolute/path/to/yolov5s.pt"  # or any custom trained model

            model = torch.hub.load(path_hubconfig, 'custom',
                               path=path_weightfile, source='local')

            results = model(img, size=640)
            results.render()
            for img in results.imgs:
                img_base64 = im.fromarray(img)
                img_base64.save("media/yolo_out/image0.jpg", format="JPEG")

            inference_img = "/media/yolo_out/image0.jpg"

            form = ImageUploadForm()
            context = {
                "form": form,
                "inference_img": inference_img
            }
            return render(request, 'image/imagemodel_form.html', context)

        else:
            form = ImageUploadForm()
        context = {
            "form": form
        }
        return render(request, 'image/imagemodel_form.html', context)
'''