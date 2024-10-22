from rest_framework.serializers import ModelSerializer
from .models import *

from rest_framework import serializers

class TestApiSerializer(ModelSerializer):
    class Meta:
        model = TestApi
        fields = '__all__'



# home page

class VideoBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBanner
        fields = '__all__'

class AboutContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutContent
        fields = '__all__'



# class StatCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StatCategory
#         fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client1
        fields = '__all__'


class Client2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client2
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class ServiceCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCarousel
        fields = '__all__'



class IndustryWeServeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryWeServeList
        fields = '__all__'


class IndustryWeServeSerializer(serializers.ModelSerializer):
    industry_lists = IndustryWeServeListSerializer(many=True, read_only=True)

    class Meta:
        model = IndustryWeServe
        fields = '__all__'

class ApproachStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApproachStep
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'


# home page ends


# About us page ________________________________ Serializers starts here _________________________#

class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = '__all__'


class AboutUsMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsMeta
        fields = '__all__'


class WWRListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WWRList
        fields = '__all__'

class WhoWeAreSerializer(serializers.ModelSerializer):
    wwr_list = WWRListSerializer(many=True, read_only=True)

    class Meta:
        model = WhoWeAre
        fields = '__all__'

class OMListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OMList
        fields = '__all__'

class OurMissionSerializer(serializers.ModelSerializer):
    om_list = OMListSerializer(many=True, read_only=True)

    class Meta:
        model = OurMission
        fields = '__all__'

class WeAreGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeAreGlobal
        fields = '__all__'

class WUListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WUList
        fields = '__all__'

class WhyUsSerializer(serializers.ModelSerializer):
    wu_list = WUListSerializer(many=True, read_only=True)

    class Meta:
        model = WhyUs
        fields = '__all__'

class AccreditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accredition
        fields = '__all__'

class IOIPListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOIPList
        fields = '__all__'

class ImplementOfIPSerializer(serializers.ModelSerializer):
    ioip_list = IOIPListSerializer(many=True, read_only=True)

    class Meta:
        model = ImplementOfIP
        fields = '__all__'

class QualityPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityPolicy
        fields = '__all__'

class ImpartialityPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpartialityPolicy
        fields = '__all__'

# About us page ________________________________ Serializers Ends here _________________________#


# Resource page ________________________________ Serializers starts here _________________________#
class SuspendedClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspendedClients
        fields = '__all__'

class SuspendedClientsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspendedClientsPage
        fields = '__all__'

class SuspendedClientsMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspendedClientsMeta
        fields = '__all__'


class AHListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AHList
        fields = '__all__'

class AppealHandlingSerializer(serializers.ModelSerializer):
    ah_list = AHListSerializer(many=True, read_only=True)

    class Meta:
        model = AppealHandling
        fields = '__all__'

class AppealHandlingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppealHandlingPage
        fields = '__all__'

class AHListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AHList
        fields = '__all__'


class ComplainHandlingMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplainHandlingMeta
        fields = '__all__'


class CHListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CHList
        fields = '__all__'

class ComplainHandlingPageSerializer(serializers.ModelSerializer):
    ch_list = CHListSerializer(many=True, read_only=True)

    class Meta:
        model = ComplainHandlingPage
        fields = '__all__'

class GrievancesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrievancesList
        fields = '__all__'

class GrievancesPageSerializer(serializers.ModelSerializer):
    grievances_list = GrievancesListSerializer(many=True, read_only=True)

    class Meta:
        model = GrievancesPage
        fields = '__all__'


class GrievancesMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrievancesMeta
        fields = '__all__'


# Resource page ________________________________ Serializers Ends here _________________________#


# Resource - Certification page ________________________________ Serializers starts here _________________________#

class CertificationImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CerificationProcessImg
        fields = '__all__'
        
class GOrRListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOrRList
        fields = '__all__'

class GrantOrRefuseSerializer(serializers.ModelSerializer):
    gor_list = GOrRListSerializer(many=True, read_only=True)

    class Meta:
        model = GrantOrRefuse
        fields = '__all__'

class MCListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCList
        fields = '__all__'

class MaintainCertificationSerializer(serializers.ModelSerializer):
    mc_list = MCListSerializer(many=True, read_only=True)

    class Meta:
        model = MaintainCertification
        fields = '__all__'

class DFIListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DFIList
        fields = '__all__'

class DetailsForIssuingSerializer(serializers.ModelSerializer):
    dfi_list = DFIListSerializer(many=True, read_only=True)

    class Meta:
        model = DetailsForIssuing
        fields = '__all__'

class WOCListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WOCList
        fields = '__all__'

class WithdrawOfCertificationSerializer(serializers.ModelSerializer):
    woc_list = WOCListSerializer(many=True, read_only=True)

    class Meta:
        model = WithdrawOfCertification
        fields = '__all__'

class SOCListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOCList
        fields = '__all__'

class SuspensionOfCertificationSerializer(serializers.ModelSerializer):
    soc_list = SOCListSerializer(many=True, read_only=True)

    class Meta:
        model = SuspensionOfCertification
        fields = '__all__'

class ROCListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ROCList
        fields = '__all__'

