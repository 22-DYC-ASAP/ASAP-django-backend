from django.db import models


#화상 사진 업로드
class BurnPic(models.Model):
    photo = models.ImageField(null = True, upload_to="images/")
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    

#화상 도수 및 도수별 증세, 치료법
class BurnDegree(models.Model):
    degree=models.IntegerField(null=False)
    description=models.TextField(null=False) #2도화상은 물집이 생겨요, 화상 치료법

#yolo model에서 이미지가 돌려진 후 반환되는 결과
class Result(models.Model):
    burn_degree=models.ForeignKey(BurnDegree, on_delete=models.CASCADE)
    image_file=models.ImageField(blank=True)

#지도의 위도, 경도
class AddressInfo(models.Model):
    latitude=models.FloatField()#위도
    logitude=models.FloatField#경도
    
    
# 화상 종류 선택
class BurnInfo(models.Model):
    burntype = models.CharField(max_length=10)
    content = models.TextField(max_length=800)

'''
    
    def __str__(self): #model class를 view? html?에서 어떻게 나타낼지
        return self.burntype # model을 string 타입으로 반환 / 화상정보까지 나타낼거면 추가적으로 수정해야함
# 화상 종류
class PickType(models.Model): #데이터 타입 중 choice field 있음 # list, radiobutton을 지원
    TYPE_CHOICE = (
    ('열탕화상','열탕화상'), #(Db에 저장되는 형식, 사용자에게 나타나는 형식)
    ('저온화상','저온화상'), #admin에서 picktype 가능
    ('마찰화상','마찰화상'),
    ('접촉화상','접촉화상'),
    ('화학화상','화학화상'),
    ('흡입화상','흡입화상'),
    ('전기화상','전기화상'),
    ('햇빛화상','햇빛화상'),
    ('화염화상','화염화상'),
    ('증기화상','증기화상'),
    )
    
    burntype = models.CharField(max_length=4, choices=TYPE_CHOICE, default ='열탕화상' )

    def __str__(self):
        #어떻게 구현해야 할 지 모르겠음. 사용자가 화상 종류를 고름.
        pass
'''