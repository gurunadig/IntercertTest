from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
 
class ImportExportAdmin(ImportExportModelAdmin):
    ...


# Register your models here.
admin.site.register(TestApi)
admin.site.register(Testimonial)
admin.site.register(AboutContent, ImportExportAdmin)
admin.site.register(VideoBanner)
admin.site.register(Stat)
admin.site.register(ServiceCarousel)
admin.site.register(ApproachStep)
admin.site.register(Certification, ImportExportAdmin)
admin.site.register(Client1, ImportExportAdmin)
admin.site.register(Client2)
admin.site.register(IndustryWeServe)
admin.site.register(AboutUsPage)
admin.site.register(AboutUsMeta)
admin.site.register(WhoWeAre)
admin.site.register(WWRList)
admin.site.register(OurMission)
admin.site.register(OMList)
admin.site.register(WeAreGlobal, ImportExportAdmin)
admin.site.register(WhyUs)
admin.site.register(WUList)
admin.site.register(Accredition)
admin.site.register(ImplementOfIP)
admin.site.register(IOIPList)
admin.site.register(QualityPolicy)
admin.site.register(ImpartialityPolicy)
admin.site.register(SuspendedClientsMeta)
admin.site.register(SuspendedClients)
admin.site.register(SuspendedClientsPage)
admin.site.register(AppealHandlingMeta)
admin.site.register(AppealHandling)
admin.site.register(AHList)
admin.site.register(AppealHandlingPage)
admin.site.register(ComplainHandlingPage)
admin.site.register(CHList)
admin.site.register(ComplainHandlingMeta)
admin.site.register(GrievancesPage)
admin.site.register(GrievancesMeta)
admin.site.register(GrievancesList)
admin.site.register(CerificationProcessImg)
admin.site.register(GrantOrRefuse)
admin.site.register(GOrRList)
admin.site.register(MaintainCertification)
admin.site.register(MCList)
admin.site.register(DetailsForIssuing)
admin.site.register(DFIList)
admin.site.register(WithdrawOfCertification)
admin.site.register(WOCList)
admin.site.register(SuspensionOfCertification)
admin.site.register(SOCList)
admin.site.register(RestoringOfCertification)
admin.site.register(ROCList)
admin.site.register(ExpandingOrReducing)
admin.site.register(EORList)
admin.site.register(CertificationProcessPage)
admin.site.register(CertificationMeta)




admin.site.register(GrcMetaTag, ImportExportAdmin)
admin.site.register(GrcSecOneList, ImportExportAdmin)
admin.site.register(GrcSecOne, ImportExportAdmin)
admin.site.register(GrcSecTwoList, ImportExportAdmin)
admin.site.register(GrcSecTwo, ImportExportAdmin)
admin.site.register(GrcSecThreeList, ImportExportAdmin)
admin.site.register(GrcSecThree, ImportExportAdmin)
admin.site.register(GrcSecFourList, ImportExportAdmin)
admin.site.register(GrcSecFour, ImportExportAdmin)
admin.site.register(GrcSecFive, ImportExportAdmin)
admin.site.register(GrcSecSixCategory, ImportExportAdmin)
admin.site.register(GrcSecSixList, ImportExportAdmin)
admin.site.register(GrcSecSix, ImportExportAdmin)
admin.site.register(GrcSecSevenList, ImportExportAdmin)
admin.site.register(GrcSecSeven, ImportExportAdmin)
admin.site.register(GrcSecEightList, ImportExportAdmin)
admin.site.register(GrcSecEight, ImportExportAdmin)
admin.site.register(GrcSubPage, ImportExportAdmin)


admin.site.register(ManagementTrnMetaTag)
admin.site.register(ManagementTrnSecOne)
admin.site.register(ManagementTrnSecOneList)
admin.site.register(ManagementTrnSecTwo)
admin.site.register(ManagementTrnSecTwoList)
admin.site.register(ManagementTrnSecThree)
admin.site.register(ManagementTrnSecThreeList)
admin.site.register(ManagementTrnSecFour)
admin.site.register(ManagementTrnSecFourList)
admin.site.register(ManagementTrnSecFive)
admin.site.register(ManagementTrnSecFiveCategory)
admin.site.register(ManagementTrnSecFiveList)
admin.site.register(ManagementTrnSecSix)
admin.site.register(ManagementTrnSecSixList)
admin.site.register(ManagementTrnSecSevenList)
admin.site.register(ManagementTrnSecSeven)
admin.site.register(ManagementTrnSubPage)



admin.site.register(ProfessionalTrnMetaTag)
admin.site.register(ProfessionalTrnSecOne)
admin.site.register(ProfessionalTrnSecOneList)
admin.site.register(ProfessionalTrnSecTwo)
admin.site.register(ProfessionalTrnSecTwoList)
admin.site.register(ProfessionalTrnSecThree)
admin.site.register(ProfessionalTrnSecThreeList)
admin.site.register(ProfessionalTrnSecFour)
admin.site.register(ProfessionalTrnSecFourList)
admin.site.register(ProfessionalTrnSecFive)
admin.site.register(ProfessionalTrnSecFiveCategory)
admin.site.register(ProfessionalTrnSecFiveList)
admin.site.register(ProfessionalTrnSecSix)
admin.site.register(ProfessionalTrnSecSixList)
admin.site.register(ProfessionalTrnSecSeven)
admin.site.register(ProfessionalTrnSecSevenList)
admin.site.register(ProfessionalTrnSubPage)