class RestoringOfCertificationSerializer(serializers.ModelSerializer):
    roc_list = ROCListSerializer(many=True, read_only=True)

    class Meta:
        model = RestoringOfCertification
        fields = '__all__'

class EORListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EORList
        fields = '__all__'

class ExpandingOrReducingSerializer(serializers.ModelSerializer):
    eor_list = EORListSerializer(many=True, read_only=True)

    class Meta:
        model = ExpandingOrReducing
        fields = '__all__'

class CertificationProcessPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationProcessPage
        fields = '__all__'


class CertificationMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationMeta
        fields = '__all__'

        
# Resource - Certification page ________________________________ Serializers Ends here _________________________#


# service page serializer


class GrcSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecOneList
        fields = '__all__'

class GrcSecOneSerializer(serializers.ModelSerializer):
    grc_sec_one_list = GrcSecOneListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcSecOne
        fields = '__all__'


class GrcSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecTwoList
        fields = '__all__'

class GrcSecTwoSerializer(serializers.ModelSerializer):
    grc_sec_two_list = GrcSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcSecTwo
        fields = '__all__'


class GrcSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecThreeList
        fields = '__all__'

class GrcSecThreeSerializer(serializers.ModelSerializer):
    grc_sec_three_list = GrcSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcSecThree
        fields = '__all__'


class GrcSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecFourList
        fields = '__all__'

class GrcSecFourSerializer(serializers.ModelSerializer):
    grc_sec_four_list = GrcSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcSecFour
        fields = '__all__'



class GrcSecFiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecFive
        fields = '__all__'


class GrcSecSixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecSixList
        fields = '__all__'


class GrcSecSixCategorySerializer(serializers.ModelSerializer):
    grc_sec_six_list = GrcSecSixListSerializer(many=True, read_only=True)
 
    class Meta:
        model = GrcSecSixCategory
        fields = ['id', 'title', 'img', 'grc_sec_six_list']
 
 
 
class GrcSecSixSerializer(serializers.ModelSerializer):
    grc_sec_six_category = GrcSecSixCategorySerializer(many=True, read_only=True)
 
    class Meta:
        model = GrcSecSix
        fields = ['id', 'section_title', 'paragraph_title', 'desc', 'img', 'grc_sec_six_category']


class GrcSecSevenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecSevenList
        fields = '__all__'

class GrcSecSevenSerializer(serializers.ModelSerializer):
    grc_sec_seven_list = GrcSecSevenListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcSecSeven
        fields = '__all__'


class GrcSecEightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcSecEightList
        fields = '__all__'

class GrcSecEightSerializer(serializers.ModelSerializer):
    grc_sec_eight_list = GrcSecEightListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcSecEight
        fields = '__all__'


class GrcMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcMetaTag
        fields = '__all__'


class GrcSubPageSerializer(serializers.ModelSerializer):
    grc_sec_one = GrcSecOneSerializer(read_only=True)
    grc_sec_two = GrcSecTwoSerializer(read_only=True)
    grc_sec_three = GrcSecThreeSerializer(read_only=True)
    grc_sec_four = GrcSecFourSerializer(read_only=True)
    grc_sec_five = GrcSecFiveSerializer(read_only=True)
    grc_sec_six = GrcSecSixSerializer(read_only=True)
    grc_sec_seven = GrcSecSevenSerializer(read_only=True)
    grc_sec_eight = GrcSecEightSerializer(read_only=True)
    grc_meta = GrcMetaTagSerializer(read_only=True)

    class Meta:
        model = GrcSubPage
        fields = '__all__'



    # Management Training Serializer Starts

class ManagementTrnSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnSecOneList
        fields = '__all__'


class ManagementTrnSecOneSerializer(serializers.ModelSerializer):
    trn_sec_one_list = ManagementTrnSecOneListSerializer(many=True, read_only=True)
    
    class Meta:
        model = ManagementTrnSecOne
        fields = '__all__'



class ManagementTrnSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnSecTwoList
        fields = '__all__'

class ManagementTrnSecTwoSerializer(serializers.ModelSerializer):
    trn_sec_two_list = ManagementTrnSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecTwo
        fields = '__all__'


class ManagementTrnSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnSecThreeList
        fields = '__all__'

class ManagementTrnSecThreeSerializer(serializers.ModelSerializer):
    trn_sec_three_list = ManagementTrnSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecThree
        fields = '__all__'


class ManagementTrnSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnSecFourList
        fields = '__all__'

class ManagementTrnSecFourSerializer(serializers.ModelSerializer):
    trn_sec_four_list = ManagementTrnSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecFour
        fields = '__all__'



class ManagementTrnSecFiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnSecFiveList
        fields = '__all__'


class ManagementTrnSecFiveCategorySerializer(serializers.ModelSerializer):
    trn_sec_five_list = ManagementTrnSecFiveListSerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecFiveCategory
        fields = ['id', 'title', 'img', 'trn_sec_five_list']


class ManagementTrnSecFiveSerializer(serializers.ModelSerializer):
    trn_sec_five_category = ManagementTrnSecFiveCategorySerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecFive
        fields = ['id', 'section_title', 'desc', 'trn_sec_five_category']


class ManagementTrnSecSixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnSecSixList
        fields = '__all__'


