from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views
from .models import *
from .serializers import *



def home(request):
    return render(request, 'home.html')    


@api_view(['GET'])
def Test_api(request):
    data = TestApi.objects.all()
    serializer = TestApiSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def VideoBannerViewSet_api(request):
    queryset = VideoBanner.objects.all()
    serializer = VideoBannerSerializer(queryset, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def AboutContent_api(request):
    queryset = AboutContent.objects.all()
    serializer = AboutContentSerializer(queryset, many=True)
    return Response(serializer.data)   



# @api_view(['GET'])
# def StatCategory_api(request):
#     queryset = StatCategory.objects.all()
#     serializer = StatCategorySerializer(queryset, many=True)
#     return Response(serializer.data)   



@api_view(['GET'])
def Stat_api(request):
    queryset = Stat.objects.all()
    serializer = StatSerializer(queryset, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def Client_api(request):
    queryset = Client1.objects.all()
    serializer = ClientSerializer(queryset, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def Client2_api(request):
    queryset = Client2.objects.all()
    serializer = Client2Serializer(queryset, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def Testimonial_api(request):
    queryset = Testimonial.objects.all()
    serializer = TestimonialSerializer(queryset, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def ServiceCarousel_api(request):
    queryset = ServiceCarousel.objects.all()
    serializer = ServiceCarouselSerializer(queryset, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def IndustryWeServe_api(request):
    queryset = IndustryWeServe.objects.all()
    serializer = IndustryWeServeSerializer(queryset, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def ApproachStep_api(request):
    queryset = ApproachStep.objects.all()
    serializer = ApproachStepSerializer(queryset, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def Certification_api(request):
    queryset = Certification.objects.all()
    serializer = CertificationSerializer(queryset, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def AboutUsPage_api(request):
    data = AboutUsPage.objects.all()
    serializer = AboutUsPageSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def AboutUsMeta_api(request):
    data = AboutUsMeta.objects.all()
    serializer = AboutUsMetaSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def WhoWeAre_api(request):
    data = WhoWeAre.objects.all()
    serializer = WhoWeAreSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def OurMission_api(request):
    data = OurMission.objects.all()
    serializer = OurMissionSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def WeAreGlobal_api(request):
    data = WeAreGlobal.objects.all()
    serializer = WeAreGlobalSerializer(data, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def WhyUs_api(request):
    data = WhyUs.objects.all()
    serializer = WhyUsSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def Accredition_api(request):
    data = Accredition.objects.all()
    serializer = AccreditionSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def ImplementOfIP_api(request):
    data = ImplementOfIP.objects.all()
    serializer = ImplementOfIPSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def QualityPolicy_api(request):
    data = QualityPolicy.objects.all()
    serializer = QualityPolicySerializer(data, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def ImpartialityPolicy_api(request):
    data = ImpartialityPolicy.objects.all()
    serializer = ImpartialityPolicySerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def SuspendedClients_api(request):
    data = SuspendedClients.objects.all()
    serializer = SuspendedClientsSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def SuspendedClientsPage_api(request):
    data = SuspendedClientsPage.objects.all()
    serializer = SuspendedClientsPageSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SuspendedClientsMeta_api(request):
    data = SuspendedClientsMeta.objects.all()
    serializer = SuspendedClientsMetaSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def AppealHandling_api(request):
    data = AppealHandling.objects.all()
    serializer = AppealHandlingSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def AppealHandlingPage_api(request):
    data = AppealHandlingPage.objects.all()
    serializer = AppealHandlingPageSerializer(data, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def AHList_api(request):
    data = AHList.objects.all()
    serializer = AHListSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def ComplainHandlingPageSerializer_api(request):
    data = ComplainHandlingPage.objects.all()
    serializer = ComplainHandlingPageSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def ComplainHandlingMeta_api(request):
    data = ComplainHandlingMeta.objects.all()
    serializer = ComplainHandlingMetaSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def GrievancesPage_api(request):
    data = GrievancesPage.objects.all()
    serializer = GrievancesPageSerializer(data, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def GrievancesList_api(request):
    data = GrievancesList.objects.all()
    serializer = GrievancesListSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GrievancesMeta_api(request):
    data = GrievancesMeta.objects.all()
    serializer = GrievancesMetaSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def CerificationProcessImg_api(request):
    data = CerificationProcessImg.objects.all()
    serializer = CertificationImgSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GrantorReuse_api(request):
    data = GrantOrRefuse.objects.all()
    serializer = GrantOrRefuseSerializer(data, many=True)
    return Response(serializer.data)  
 



@api_view(['GET'])
def MaintainCertification_api(request):
    data = MaintainCertification.objects.all()
    serializer = MaintainCertificationSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def DetailsForIssuing_api(request):
    data = DetailsForIssuing.objects.all()
    serializer = DetailsForIssuingSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def WithdrawOfCertification_api(request):
    data = WithdrawOfCertification.objects.all()
    serializer = WithdrawOfCertificationSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SuspensionOfCertification_api(request):
    data = SuspensionOfCertification.objects.all()
    serializer = SuspensionOfCertificationSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def RestoringOfCertification_api(request):
    data = RestoringOfCertification.objects.all()
    serializer = RestoringOfCertificationSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def ExpandingOrReducing_api(request):
    data = ExpandingOrReducing.objects.all()
    serializer = ExpandingOrReducingSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def CertificationProcessPage_api(request):
    data = CertificationProcessPage.objects.all()
    serializer = CertificationProcessPageSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def CertificationMeta_api(request):
    data = CertificationMeta.objects.all()
    serializer = CertificationMetaSerializer(data, many=True)
    return Response(serializer.data)   



# service page 


#Use this one View to get Nested Data 
@api_view(['GET'])
def GrcSubPage_api(request):
    data = GrcSubPage.objects.all()
    serializer = GrcSubPageSerializer(data, many=True)
    return Response(serializer.data)   



#Views for all API[not necessary]
@api_view(['GET'])
def GrcMetaTags_api(request):
    data = GrcMetaTags.objects.all()
    serializer = GrcMetaTagsSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def SecOne_api(request):
    data = GrcSecOne.objects.all()
    serializer = GrcSecOneSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SecOneList_api(request):
    data = GrcSecOneList.objects.all()
    serializer =  GrcSecOneListSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SecTwo_api(request):
    data = GrcSecTwo.objects.all()
    serializer = GrcSecTwoSerializer(data, many=True)
    return Response(serializer.data)   




@api_view(['GET'])
def SecThree_api(request):
    data =  GrcSecThree.objects.all()
    serializer =  GrcSecThreeSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SecFour_api(request):
    data = GrcSecFour.objects.all()
    serializer = GrcSecFourSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SecFive_api(request):
    data = GrcSecFive.objects.all()
    serializer = GrcSecFiveSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SecSix_api(request):
    data = GrcSecSix.objects.all()
    serializer = GrcSecSixSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def SecSeven_api(request):
    data = GrcSecSeven.objects.all()
    serializer = GrcSecSevenSerializer(data, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def SecEight_api(request):
    data = GrcSecEight.objects.all()
    serializer = GrcSecEightSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def GrcSubPage_api(request):
    data = GrcSubPage.objects.all()
    serializer = GrcSubPageSerializer(data, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def ManagementTrnSubPage_api(request):
    data = ManagementTrnSubPage.objects.all()
    serializer = ManagementTrnSubPageSerializer(data, many=True)
    return Response(serializer.data)


 
@api_view(['GET'])
def ProfessionalTrnSubPage_api(request):
    data = ProfessionalTrnSubPage.objects.all()
    serializer = ProfessionalTrnSubPageSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AuditSubPage_api(request):
    data = AuditSubPage.objects.all()
    serializer = AuditSubPageSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def StcSubPage_api(request):
    data = StcSubPage.objects.all()
    serializer = StcSubPageSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GrcMainPage_api(request):
    data = GrcMainPage.objects.all()
    serializer = GrcMainPageSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AuditMainPage_api(request):
    data = AuditMainPage.objects.all()
    serializer = AuditMainPageSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TrnMainPage_api(request):
    data = TrnMainPage.objects.all()
    serializer = TrnMainPageSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ContactDetail_api(request):
    data = ContactDetail.objects.all()
    serializer = ContactDetailSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def MstMainPage_api(request):
    data = MstMainPage.objects.all()
    serializer = MstMainPageSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PtrnMainPage_api(request):
    data = PtrnMainPage.objects.all()
    serializer = PtrnMainPageSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def StcMainPage_api(request):
    data = StcMainPage.objects.all()
    serializer = StcMainPageSerializer(data, many=True)
    return Response(serializer.data)


# Post Method
@api_view(['GET','POST'])
def ContactForm_api(request):
    if request.method == "GET":
        formdata = ContactForm.objects.all()
        serializer = ContactFormSerializer(formdata, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# Post Method
@api_view(['GET','POST'])
def CareerForm_api(request):
    if request.method == "GET":
        formdata = CareerForm.objects.all()
        serializer = CareerFormSerializer(formdata, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CareerFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET'])
def CareerPagePage_api(request):
    data = CareerPagePage.objects.all()
    serializer = CareerPagePageSerializer(data, many=True)
    return Response(serializer.data)
 
 
@api_view(['GET'])
def PrivacyPolicyPage_api(request):
    data = PrivacyPolicyPage.objects.all()
    serializer = PrivacyPolicySubPageSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Blog_api(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BlogCatg_api(request):
    blogctg = BlogCtg.objects.all()
    serializer = BlogCtgSerializer(blogctg, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Blog_detail_api(request, id):
    blog = Blog.objects.get(id=id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(['GET','POST'])
def CustomerFeedbackForm_api(request):
    if request.method == "GET":
        formdata = CustomerFeedbackForm.objects.all()
        serializer = CustomerFeedbackFormSerializer(formdata, many=True)
        return Response(serializer.data)
 
    elif request.method == "POST":
        serializer = CustomerFeedbackFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def CmgSubPage_api(request):
    data = CmgSubPage.objects.all()
    serializer = CmgSubPageSerializer(data, many=True)
    return Response(serializer.data)  


@api_view(['GET'])
def Nav_api(request):
    blogs = Nav.objects.all()
    serializer = NavSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def NavCatg_api(request):
    blogctg = NavCtg.objects.all()
    serializer = NavCtgSerializer(blogctg, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def Search_api(request):
    search = Search.objects.all()
    serializer = SearchSerializer(search, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def GrcOffering_api(request):
    grc = GrcOffering.objects.all()
    serializer = GrcOfferingSerializer(grc, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GrcOfferingCtg_api(request):
    grcctg = GrcOfferingCtg.objects.all()
    serializer = GrcOfferingCtgSerializer(grcctg, many=True)
    return Response(serializer.data)