admin.site.register(AuditMetaTag)
admin.site.register(AuditSecOne)
admin.site.register(AuditSecOneList)
admin.site.register(AuditSecTwoList)
admin.site.register(AuditSecTwo)
admin.site.register(AuditSecThreeList)
admin.site.register(AuditSecThree)
admin.site.register(AuditSecFourList)
admin.site.register(AuditSecFour)
admin.site.register(AuditSecFiveList)
admin.site.register(AuditSecFive)
admin.site.register(AuditSecSixList)
admin.site.register(AuditSecSix)
admin.site.register(AuditSecSevenList)
admin.site.register(AuditSecSeven)
admin.site.register(AuditSubPage)


admin.site.register(StcMetaTag, ImportExportAdmin)
admin.site.register(StcSecOne, ImportExportAdmin)
admin.site.register(StcSecTwoList, ImportExportAdmin)
admin.site.register(StcSecTwo, ImportExportAdmin)
admin.site.register(StcSecThreeList, ImportExportAdmin)
admin.site.register(StcSecThree, ImportExportAdmin)
admin.site.register(StcSecFourList, ImportExportAdmin)
admin.site.register(StcSecFour, ImportExportAdmin)
admin.site.register(StcSecFiveList, ImportExportAdmin)
admin.site.register(StcSecFive, ImportExportAdmin)
admin.site.register(StcSecSixList, ImportExportAdmin)
admin.site.register(StcSecSix, ImportExportAdmin)
admin.site.register(StcSecSevenList, ImportExportAdmin)
admin.site.register(StcSecSeven, ImportExportAdmin)
admin.site.register(StcSecEightList, ImportExportAdmin)
admin.site.register(StcSecEight, ImportExportAdmin)
admin.site.register(StcSecNineList, ImportExportAdmin)
admin.site.register(StcSecNine, ImportExportAdmin)
admin.site.register(StcSubPage, ImportExportAdmin)



admin.site.register(GrcMainMetaTag, ImportExportAdmin)
admin.site.register(GrcMainSecOne, ImportExportAdmin)
admin.site.register(GrcMainSecTwoList, ImportExportAdmin)
admin.site.register(GrcMainSecTwo, ImportExportAdmin)
admin.site.register(GrcMainSecThreeList, ImportExportAdmin)
admin.site.register(GrcMainSecThree, ImportExportAdmin)
admin.site.register(GrcMainSecFourList, ImportExportAdmin)
admin.site.register(GrcMainSecFour, ImportExportAdmin)
admin.site.register(GrcMainSecFourCategory, ImportExportAdmin)
admin.site.register(GrcMainSecFiveList, ImportExportAdmin)
admin.site.register(GrcMainSecFive, ImportExportAdmin)
admin.site.register(GrcMainPage, ImportExportAdmin)



admin.site.register(AuditMainMetaTag, ImportExportAdmin)
admin.site.register(AuditMainSecOne, ImportExportAdmin)
admin.site.register(AuditMainSecTwoList, ImportExportAdmin)
admin.site.register(AuditMainSecTwo, ImportExportAdmin)
admin.site.register(AuditMainSecThreeList, ImportExportAdmin)
admin.site.register(AuditMainSecThree, ImportExportAdmin)
admin.site.register(AuditMainPage, ImportExportAdmin)



admin.site.register(TrnMainMetaTag, ImportExportAdmin)
admin.site.register(TrnMainSecOne, ImportExportAdmin)
admin.site.register(TrnMainSecTwoList, ImportExportAdmin)
admin.site.register(TrnMainSecTwo, ImportExportAdmin)
admin.site.register(TrnMainSecThreeList, ImportExportAdmin)
admin.site.register(TrnMainSecThree, ImportExportAdmin)
admin.site.register(TrnMainSecFourList, ImportExportAdmin)
admin.site.register(TrnMainSecFour, ImportExportAdmin)
admin.site.register(TrnMainPage, ImportExportAdmin)

admin.site.register(ContactDetail, ImportExportAdmin)


admin.site.register(MstMainMetaTag, ImportExportAdmin)
admin.site.register(MstMainSecOneList, ImportExportAdmin)
admin.site.register(MstMainSecOne, ImportExportAdmin)
admin.site.register(MstMainSecTwo, ImportExportAdmin)
admin.site.register(MstMainSecThreeList, ImportExportAdmin)
admin.site.register(MstMainSecThree, ImportExportAdmin)
admin.site.register(MstMainSecFourList, ImportExportAdmin)
admin.site.register(MstMainSecFour, ImportExportAdmin)
admin.site.register(MstMainSecFiveList, ImportExportAdmin)
admin.site.register(MstMainSecFive, ImportExportAdmin)
admin.site.register(MstMainSecSixList, ImportExportAdmin)
admin.site.register(MstMainSecSix, ImportExportAdmin)
admin.site.register(MstMainSecSevenList, ImportExportAdmin)
admin.site.register(MstMainSecSeven, ImportExportAdmin)
admin.site.register(MstMainPage, ImportExportAdmin)