class ManagementTrnSecSixCategorySerializer(serializers.ModelSerializer):
    trn_sec_six_list = ManagementTrnSecSixListSerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecSixList
        fields = '__all__'



class ManagementTrnSecSixSerializer(serializers.ModelSerializer):
    trn_sec_six_category = ManagementTrnSecSixCategorySerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecSix
        fields = '__all__'


class ManagementTrnSecSevenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnSecSevenList
        fields = '__all__'


class ManagementTrnSecSevenSerializer(serializers.ModelSerializer):
    trn_sec_seven_list= ManagementTrnSecSevenListSerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTrnSecSeven
        fields = '__all__'



class ManagementTrnMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementTrnMetaTag
        fields = '__all__'
        


class ManagementTrnSubPageSerializer(serializers.ModelSerializer):
    trn_sec_one = ManagementTrnSecOneSerializer(read_only=True)
    trn_sec_two = ManagementTrnSecTwoSerializer(read_only=True)
    trn_sec_three = ManagementTrnSecThreeSerializer(read_only=True)
    trn_sec_four = ManagementTrnSecFourSerializer(read_only=True)
    trn_sec_five = ManagementTrnSecFiveSerializer(read_only=True)
    trn_sec_six = ManagementTrnSecSixSerializer(read_only=True)
    trn_sec_seven = ManagementTrnSecSevenSerializer(read_only=True)
    trn_meta = ManagementTrnMetaTagSerializer(read_only=True)

    class Meta:
        model = ManagementTrnSubPage
        fields = '__all__'

    #Management Training Serializer Ends




      # Professional Training Serializer Starts
 
class ProfessionalTrnSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnSecOneList
        fields = '__all__'
 
 
class ProfessionalTrnSecOneSerializer(serializers.ModelSerializer):
    prf_trn_sec_one_list = ProfessionalTrnSecOneListSerializer(many=True, read_only=True)
   
    class Meta:
        model = ProfessionalTrnSecOne
        fields = '__all__'
 
 
 
class ProfessionalTrnSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnSecTwoList
        fields = '__all__'
 
class ProfessionalTrnSecTwoSerializer(serializers.ModelSerializer):
    prf_trn_sec_two_list = ProfessionalTrnSecTwoListSerializer(many=True, read_only=True)
 
    class Meta:
        model = ProfessionalTrnSecTwo
        fields = '__all__'
 
 
class ProfessionalTrnSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnSecThreeList
        fields = '__all__'
 
class ProfessionalTrnSecThreeSerializer(serializers.ModelSerializer):
    prf_trn_sec_three_list = ProfessionalTrnSecThreeListSerializer(many=True, read_only=True)
 
    class Meta:
        model = ProfessionalTrnSecThree
        fields = '__all__'
 
 
class ProfessionalTrnSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnSecFourList
        fields = '__all__'
 
class ProfessionalTrnSecFourSerializer(serializers.ModelSerializer):
    prf_trn_sec_four_list = ProfessionalTrnSecFourListSerializer(many=True, read_only=True)
 
    class Meta:
        model = ProfessionalTrnSecFour
        fields = '__all__'
 
 
class ProfessionalTrnSecFiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnSecFiveList
        fields = '__all__'

class ProfessionalTrnSecFiveCategorySerializer(serializers.ModelSerializer):
    prf_trn_sec_five_list = ProfessionalTrnSecFiveListSerializer(many=True, read_only=True)

    class Meta:
        model = ProfessionalTrnSecFiveCategory
        fields = ['id', 'title', 'img', 'prf_trn_sec_five_list']
 
class ProfessionalTrnSecFiveSerializer(serializers.ModelSerializer):
    prf_trn_sec_five_category = ProfessionalTrnSecFiveCategorySerializer(many=True, read_only=True)
 
    class Meta:
        model = ProfessionalTrnSecFive
        fields = ['id', 'section_title','sub_text','desc','level_heading','prf_trn_sec_five_category']

 
class ProfessionalTrnSecSixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnSecSixList
        fields = '__all__'
 
 
class ProfessionalTrnSecSixCategorySerializer(serializers.ModelSerializer):
    prf_trn_sec_six_list = ProfessionalTrnSecSixListSerializer(many=True, read_only=True)
 
    class Meta:
        model = ProfessionalTrnSecSixList
        fields = '__all__'
 
 
 
class ProfessionalTrnSecSixSerializer(serializers.ModelSerializer):
    prf_trn_sec_six_category = ProfessionalTrnSecSixCategorySerializer(many=True, read_only=True)
 
    class Meta:
        model = ProfessionalTrnSecSix
        fields = '__all__'


class ProfessionalTrnSecSevenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnSecSevenList
        fields = '__all__'


class ProfessionalTrnSecSevenSerializer(serializers.ModelSerializer):
    prf_trn_sec_seven_list= ProfessionalTrnSecSevenListSerializer(many=True, read_only=True)

    class Meta:
        model = ProfessionalTrnSecSeven
        fields = '__all__'
 
 
class ProfessionalTrnMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalTrnMetaTag
        fields = '__all__'
 
 
class ProfessionalTrnSubPageSerializer(serializers.ModelSerializer):
    prf_trn_sec_one = ProfessionalTrnSecOneSerializer(read_only=True)
    prf_trn_sec_two = ProfessionalTrnSecTwoSerializer(read_only=True)
    prf_trn_sec_three = ProfessionalTrnSecThreeSerializer(read_only=True)
    prf_trn_sec_four = ProfessionalTrnSecFourSerializer(read_only=True)
    prf_trn_sec_five = ProfessionalTrnSecFiveSerializer(read_only=True)
    prf_trn_sec_six = ProfessionalTrnSecSixSerializer(read_only=True)
    prf_trn_sec_seven = ProfessionalTrnSecSevenSerializer(read_only=True)
    prf_trn_meta = ProfessionalTrnMetaTagSerializer(read_only=True)
 
    class Meta:
        model = ProfessionalTrnSubPage
        fields = '__all__'
 
    #Professional Training Serializer Ends


    #Audir Serializer Starts

class AuditSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSecOneList
        fields = '__all__'


class AuditSecOneSerializer(serializers.ModelSerializer):
    audit_sec_one_list = AuditSecOneListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditSecOne
        fields = '__all__'


class AuditSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSecTwoList
        fields = '__all__'

class AuditSecTwoSerializer(serializers.ModelSerializer):
    audit_sec_two_list = AuditSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditSecTwo
        fields = '__all__'


class AuditSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSecThreeList
        fields = '__all__'

class AuditSecThreeSerializer(serializers.ModelSerializer):
    audit_sec_three_list = AuditSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditSecThree
        fields = '__all__'


class AuditSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSecFourList
        fields = '__all__'

class AuditSecFourSerializer(serializers.ModelSerializer):
    audit_sec_four_list = AuditSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditSecFour
        fields = '__all__'



class AuditSecFiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSecFourList
        fields = '__all__'


class AuditSecFiveSerializer(serializers.ModelSerializer):
    audit_sec_five_list = AuditSecFiveListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditSecFive
        fields = '__all__'


class AuditSecSixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSecSixList
        fields = '__all__'

class AuditSecSixSerializer(serializers.ModelSerializer):
    audit_sec_six_list = AuditSecSixListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditSecSix
        fields = '__all__'


class AuditSecSevenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSecSevenList
        fields = '__all__'

class AuditSecSevenSerializer(serializers.ModelSerializer):
    audit_sec_seven_list = AuditSecSevenListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditSecSeven
        fields = '__all__'


class AuditMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMetaTag
        fields = '__all__'

class AuditSubPageSerializer(serializers.ModelSerializer):
    audit_sec_one = AuditSecOneSerializer(read_only=True)
    audit_sec_two = AuditSecTwoSerializer(read_only=True)
    audit_sec_three = AuditSecThreeSerializer(read_only=True)
    audit_sec_four = AuditSecFourSerializer(read_only=True)
    audit_sec_five = AuditSecFiveSerializer(read_only=True)
    audit_sec_six = AuditSecSixSerializer(read_only=True)
    audit_sec_seven = AuditSecSevenSerializer(read_only=True)
    audit_meta = AuditMetaTagSerializer(read_only=True)

    class Meta:
        model = AuditSubPage
        fields = '__all__'


#Audit Serializer Ends


#Security Sub Service Serializer Starts





class StcSecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecOne
        fields = '__all__'
 
 
class StcSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecTwoList
        fields = '__all__'
 
class StcSecTwoSerializer(serializers.ModelSerializer):
    stc_sec_two_list = StcSecTwoListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecTwo
        fields = '__all__'
 
 
class StcSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecThreeList
        fields = '__all__'
 
class StcSecThreeSerializer(serializers.ModelSerializer):
    stc_sec_three_list = StcSecThreeListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecThree
        fields = '__all__'
 
 
class StcSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecFourList
        fields = '__all__'
 
class StcSecFourSerializer(serializers.ModelSerializer):
    stc_sec_four_list = StcSecFourListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecFour
        fields = '__all__'
 
 
 
class StcSecFiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecFiveList
        fields = '__all__'
 
class StcSecFiveSerializer(serializers.ModelSerializer):
    stc_sec_five_list = StcSecFiveListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecFive
        fields = '__all__'
 
 
 
class StcSecSixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecSixList
        fields = '__all__'
 
class StcSecSixSerializer(serializers.ModelSerializer):
    stc_sec_six_list = StcSecSixListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecSix
        fields = '__all__'
 
 
 
class StcSecSevenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecSevenList
        fields = '__all__'
 
class StcSecSevenSerializer(serializers.ModelSerializer):
    stc_sec_seven_list = StcSecSevenListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecSeven
        fields = '__all__'
 
 
class StcSecEightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecEightList
        fields = '__all__'
 
class StcSecEightSerializer(serializers.ModelSerializer):
    stc_sec_eight_list = StcSecEightListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecEight
        fields = '__all__'



class StcSecNineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcSecNineList
        fields = '__all__'
 
class StcSecNineSerializer(serializers.ModelSerializer):
    stc_sec_nine_list = StcSecNineListSerializer(many=True, read_only=True)
 
    class Meta:
        model = StcSecNine
        fields = '__all__'
  
class StcMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMetaTag
        fields = '__all__'
 
 