admin.site.register(PtrnMainMetaTag, ImportExportAdmin)
admin.site.register(PtrnMainSecOne, ImportExportAdmin)
admin.site.register(PtrnMainSecTwoList, ImportExportAdmin)
admin.site.register(PtrnMainSecTwo, ImportExportAdmin)
admin.site.register(PtrnMainSecThreeList, ImportExportAdmin)
admin.site.register(PtrnMainSecThree, ImportExportAdmin)
admin.site.register(PtrnMainSecFourList, ImportExportAdmin)
admin.site.register(PtrnMainSecFour, ImportExportAdmin)
admin.site.register(PtrnMainPage, ImportExportAdmin)



admin.site.register(StcMainMetaTag, ImportExportAdmin)
admin.site.register(StcMainSecOneList, ImportExportAdmin)
admin.site.register(StcMainSecOne, ImportExportAdmin)
admin.site.register(StcMainSecTwoList, ImportExportAdmin)
admin.site.register(StcMainSecTwo, ImportExportAdmin)
admin.site.register(StcMainSecThreeList, ImportExportAdmin)
admin.site.register(StcMainSecThree, ImportExportAdmin)
admin.site.register(StcMainSecFourList, ImportExportAdmin)
admin.site.register(StcMainSecFour, ImportExportAdmin)
admin.site.register(StcMainSecFiveList, ImportExportAdmin)
admin.site.register(StcMainSecFive, ImportExportAdmin)
admin.site.register(StcMainSecSixList, ImportExportAdmin)
admin.site.register(StcMainSecSix, ImportExportAdmin)
admin.site.register(StcMainPage, ImportExportAdmin)



admin.site.register(ContactForm)
admin.site.register(CareerForm)



admin.site.register(CareerPageMetaTag, ImportExportAdmin)
admin.site.register(CareerPageSecOne, ImportExportAdmin)
admin.site.register(CareerPageSecTwo, ImportExportAdmin)
admin.site.register(CareerPageSecTwoList, ImportExportAdmin)
admin.site.register(CareerPagePage, ImportExportAdmin)
 
admin.site.register(PrivacyPolicyMetaTag, ImportExportAdmin)
admin.site.register(PrivacyPolicyPage, ImportExportAdmin)
admin.site.register(PrivacyPolicySecOne, ImportExportAdmin)
admin.site.register(PrivacyPolicySecTwo, ImportExportAdmin)
admin.site.register(PrivacyPolicySecTwoSubList, ImportExportAdmin)
admin.site.register(PrivacyPolicySecTwoList, ImportExportAdmin)
admin.site.register(PrivacyPolicySecThree, ImportExportAdmin)
admin.site.register(PrivacyPolicySecThreeList, ImportExportAdmin)



admin.site.register(CustomerFeedbackForm, ImportExportAdmin)


admin.site.register(BlogMetaTag, ImportExportAdmin)
admin.site.register(BlogSecOne, ImportExportAdmin)
admin.site.register(BlogSecOneList, ImportExportAdmin)
admin.site.register(BlogSecTwo, ImportExportAdmin)
admin.site.register(BlogSecTwoList, ImportExportAdmin)
admin.site.register(BlogSecThree, ImportExportAdmin)
admin.site.register(BlogSecThreeList, ImportExportAdmin)
admin.site.register(BlogSecFour, ImportExportAdmin)
admin.site.register(BlogSecFourList, ImportExportAdmin)
admin.site.register(Blog, ImportExportAdmin)
admin.site.register(BlogCtg, ImportExportAdmin)



admin.site.register(CmgClientsMeta,ImportExportAdmin)
admin.site.register(CmgSubPage,ImportExportAdmin)
admin.site.register(CmgSecOne,ImportExportAdmin)
admin.site.register(CmgSecOneList,ImportExportAdmin)
admin.site.register(CmgSecTwo,ImportExportAdmin)
admin.site.register(CmgSecTwoList,ImportExportAdmin)
admin.site.register(CmgSecThree,ImportExportAdmin)
admin.site.register(CmgSecThreeList,ImportExportAdmin)
admin.site.register(CmgSecFour,ImportExportAdmin)
admin.site.register(CmgSecFourList,ImportExportAdmin)



admin.site.register(NavCtg,ImportExportAdmin)
admin.site.register(Nav,ImportExportAdmin)



admin.site.register(Search,ImportExportAdmin)


admin.site.register(GrcOfferingCtg,ImportExportAdmin)
admin.site.register(GrcOffering,ImportExportAdmin)