class StcSubPageSerializer(serializers.ModelSerializer):
    stc_sec_one = StcSecOneSerializer(read_only=True)
    stc_sec_two = StcSecTwoSerializer(read_only=True)
    stc_sec_three = StcSecThreeSerializer(read_only=True)
    stc_sec_four = StcSecFourSerializer(read_only=True)
    stc_sec_five = StcSecFiveSerializer(read_only=True)
    stc_sec_six = StcSecSixSerializer(read_only=True)
    stc_sec_seven = StcSecSevenSerializer(read_only=True)
    stc_sec_eight = StcSecEightSerializer(read_only=True)
    stc_sec_nine = StcSecNineSerializer(read_only=True)
    stc_meta = StcMetaTagSerializer(read_only=True)
 
    class Meta:
        model = StcSubPage
        fields = '__all__'


#Security Sub Service Serializer Ends Here


#Grc Main Page Serializer starts


class GrcMainSecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcMainSecOne
        fields = '__all__'


class GrcMainSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcMainSecTwoList
        fields = '__all__'

class GrcMainSecTwoSerializer(serializers.ModelSerializer):
    grcmain_sec_two_list = GrcMainSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcMainSecTwo
        fields = '__all__'


class GrcMainSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcMainSecThreeList
        fields = '__all__'

class GrcMainSecThreeSerializer(serializers.ModelSerializer):
    grcmain_sec_three_list = GrcMainSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcMainSecThree
        fields = '__all__'


class GrcMainFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcMainSecFourList
        fields = '__all__'


class GrcMainSecFourCategorySerializer(serializers.ModelSerializer):
    grcmain_sec_four_list = GrcMainFourListSerializer(many=True, read_only=True)
 
    class Meta:
        model = GrcMainSecFourCategory
        fields = ['id', 'title', 'grcmain_sec_four_list']
 
 
 
class GrcMainSecFourSerializer(serializers.ModelSerializer):
    grcmain_sec_four_category = GrcMainSecFourCategorySerializer(many=True, read_only=True)
 
    class Meta:
        model = GrcMainSecFour
        fields = ['id', 'section_title', 'paragraph_title', 'desc', 'grcmain_sec_four_category']


class GrcMainSecFiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcMainSecFiveList
        fields = '__all__'


class GrcMainSecFiveSerializer(serializers.ModelSerializer):
    grcmain_sec_five_list = GrcMainSecFiveListSerializer(many=True, read_only=True)

    class Meta:
        model = GrcMainSecFive
        fields = '__all__'


class GrcMainMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcMainMetaTag
        fields = '__all__'


class GrcMainPageSerializer(serializers.ModelSerializer):
    grcmain_sec_one = GrcMainSecOneSerializer(read_only=True)
    grcmain_sec_two = GrcMainSecTwoSerializer(read_only=True)
    grcmain_sec_three = GrcMainSecThreeSerializer(read_only=True)
    grcmain_sec_four = GrcMainSecFourSerializer(read_only=True)
    grcmain_sec_five = GrcMainSecFiveSerializer(read_only=True)
    grcmain_meta = GrcMainMetaTagSerializer(read_only=True)

    class Meta:
        model = GrcMainPage
        fields = '__all__'


#Grc Main Page Serializer Ends


#Audit Main Page Serializer Starts


class AuditMainSecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMainSecOne
        fields = '__all__'


class AuditMainSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMainSecTwoList
        fields = '__all__'

class AuditMainSecTwoSerializer(serializers.ModelSerializer):
    auditmain_sec_two_list = AuditMainSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditMainSecTwo
        fields = '__all__'


class AuditMainSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMainSecThreeList
        fields = '__all__'

class AuditMainSecThreeSerializer(serializers.ModelSerializer):
    auditmain_sec_three_list = AuditMainSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = AuditMainSecThree
        fields = '__all__'


class AuditMainMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMainMetaTag
        fields = '__all__'


class AuditMainPageSerializer(serializers.ModelSerializer):
    auditmain_sec_one = AuditMainSecOneSerializer(read_only=True)
    auditmain_sec_two = AuditMainSecTwoSerializer(read_only=True)
    auditmain_sec_three = AuditMainSecThreeSerializer(read_only=True)
    auditmain_meta = AuditMainMetaTagSerializer(read_only=True)

    class Meta:
        model = AuditMainPage
        fields = '__all__'


#Audit Main Page Serializer Ends


#Training Main Serializer Starts


class TrnMainSecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrnMainSecOne
        fields = '__all__'


class TrnMainSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrnMainSecTwoList
        fields = '__all__'

class TrnMainSecTwoSerializer(serializers.ModelSerializer):
    trnmain_sec_two_list = TrnMainSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = TrnMainSecTwo
        fields = '__all__'

class TrnMainSecThreeListListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrnMainSecThreeListList
        fields = '__all__'

class TrnMainSecThreeListListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrnMainSecThreeListList
        fields = '__all__'


class TrnMainSecThreeListSerializer(serializers.ModelSerializer):
    trnmain_sec_three_list_list = TrnMainSecThreeListListSerializer(many=True, read_only=True)
    class Meta:
        model = TrnMainSecThreeList
        fields = '__all__'

class TrnMainSecThreeSerializer(serializers.ModelSerializer):
    trnmain_sec_three_list = TrnMainSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = TrnMainSecThree
        fields = '__all__'


class TrnMainSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrnMainSecFourList
        fields = '__all__'

class TrnMainSecFourSerializer(serializers.ModelSerializer):
    trnmain_sec_four_list = TrnMainSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = TrnMainSecFour
        fields = '__all__'


class TrnMainMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrnMainMetaTag
        fields = '__all__'


class TrnMainPageSerializer(serializers.ModelSerializer):
    trnmain_sec_one = TrnMainSecOneSerializer(read_only=True)
    trnmain_sec_two = TrnMainSecTwoSerializer(read_only=True)
    trnmain_sec_three = TrnMainSecThreeSerializer(read_only=True)
    trnmain_sec_four = TrnMainSecFourSerializer(read_only=True)
    trnmain_meta = TrnMainMetaTagSerializer(read_only=True)

    class Meta:
        model = TrnMainPage
        fields = '__all__'

#Training Main Page Serializer Ends


class ContactDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactDetail
        fields = '__all__'


#Management system training strats

class MstMainSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainSecOneList
        fields = '__all__'


class MstMainSecOneSerializer(serializers.ModelSerializer):
    mstmain_sec_one_list = MstMainSecOneListSerializer(many=True, read_only=True)

    class Meta:
        model = MstMainSecOne
        fields = '__all__'



class MstMainSecTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainSecTwo
        fields = '__all__'


class MstMainSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainSecThreeList
        fields = '__all__'

class MstMainSecThreeSerializer(serializers.ModelSerializer):
    mstmain_sec_three_list = MstMainSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = MstMainSecThree
        fields = '__all__'


class MstMainSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainSecFourList
        fields = '__all__'

class MstMainSecFourSerializer(serializers.ModelSerializer):
    mstmain_sec_four_list = MstMainSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = MstMainSecFour
        fields = '__all__'


class MstMainSecFiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainSecFiveList
        fields = '__all__'

class MstMainSecFiveSerializer(serializers.ModelSerializer):
    mstmain_sec_five_list = MstMainSecFiveListSerializer(many=True, read_only=True)

    class Meta:
        model = MstMainSecFive
        fields = '__all__'

class MstMainSecSixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainSecSixList
        fields = '__all__'

class MstMainSecSixSerializer(serializers.ModelSerializer):
    mstmain_sec_six_list = MstMainSecSixListSerializer(many=True, read_only=True)

    class Meta:
        model = MstMainSecSix  
        fields = '__all__'


class MstMainSecSevenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainSecSevenList
        fields = '__all__'


class MstMainSecSevenSerializer(serializers.ModelSerializer):
    mstmain_sec_seven_list = MstMainSecSevenListSerializer(many=True, read_only=True)

    class Meta:
        model = MstMainSecSeven
        fields = '__all__'


class MstMainMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMainMetaTag
        fields = '__all__'


class MstMainPageSerializer(serializers.ModelSerializer):
    mstmain_sec_one = MstMainSecOneSerializer(read_only=True)
    mstmain_sec_two = MstMainSecTwoSerializer(read_only=True)
    mstmain_sec_three = MstMainSecThreeSerializer(read_only=True)
    mstmain_sec_four = MstMainSecFourSerializer(read_only=True)
    mstmain_sec_five = MstMainSecFiveSerializer(read_only=True)
    mstmain_sec_six = MstMainSecSixSerializer(read_only=True)
    mstmain_sec_seven = MstMainSecSevenSerializer(read_only=True)
    mstmain_meta = MstMainMetaTagSerializer(read_only=True)

    class Meta:
        model = MstMainPage
        fields = '__all__'

#Management system training ends


#professional training starts 


class PtrnMainSecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PtrnMainSecOne
        fields = '__all__'


class PtrnMainSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PtrnMainSecTwoList
        fields = '__all__'


class PtrnMainSecTwoSerializer(serializers.ModelSerializer):
    ptrnmain_sec_two_list = PtrnMainSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = PtrnMainSecTwo
        fields = '__all__'


class PtrnMainSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PtrnMainSecThreeList
        fields = '__all__'


class PtrnMainSecThreeSerializer(serializers.ModelSerializer):
    ptrnmain_sec_three_list = PtrnMainSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = PtrnMainSecThree
        fields = '__all__'


class PtrnMainSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PtrnMainSecFourList
        fields = '__all__'

class PtrnMainSecFourSerializer(serializers.ModelSerializer):
    ptrnmain_sec_four_list = PtrnMainSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = PtrnMainSecFour
        fields = '__all__'


class PtrnMainMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PtrnMainMetaTag
        fields = '__all__'


class PtrnMainPageSerializer(serializers.ModelSerializer):
    ptrnmain_sec_one = PtrnMainSecOneSerializer(read_only=True)
    ptrnmain_sec_two = PtrnMainSecTwoSerializer(read_only=True)
    ptrnmain_sec_three = PtrnMainSecThreeSerializer(read_only=True)
    ptrnmain_sec_four = PtrnMainSecFourSerializer(read_only=True)
    ptrnmain_meta = PtrnMainMetaTagSerializer(read_only=True)

    class Meta:
        model = PtrnMainPage
        fields = '__all__'

#professional training ends 



#security system testing

class StcMainSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMainSecOneList
        fields = '__all__'


class StcMainSecOneSerializer(serializers.ModelSerializer):
    stcmain_sec_one_list = StcMainSecOneListSerializer(many=True, read_only=True)

    class Meta:
        model = StcMainSecOne
        fields = '__all__'


class StcMainSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMainSecTwoList
        fields = '__all__'


class StcMainSecTwoSerializer(serializers.ModelSerializer):
    stcmain_sec_two_list = StcMainSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = StcMainSecTwo
        fields = '__all__'


class StcMainSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMainSecThreeList
        fields = '__all__'

class StcMainSecThreeSerializer(serializers.ModelSerializer):
    stcmain_sec_three_list = StcMainSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = StcMainSecThree
        fields = '__all__'


class StcMainSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMainSecFourList
        fields = '__all__'

class StcMainSecFourSerializer(serializers.ModelSerializer):
    stcmain_sec_four_list = StcMainSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = StcMainSecFour
        fields = '__all__'


class StcMainSecFiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMainSecFiveList
        fields = '__all__'

class StcMainSecFiveSerializer(serializers.ModelSerializer):
    stcmain_sec_five_list = StcMainSecFiveListSerializer(many=True, read_only=True)

    class Meta:
        model = StcMainSecFive
        fields = '__all__'

class StcMainSecSixListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMainSecSixList
        fields = '__all__'

class StcMainSecSixSerializer(serializers.ModelSerializer):
    stcmain_sec_six_list = StcMainSecSixListSerializer(many=True, read_only=True)

    class Meta:
        model = StcMainSecSix  
        fields = '__all__'


class StcMainMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = StcMainMetaTag
        fields = '__all__'


class StcMainPageSerializer(serializers.ModelSerializer):
    stcmain_sec_one = StcMainSecOneSerializer(read_only=True)
    stcmain_sec_two = StcMainSecTwoSerializer(read_only=True)
    stcmain_sec_three = StcMainSecThreeSerializer(read_only=True)
    stcmain_sec_four = StcMainSecFourSerializer(read_only=True)
    stcmain_sec_five = StcMainSecFiveSerializer(read_only=True)
    stcmain_sec_six = StcMainSecSixSerializer(read_only=True)
    stcmain_meta = StcMainMetaTagSerializer(read_only=True)

    class Meta:
        model = StcMainPage
        fields = '__all__'


#security testing serializer ends




class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'


class MainContactFormSerializer(ModelSerializer):
    class Meta:
        model = MainContactForm
        fields = '__all__'


class CareerFormSerializer(ModelSerializer):
    class Meta:
        model = CareerForm
        fields = '__all__'


class CareerPageSecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPageSecOne
        fields = '__all__'
 
 
class CareerPageSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPageSecTwoList
        fields = '__all__'
 
class CareerPageSecTwoSerializer(serializers.ModelSerializer):
    careerpage_sec_two_list = CareerPageSecTwoListSerializer(many=True, read_only=True)
 
    class Meta:
        model = CareerPageSecTwo
        fields = '__all__'
 
 
class CareerPageMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPageMetaTag
        fields = '__all__'
 
 
class CareerPagePageSerializer(serializers.ModelSerializer):
    careerpage_sec_one = CareerPageSecOneSerializer(read_only=True)
    careerpage_sec_two = CareerPageSecTwoSerializer(read_only=True)
    careerpage_meta = CareerPageMetaTagSerializer(read_only=True)
 
    class Meta:
        model = CareerPagePage
        fields = '__all__'
 
 
 
 
class PrivacyPolicySecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicySecOne
        fields = '__all__'
 
 
class PrivacyPolicySecTwoSubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicySecTwoSubList
        fields = '__all__'
 
 
class PrivacyPolicySecTwoListSerializer(serializers.ModelSerializer):
    subList = PrivacyPolicySecTwoSubListSerializer(many=True, read_only=True)
 
    class Meta:
        model = PrivacyPolicySecTwoList
        fields = '__all__'
 
 
class PrivacyPolicySecTwoSerializer(serializers.ModelSerializer):
    prpolicy_sec_two_list = PrivacyPolicySecTwoListSerializer(many=True, read_only=True)
 
    class Meta:
        model = PrivacyPolicySecTwo
        fields = '__all__'
 
 
class PrivacyPolicySecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicySecThreeList
        fields = '__all__'
 
class PrivacyPolicySecThreeSerializer(serializers.ModelSerializer):
    prpolicy_sec_three_list = PrivacyPolicySecThreeListSerializer(many=True, read_only=True)
 
    class Meta:
        model = PrivacyPolicySecThree
        fields = '__all__'
 
 
class PrivacyPolicyMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicyMetaTag
        fields = '__all__'
 
 
class PrivacyPolicySubPageSerializer(serializers.ModelSerializer):
    prpolicy_sec_one = PrivacyPolicySecOneSerializer(read_only=True)
    prpolicy_sec_two = PrivacyPolicySecTwoSerializer(read_only=True)
    prpolicy_sec_three = PrivacyPolicySecThreeSerializer(read_only=True)
    prpolicy_meta = PrivacyPolicyMetaTagSerializer(read_only=True)
 
    class Meta:
        model = PrivacyPolicyPage
        fields = '__all__'


class BlogSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSecOneList
        fields = '__all__'

# BlogSecOne Serializer
class BlogSecOneSerializer(serializers.ModelSerializer):
    blog_sec_one_list = BlogSecOneListSerializer(many=True, read_only=True)

    class Meta:
        model = BlogSecOne
        fields = '__all__'


# BlogSecTwoList Serializer
class BlogSecTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSecTwoList
        fields = '__all__'

# BlogSecTwo Serializer
class BlogSecTwoSerializer(serializers.ModelSerializer):
    blog_sec_two_list = BlogSecTwoListSerializer(many=True, read_only=True)

    class Meta:
        model = BlogSecTwo
        fields = '__all__'


# BlogSecThreeList Serializer
class BlogSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSecThreeList
        fields = '__all__'

# BlogSecThree Serializer
class BlogSecThreeSerializer(serializers.ModelSerializer):
    blog_sec_three_list = BlogSecThreeListSerializer(many=True, read_only=True)

    class Meta:
        model = BlogSecThree
        fields = '__all__'


class BlogSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSecFourList
        fields = '__all__'

class BlogSecFourSerializer(serializers.ModelSerializer):
    grcmain_sec_four_list = BlogSecFourListSerializer(many=True, read_only=True)

    class Meta:
        model = BlogSecFour
        fields = '__all__'


class BlogMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogMetaTag
        fields = '__all__'


class BlogCtgSerializer(ModelSerializer):
    class Meta:
        model = BlogCtg
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    blog_sec_one = BlogSecOneSerializer(read_only=True)
    blog_sec_two = BlogSecTwoSerializer(read_only=True)
    blog_sec_three = BlogSecThreeSerializer(read_only=True)
    blog_sec_four = BlogSecFourSerializer(read_only=True)
    blog_meta = BlogMetaTagSerializer(read_only=True)
    blogs = BlogCtgSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

class CustomerFeedbackFormSerializer(ModelSerializer):
    class Meta:
        model = CustomerFeedbackForm
        fields = '__all__'



class CmgMetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmgClientsMeta
        fields = '__all__'
 
class cmgSecOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmgSecOneList
        fields = '__all__'
 
class cmgSecOneSerializer(serializers.ModelSerializer):
    cmg_sec_one_list = cmgSecOneListSerializer(many=True, read_only=True)
 
    class Meta:
        model = CmgSecOne
        fields = '__all__'
 
class cmgSecTwoListSecOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmgSecTwoListSecOne
        fields = '__all__'

class cmgSecTwoListSecTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmgSecTwoListSecTwo
        fields = '__all__'
 
class cmgSecTwoSerializer(serializers.ModelSerializer):
    cmg_sec_two_list_sec_one = cmgSecTwoListSecOneSerializer(many=True, read_only=True)
    cmg_sec_two_list_sec_two = cmgSecTwoListSecTwoSerializer(many=True, read_only=True)
 
    class Meta:
        model = CmgSecTwo
        fields = '__all__'
 
class cmgSecThreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmgSecThreeList
        fields = '__all__'
 
class cmgSecThreeSerializer(serializers.ModelSerializer):
    cmg_sec_three_list = cmgSecThreeListSerializer(many=True, read_only=True)
 
    class Meta:
        model = CmgSecThree
        fields = '__all__'
 
class cmgSecFourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmgSecFourList
        fields = '__all__'
 
class cmgSecFourSerializer(serializers.ModelSerializer):
    cmg_sec_four_list = cmgSecFourListSerializer(many=True, read_only=True)
 
    class Meta:
        model = CmgSecFour
        fields = '__all__'
 
class CmgSubPageSerializer(serializers.ModelSerializer):
    cmg_sec_one = cmgSecOneSerializer(read_only=True)
    cmg_sec_two = cmgSecTwoSerializer(read_only=True)
    cmg_sec_three = cmgSecThreeSerializer(read_only=True)
    cmg_sec_four = cmgSecFourSerializer(read_only=True)
    CmgMetaTags = CmgMetaTagsSerializer(read_only=True)
 
    class Meta:
        model = CmgSubPage
        fields = '__all__'


class NavCtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavCtg
        fields = '__all__'

class NavSerializer(serializers.ModelSerializer):
    nav_ctg = NavCtgSerializer(read_only=True) 

    class Meta:
        model = Nav
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'



class GrcOfferingCtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrcOfferingCtg
        fields = '__all__'

class GrcOfferingSerializer(serializers.ModelSerializer):
    grc_offering_ctg = GrcOfferingCtgSerializer(read_only=True) 

    class Meta:
        model = GrcOffering
        fields = '__all__'


class SuspendedClientBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspendedClientBanner
        fields = '__all__'


class CertificationProcessBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationProcessBanner
        fields = '__all__'


class CertificationGuidlineBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationGuidlineBanner
        fields = '__all__'


class AppealHandlingBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppealHandlingBanner
        fields = '__all__'


class GrievancesBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrievancesBanner
        fields = '__all__'


class ComplaintHandlingProcessBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintHandlingProcessBanner
        fields = '__all__'


class CustomerFeedbackBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedbackBanner
        fields = '__all__'


class CertificationVerificationBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationVerificationBanner
        fields = '__all__'




