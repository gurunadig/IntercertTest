from django.db import models

class TestApi(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
    

# home page starts
    
# Home Page Models
class VideoBanner(models.Model):
    label = models.CharField(max_length=255)
    video_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Video Banner"
        verbose_name_plural = "Video Banners"    

#Home Page Section
class AboutContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

# class StatCategory(models.Model):
#     label = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.label

class Stat(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    # stat_ctg = models.ForeignKey(StatCategory, on_delete=models.CASCADE, related_name='stat')
    
    def __str__(self):
        return self.title


class Client1(models.Model):
    client_img = models.ImageField(default="400-200.png", null=False, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class Client2(models.Model):
    img_client = models.ImageField(default="400-200.png", null=False, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default="400-200.png", null=False, blank=True)

    def __str__(self):
        return self.title
    

class ServiceCarousel(models.Model):
    heading = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class IndustryWeServe(models.Model):
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    title = models.TextField()

    def __str__(self):
        return self.title

class ApproachStep(models.Model):
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    image_no = models.ImageField(default="400-200.png", null=False, blank=True)
    tooltip = models.TextField(default="")
    tooltip_place = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    

# home page ends


#About Us ________________________________________________________Models start here________#
#About Page Content and Meta Tags
class AboutUsPage(models.Model):
    page_title = models.CharField(max_length=255)
    page_sub = models.TextField()
    page_desc = models.TextField()
    bannerimg = models.ImageField(upload_to='banners/')


class AboutUsMeta(models.Model):
    title = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    author = models.TextField()
    robots = models.TextField()
    googlebot = models.TextField()
    language = models.TextField()
    google_site_verification = models.TextField()
    og_url = models.TextField()
    og_type = models.TextField()
    og_title = models.TextField()
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='og_images/')
    twitter_card = models.TextField()
    twitter_domain = models.TextField()
    twitter_url = models.TextField()
    twitter_title = models.TextField()
    twitter_desc = models.TextField()
    twitter_image = models.ImageField(upload_to='twitter_images/')

#About Page Content and Meta Tags



#Who We Are Section starts
class WhoWeAre(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class WWRList(models.Model):
    who_we_are = models.ForeignKey(WhoWeAre, related_name='wwr_list', on_delete=models.CASCADE)
    list_text = models.TextField()

#Who We Are Section ends


#OurMission Section starts
class OurMission(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class OMList(models.Model):
    our_mission = models.ForeignKey(OurMission, related_name='om_list', on_delete=models.CASCADE)
    list_text = models.TextField()

#OurMission Section ends

#WeAreGlobal Section starts
class WeAreGlobal(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    img = models.ImageField(upload_to='global/')

#WeAreGlobal Section ends

#Why Us Section starts
class WhyUs(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class WUList(models.Model):
    why_us = models.ForeignKey(WhyUs, related_name='wu_list', on_delete=models.CASCADE)
    title = models.TextField()
    img = models.ImageField(upload_to='why_us/')
    desc = models.TextField()

#Why Us Section ends


#Accredition Section starts
class Accredition(models.Model):
    sec_title = models.TextField()
    img = models.ImageField(upload_to='accredition/')

#Accredition Section ends

#Implement Of IP Section starts
class ImplementOfIP(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()


class IOIPList(models.Model):
    implement_of_ip = models.ForeignKey(ImplementOfIP, related_name='ioip_list', on_delete=models.CASCADE)
    list_text = models.TextField()

#Implement Of IP Section ends


#Quality Policy Section starts
class QualityPolicy(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='quality_policy/')
    text_extra = models.TextField()

#Quality Policy Section ends


#Impartiality Policy Section starts
class ImpartialityPolicy(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

#Impartiality Policy Section ends
#About Us ________________________________________________________Models ends here________#


#__ Resource - Suspended Clients Page _____________________________________________________ starts here __#
#Suspended Clients Content and Meta Tags

class SuspendedClientsMeta(models.Model):
    title = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    author = models.TextField()
    robots = models.TextField()
    googlebot = models.TextField()
    language = models.TextField()
    google_site_verification = models.TextField()
    og_url = models.TextField()
    og_type = models.TextField()
    og_title = models.TextField()
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='og_images/')
    twitter_card = models.TextField()
    twitter_domain = models.TextField()
    twitter_url = models.TextField()
    twitter_title = models.TextField()
    twitter_desc = models.TextField()
    twitter_image = models.ImageField(upload_to='twitter_images/')

#SuspendedClients Content and Meta Tags

class SuspendedClients(models.Model):
    certification_number = models.TextField()
    company_name = models.TextField()
    scope = models.TextField()
    standard = models.TextField()

class SuspendedClientsPage(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()
    bgimg = models.ImageField(upload_to='suspended_clients_bg/')
    diagram = models.ImageField(upload_to='suspended_clients_diagram/')

#__ Resource - Suspended Clients Page _____________________________________________________ ends here __#


#__ Resource - Appeal Handling Page ___________________ Models __________________________________ starts here __#

#Appeal Handling Content and Meta Tags

class AppealHandlingMeta(models.Model):
    title = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    author = models.TextField()
    robots = models.TextField()
    googlebot = models.TextField()
    language = models.TextField()
    google_site_verification = models.TextField()
    og_url = models.TextField()
    og_type = models.TextField()
    og_title = models.TextField()
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='og_images/')
    twitter_card = models.TextField()
    twitter_domain = models.TextField()
    twitter_url = models.TextField()
    twitter_title = models.TextField()
    twitter_desc = models.TextField()
    twitter_image = models.ImageField(upload_to='twitter_images/')

#Appeal Handling Content and Meta Tags

class AppealHandling(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='appeal_handling/')

class AHList(models.Model):
    appeal_handling = models.ForeignKey(AppealHandling, related_name='ah_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class AppealHandlingPage(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()
    bgimg = models.ImageField(upload_to='appeal_handling_page_bg/')
    diagram = models.ImageField(upload_to='appeal_handling_page_diagram/')

#__ Resource - Appeal Handling Page ___________________ Models __________________________________ ends here __#



#__ Resource - ComplainHandling Page ___________________ Models __________________________________ starts here __#

class ComplainHandlingPage(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()
    bgimg = models.ImageField(upload_to='complain_handling_page_bg/')
    diagram = models.ImageField(upload_to='complain_handling_page_diagram/')

class CHList(models.Model):
    complain_handling = models.ForeignKey(ComplainHandlingPage, related_name='ch_list', on_delete=models.CASCADE)
    list_text = models.TextField()


class ComplainHandlingMeta(models.Model):
    title = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    author = models.TextField()
    robots = models.TextField()
    googlebot = models.TextField()
    language = models.TextField()
    google_site_verification = models.TextField()
    og_url = models.TextField()
    og_type = models.TextField()
    og_title = models.TextField()
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='og_images/')
    twitter_card = models.TextField()
    twitter_domain = models.TextField()
    twitter_url = models.TextField()
    twitter_title = models.TextField()
    twitter_desc = models.TextField()
    twitter_image = models.ImageField(upload_to='twitter_images/')

#__ Resource - ComplainHandling Page ___________________ Models __________________________________ ends here __#



#__ Resource - Grievances Page _____________________ Models ________________________________ starts here __#

class GrievancesPage(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()
    bgimg = models.ImageField(upload_to='grievances_page_bg/')
    diagram = models.ImageField(upload_to='grievances_page_diagram/')

class GrievancesList(models.Model):
    grievances = models.ForeignKey(GrievancesPage, related_name='grievances_list', on_delete=models.CASCADE)
    list_text = models.TextField()


class GrievancesMeta(models.Model):
    title = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    author = models.TextField()
    robots = models.TextField()
    googlebot = models.TextField()
    language = models.TextField()
    google_site_verification = models.TextField()
    og_url = models.TextField()
    og_type = models.TextField()
    og_title = models.TextField()
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='og_images/')
    twitter_card = models.TextField()
    twitter_domain = models.TextField()
    twitter_url = models.TextField()
    twitter_title = models.TextField()
    twitter_desc = models.TextField()
    twitter_image = models.ImageField(upload_to='twitter_images/')

#__ Resource - Grievances Page ____________________ Models _________________________________ ends here __#



#__ Resource - Certification  __________________ Models___________________________________ ends here __#

class CerificationProcessImg(models.Model):
    sec_title = models.TextField()
    mainImg = models.ImageField(upload_to='bg_images/')

class GrantOrRefuse(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class GOrRList(models.Model):
    grant_or_refuse = models.ForeignKey(GrantOrRefuse, related_name='gor_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class MaintainCertification(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class MCList(models.Model):
    maintain_certification = models.ForeignKey(MaintainCertification, related_name='mc_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class DetailsForIssuing(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class DFIList(models.Model):
    details_for_issuing = models.ForeignKey(DetailsForIssuing, related_name='dfi_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class WithdrawOfCertification(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class WOCList(models.Model):
    withdraw_of_certification = models.ForeignKey(WithdrawOfCertification, related_name='woc_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class SuspensionOfCertification(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class SOCList(models.Model):
    suspension_of_certification = models.ForeignKey(SuspensionOfCertification, related_name='soc_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class RestoringOfCertification(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class ROCList(models.Model):
    restoring_of_certification = models.ForeignKey(RestoringOfCertification, related_name='roc_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class ExpandingOrReducing(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()

class EORList(models.Model):
    expanding_or_reducing = models.ForeignKey(ExpandingOrReducing, related_name='eor_list', on_delete=models.CASCADE)
    list_text = models.TextField()

class CertificationProcessPage(models.Model):
    sec_title = models.TextField()
    sub_text = models.TextField()
    desc = models.TextField()
    BGimg = models.ImageField(upload_to='bg_images/')
    diagram = models.ImageField(upload_to='diagrams/')


class CertificationMeta(models.Model):
    title = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    author = models.TextField()
    robots = models.TextField()
    googlebot = models.TextField()
    language = models.TextField()
    google_site_verification = models.TextField()
    og_url = models.TextField()
    og_type = models.TextField()
    og_title = models.TextField()
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='og_images/')
    twitter_card = models.TextField()
    twitter_domain = models.TextField()
    twitter_url = models.TextField()
    twitter_title = models.TextField()
    twitter_desc = models.TextField()
    twitter_image = models.ImageField(upload_to='twitter_images/')
#__ Resource - Certification ______________________ Models _______________________________ ends here __#

# service page starts


class GrcMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class GrcSecOneList(models.Model):
    title = models.TextField()
    desc = models.TextField()
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.desc[:20]


class GrcSecOne(models.Model):
    section_title = models.TextField()
    paragraph_title = models.TextField(blank=True, null=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    grc_sec_one_list = models.ManyToManyField(GrcSecOneList, related_name='grc_sec_one_list')

    def __str__(self):
        return self.section_title


class GrcSecTwoList(models.Model):
    title = models.TextField()
    desc = models.TextField()
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.desc[:20]


class GrcSecTwo(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    grc_sec_two_list = models.ManyToManyField(GrcSecTwoList, related_name='grc_sec_two_list')

    def __str__(self):
        return self.section_title


class GrcSecThreeList(models.Model):
    title = models.TextField()
    desc = models.TextField()
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class GrcSecThree(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    grc_sec_three_list = models.ManyToManyField(GrcSecThreeList, related_name='grc_sec_three_list')

    def __str__(self):
        return self.section_title


class GrcSecFourList(models.Model):
    title = models.TextField()
    desc = models.TextField()
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class GrcSecFour(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    grc_sec_four_list = models.ManyToManyField(GrcSecFourList, related_name='grc_sec_four_list')

    def __str__(self):
        return self.section_title



class GrcSecFive(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.section_title


class GrcSecSixList(models.Model):
    title = models.TextField()
    desc = models.TextField()
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class GrcSecSixCategory(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    grc_sec_six_list = models.ManyToManyField(GrcSecSixList, related_name='grc_sec_six_list')

    def __str__(self):
        return self.title


class GrcSecSix(models.Model):
    section_title = models.TextField()
    paragraph_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    grc_sec_six_category = models.ManyToManyField(GrcSecSixCategory, related_name='grc_sec_six_category')

    def __str__(self):
        return self.section_title


class GrcSecSevenList(models.Model):
    title = models.TextField()
    desc = models.TextField()
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title




class GrcSecSeven(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='images/')
    grc_sec_seven_list = models.ManyToManyField(GrcSecSevenList, related_name='grc_sec_seven_list')

    def __str__(self):
        return self.section_title


class GrcSecEightList(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title


class GrcSecEight(models.Model):
    section_title = models.TextField()
    paragraph_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    grc_sec_eight_list = models.ManyToManyField(GrcSecEightList, related_name='grc_sec_eight_list')

    def __str__(self):
        return self.section_title


class GrcSubPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    grc_sec_one = models.ForeignKey(GrcSecOne, on_delete=models.CASCADE, related_name='grc_sec_one', blank= True, null=True)
    grc_sec_two = models.ForeignKey(GrcSecTwo, on_delete=models.CASCADE, related_name='grc_sec_two', blank= True, null=True)
    grc_sec_three = models.ForeignKey(GrcSecThree, on_delete=models.CASCADE, related_name='grc_sec_three', blank= True, null=True)
    grc_sec_four = models.ForeignKey(GrcSecFour, on_delete=models.CASCADE, related_name='grc_sec_four', blank= True, null=True)
    grc_sec_five = models.ForeignKey(GrcSecFive, on_delete=models.CASCADE, related_name='grc_sec_five', blank= True, null=True)
    grc_sec_six = models.ForeignKey(GrcSecSix, on_delete=models.CASCADE, related_name='grc_sec_six', blank= True, null=True)
    grc_sec_seven = models.ForeignKey(GrcSecSeven, on_delete=models.CASCADE, related_name='grc_sec_seven', blank= True, null=True)
    grc_sec_eight = models.ForeignKey(GrcSecEight, on_delete=models.CASCADE, related_name='grc_sec_eight', blank= True, null=True)
    grc_meta = models.ForeignKey(GrcMetaTag, on_delete=models.CASCADE, related_name='grc_meta', blank= True, null=True)


    def __str__(self):
        return self.section_title
    
# service page ends




# Management Training model starts

class ManagementTrnMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')


class ManagementTrnSecOneList(models.Model):
    list_text = models.TextField()

class ManagementTrnSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    paragraph = models.TextField( blank= True, null=True)
    sub_title = models.TextField( blank= True, null=True)
    sub_text = models.TextField( blank= True, null=True)
    trn_sec_one_list = models.ManyToManyField(ManagementTrnSecOneList, related_name='trn_sec_one_list')

    def __str__(self):
        return self.section_title


class ManagementTrnSecTwoList(models.Model):
    list_text = models.TextField()


class ManagementTrnSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    trn_sec_two_list = models.ManyToManyField(ManagementTrnSecTwoList, related_name='trn_sec_two_list')


class ManagementTrnSecThreeList(models.Model):
    list_text = models.TextField()


class ManagementTrnSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    trn_sec_three_list = models.ManyToManyField(ManagementTrnSecThreeList, related_name='trn_sec_three_list')



class ManagementTrnSecFourList(models.Model):
    list_text = models.TextField()


class ManagementTrnSecFour(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    trn_sec_four_list = models.ManyToManyField(ManagementTrnSecFourList, related_name='trn_sec_four_list')


class ManagementTrnSecFiveList(models.Model):
    title = models.TextField( null=True, blank=True)
    desc = models.TextField( null=True, blank=True)
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)


class ManagementTrnSecFiveCategory(models.Model):
    title = models.CharField(max_length=255, default="")
    img = models.ImageField(upload_to='images/')
    trn_sec_five_list = models.ManyToManyField(ManagementTrnSecFiveList, related_name='trn_sec_five_list')


class ManagementTrnSecFive(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    trn_sec_five_category = models.ManyToManyField(ManagementTrnSecFiveCategory, related_name='trn_sec_five_category')


class ManagementTrnSecSixList(models.Model):
    list_text = models.TextField(blank=True, null=True)


class ManagementTrnSecSix(models.Model):
    section_title = models.TextField()
    paragraph = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    trn_sec_six_list = models.ManyToManyField(ManagementTrnSecSixList, related_name='trn_sec_six_list')



class ManagementTrnSecSevenList(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=255)


class ManagementTrnSecSeven(models.Model):
    section_title = models.TextField()
    paragraph_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    trn_sec_seven_list = models.ManyToManyField(ManagementTrnSecSevenList, related_name='trn_sec_seven_list')



class ManagementTrnSubPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    trn_sec_one = models.ForeignKey(ManagementTrnSecOne, on_delete=models.CASCADE, related_name='trn_sec_one', blank=True, null=True)
    trn_sec_two = models.ForeignKey(ManagementTrnSecTwo, on_delete=models.CASCADE, related_name='trn_sec_two', blank=True, null=True)
    trn_sec_three = models.ForeignKey(ManagementTrnSecThree, on_delete=models.CASCADE, related_name='trn_sec_three', blank=True, null=True)
    trn_sec_four = models.ForeignKey(ManagementTrnSecFour, on_delete=models.CASCADE, related_name='trn_sec_four', blank=True, null=True)
    trn_sec_five = models.ForeignKey(ManagementTrnSecFive, on_delete=models.CASCADE, related_name='trn_sec_five', blank=True, null=True)
    trn_sec_six = models.ForeignKey(ManagementTrnSecSix, on_delete=models.CASCADE, related_name='trn_sec_six', blank=True, null=True)
    trn_sec_seven = models.ForeignKey(ManagementTrnSecSeven, on_delete=models.CASCADE, related_name='trn_sec_seven', blank=True, null=True)
    trn_meta = models.ForeignKey(ManagementTrnMetaTag, on_delete=models.CASCADE, related_name='trn_meta', blank=True, null=True)
    

# Management Training model Ends




#Professional Training model starts
 
class ProfessionalTrnMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return self.title
 
class ProfessionalTrnSecOneList(models.Model):
    list_text = models.TextField()
 
    def __str__(self):
        return self.list_text
 
class ProfessionalTrnSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    paragraph = models.TextField( blank= True, null=True)
    sub_title = models.TextField( blank= True, null=True)
    sub_text = models.TextField( blank= True, null=True)
    prf_trn_sec_one_list = models.ManyToManyField(ProfessionalTrnSecOneList, related_name='prf_trn_sec_one_list')
 
    def __str__(self):
        return self.section_title
 
 
class ProfessionalTrnSecTwoList(models.Model):
    list_text = models.TextField()
 
    def __str__(self):
        return self.list_text
 
 
class ProfessionalTrnSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    prf_trn_sec_two_list = models.ManyToManyField(ProfessionalTrnSecTwoList, related_name='prf_trn_sec_two_list')
 
    def __str__(self):
        return self.section_title
 
class ProfessionalTrnSecThreeList(models.Model):
    list_text = models.TextField()
 
    def __str__(self):
        return self.list_text
 
class ProfessionalTrnSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    prf_trn_sec_three_list = models.ManyToManyField(ProfessionalTrnSecThreeList, related_name='prf_trn_sec_three_list')
 
    def __str__(self):
        return self.section_title
 
class ProfessionalTrnSecFourList(models.Model):
    list_text = models.TextField()
   
    def __str__(self):
        return self.list_text
 
class ProfessionalTrnSecFour(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    prf_trn_sec_four_list = models.ManyToManyField(ProfessionalTrnSecFourList, related_name='prf_trn_sec_four_list')
 
    def __str__(self):
        return self.section_title
 
class ProfessionalTrnSecFiveList(models.Model):
    title = models.TextField( null=True, blank=True)
    desc = models.TextField( null=True, blank=True)
    imgfield = models.ImageField(upload_to='images/', null=True, blank=True)
       

class ProfessionalTrnSecFiveCategory(models.Model):
    title = models.CharField(max_length=255, default="")
    img = models.ImageField(upload_to='images/')
    prf_trn_sec_five_list = models.ManyToManyField(ProfessionalTrnSecFiveList, related_name='prf_trn_sec_five_list')
       
    def __str__(self):
        return self.title
 
class ProfessionalTrnSecFive(models.Model):
    section_title = models.TextField()
    sub_text = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField()
    level_heading = models.CharField(max_length=255, blank=True, null=True)
    prf_trn_sec_five_category = models.ManyToManyField(ProfessionalTrnSecFiveCategory, related_name='prf_trn_sec_five_category')
 
    def __str__(self):
        return self.section_title
 
class ProfessionalTrnSecSixList(models.Model):
    list_text = models.TextField()
     
    def __str__(self):
        return self.list_text
 
class ProfessionalTrnSecSix(models.Model):
    section_title = models.TextField()
    paragraph = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    prf_trn_sec_six_list = models.ManyToManyField(ProfessionalTrnSecSixList, related_name='prf_trn_sec_six_list')
     
    def __str__(self):
        return self.section_title


class ProfessionalTrnSecSevenList(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=255)


class ProfessionalTrnSecSeven(models.Model):
    section_title = models.TextField()
    paragraph_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    prf_trn_sec_seven_list = models.ManyToManyField(ProfessionalTrnSecSevenList, related_name='prf_trn_sec_seven_list')

   
 
class ProfessionalTrnSubPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    prf_trn_sec_one = models.ForeignKey(ProfessionalTrnSecOne, on_delete=models.CASCADE, related_name='prf_trn_sec_one', blank=True, null=True)
    prf_trn_sec_two = models.ForeignKey(ProfessionalTrnSecTwo, on_delete=models.CASCADE, related_name='prf_trn_sec_two', blank=True, null=True)
    prf_trn_sec_three = models.ForeignKey(ProfessionalTrnSecThree, on_delete=models.CASCADE, related_name='prf_trn_sec_three', blank=True, null=True)
    prf_trn_sec_four = models.ForeignKey(ProfessionalTrnSecFour, on_delete=models.CASCADE, related_name='prf_trn_sec_four', blank=True, null=True)
    prf_trn_sec_five = models.ForeignKey(ProfessionalTrnSecFive, on_delete=models.CASCADE, related_name='prf_trn_sec_five', blank=True, null=True)
    prf_trn_sec_six = models.ForeignKey(ProfessionalTrnSecSix, on_delete=models.CASCADE, related_name='prf_trn_sec_six', blank=True, null=True)
    prf_trn_sec_seven = models.ForeignKey(ProfessionalTrnSecSeven, on_delete=models.CASCADE, related_name='prf_trn_sec_seven', blank=True, null=True)
    prf_trn_meta = models.ForeignKey(ProfessionalTrnMetaTag, on_delete=models.CASCADE, related_name='prf_trn_meta', blank=True, null=True)
 
       
    def __str__(self):
        return self.section_title
 
    #Professional Training Model Ends


    #Audit Model starts

    
class AuditMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')


class AuditSecOneList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class AuditSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    audit_sec_one_list = models.ManyToManyField(AuditSecOneList, related_name='audit_sec_one_list')


class AuditSecTwoList(models.Model):
    list_title = models.TextField(blank=True, null=True)
    list_text = models.TextField()


class AuditSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    audit_sec_two_list = models.ManyToManyField(AuditSecTwoList, related_name='audit_sec_two_list')


class AuditSecThreeList(models.Model):
    list_text = models.TextField()


class AuditSecThree(models.Model):
    section_title = models.TextField()
    purpose = models.TextField(blank=True, null=True)
    desc = models.TextField()
    list_tile = models.TextField(blank=True, null=True)
    audit_sec_three_list = models.ManyToManyField(AuditSecThreeList, related_name='audit_sec_three_list')



class AuditSecFourList(models.Model):
    list_text = models.TextField()


class AuditSecFour(models.Model):
    section_title = models.TextField()
    purpose = models.TextField(blank=True, null=True)
    desc = models.TextField()
    list_tile = models.TextField(blank=True, null=True)
    audit_sec_four_list = models.ManyToManyField(AuditSecFourList, related_name='audit_sec_four_list')


class AuditSecFiveList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
    url = models.TextField()


class AuditSecFive(models.Model):
    section_title = models.TextField()
    purpose = models.TextField(blank=True, null=True)
    desc = models.TextField()
    list_tile = models.TextField(blank=True, null=True)
    audit_sec_five_list = models.ManyToManyField(AuditSecFiveList, related_name='audit_sec_five_list')


class AuditSecSixList(models.Model):
    list_text = models.TextField()


class AuditSecSix(models.Model):
    section_title = models.TextField()
    desc = models.TextField(),
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    audit_sec_six_list = models.ManyToManyField(AuditSecSixList, related_name='audit_sec_seven_list')


class AuditSecSevenList(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=255)


class AuditSecSeven(models.Model):
    section_title = models.TextField()
    paragraph_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    audit_sec_seven_list = models.ManyToManyField(AuditSecSevenList, related_name='audit_sec_seven_list')


class AuditSubPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    audit_sec_one = models.ForeignKey(AuditSecOne, on_delete=models.CASCADE, related_name='audit_sec_one', blank=True, null=True)
    audit_sec_two = models.ForeignKey(AuditSecTwo, on_delete=models.CASCADE, related_name='audit_sec_two', blank=True, null=True)
    audit_sec_three = models.ForeignKey(AuditSecThree, on_delete=models.CASCADE, related_name='audit_sec_three', blank=True, null=True)
    audit_sec_four = models.ForeignKey(AuditSecFour, on_delete=models.CASCADE, related_name='audit_sec_four', blank=True, null=True)
    audit_sec_five = models.ForeignKey(AuditSecFive, on_delete=models.CASCADE, related_name='audit_sec_five', blank=True, null=True)
    audit_sec_six = models.ForeignKey(AuditSecSix, on_delete=models.CASCADE, related_name='audit_sec_six', blank=True, null=True)
    audit_sec_seven = models.ForeignKey(AuditSecSeven, on_delete=models.CASCADE, related_name='audit_sec_seven', blank=True, null=True)
    audit_meta = models.ForeignKey(AuditMetaTag, on_delete=models.CASCADE, related_name='audit_meta', blank=True, null=True)
    
#Audit Model Ends


# Security Sub Service Model Starts

class StcMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')
 
 
class StcSecOne(models.Model):
    section_title = models.TextField()
    desc1 = models.TextField()
    desc2 = models.TextField(null=True, blank=True)
 
 
class StcSecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()
 
 
class StcSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    stc_sec_two_list = models.ManyToManyField(StcSecTwoList, related_name='stc_sec_two_list')
 
 
class StcSecThreeList(models.Model):
    list_text = models.TextField()
    desc = models.TextField()
 
 
class StcSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    stc_sec_three_list = models.ManyToManyField(StcSecThreeList, related_name='stc_sec_three_list')
 
 
 
class StcSecFourList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
 
 
class StcSecFour(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    stc_sec_four_list = models.ManyToManyField(StcSecFourList, related_name='stc_sec_four_list')
 
 
class StcSecFiveList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
 
 
class StcSecFive(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    stc_sec_five_list = models.ManyToManyField(StcSecFiveList, related_name='stc_sec_five_list')
 
 
 
class StcSecSixList(models.Model):
    list_text = models.TextField()
    desc = models.TextField()
 
 
class StcSecSix(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    stc_sec_six_list = models.ManyToManyField(StcSecSixList, related_name='stc_sec_six_list')
 
 
 
class StcSecSevenList(models.Model):
    list_text = models.TextField()
    desc = models.TextField()
 
 
class StcSecSeven(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    stc_sec_seven_list = models.ManyToManyField(StcSecSevenList, related_name='stc_sec_seven_list')
 
 
class StcSecEightList(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=255)
 
 
class StcSecEight(models.Model):
    section_title = models.TextField()
    paragraph_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    stc_sec_eight_list = models.ManyToManyField(StcSecEightList, related_name='stc_sec_eight_list')



class StcSecNineList(models.Model):
    list_title = models.TextField(null=True, blank=True)
    list_text = models.TextField(null=True, blank=True)


class StcSecNine(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    stc_sec_nine_list = models.ManyToManyField(StcSecNineList, related_name='stc_sec_nine_list')
 
 
 
 
class StcSubPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    stc_sec_one = models.ForeignKey(StcSecOne, on_delete=models.CASCADE, related_name='stc_sec_one', blank=True, null=True)
    stc_sec_two = models.ForeignKey(StcSecTwo, on_delete=models.CASCADE, related_name='stc_sec_two', blank=True, null=True)
    stc_sec_three = models.ForeignKey(StcSecThree, on_delete=models.CASCADE, related_name='stc_sec_three', blank=True, null=True)
    stc_sec_four = models.ForeignKey(StcSecFour, on_delete=models.CASCADE, related_name='stc_sec_four', blank=True, null=True)
    stc_sec_five = models.ForeignKey(StcSecFive, on_delete=models.CASCADE, related_name='stc_sec_five', blank=True, null=True)
    stc_sec_six = models.ForeignKey(StcSecSix, on_delete=models.CASCADE, related_name='stc_sec_six', blank=True, null=True)
    stc_sec_seven = models.ForeignKey(StcSecSeven, on_delete=models.CASCADE, related_name='stc_sec_seven', blank=True, null=True)
    stc_sec_eight = models.ForeignKey(StcSecEight, on_delete=models.CASCADE, related_name='stc_sec_eight', blank=True, null=True)
    stc_sec_nine = models.ForeignKey(StcSecNine, on_delete=models.CASCADE, related_name='stc_sec_nine', blank=True, null=True)
    stc_meta = models.ForeignKey(StcMetaTag, on_delete=models.CASCADE, related_name='stc_meta', blank=True, null=True)
    

    #Security Sub Service Ends here


    #Grc Main Page Model Start

    
class GrcMainMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')




class GrcMainSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    subDesc = models.TextField(blank=True, null=True)


class GrcMainSecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class GrcMainSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    grcmain_sec_two_list = models.ManyToManyField(GrcMainSecTwoList, related_name='grcmain_sec_two_list')


class GrcMainSecThreeList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class GrcMainSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    grcmain_sec_three_list = models.ManyToManyField(GrcMainSecThreeList, related_name='grcmain_sec_three_list')



class GrcMainSecFourList(models.Model):
    title = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)


class GrcMainSecFourCategory(models.Model):
    title = models.CharField(max_length=255)
    grcmain_sec_four_list = models.ManyToManyField(GrcMainSecFourList, related_name='grcmain_sec_four_list')


class GrcMainSecFour(models.Model):
    section_title = models.TextField(blank=True, null=True)
    paragraph_title = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    grcmain_sec_four_category = models.ManyToManyField(GrcMainSecFourCategory, related_name='grcmain_sec_four_category')


class GrcMainSecFiveList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
    url = models.TextField()


class GrcMainSecFive(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    grcmain_sec_five_list = models.ManyToManyField(GrcMainSecFiveList, related_name='grcmain_sec_five_list')


class GrcMainPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    grcmain_sec_one = models.ForeignKey(GrcMainSecOne, on_delete=models.CASCADE, related_name='grcmain_sec_one', blank=True, null=True)
    grcmain_sec_two = models.ForeignKey(GrcMainSecTwo, on_delete=models.CASCADE, related_name='grcmain_sec_two', blank=True, null=True)
    grcmain_sec_three = models.ForeignKey(GrcMainSecThree, on_delete=models.CASCADE, related_name='grcmain_sec_three', blank=True, null=True)
    grcmain_sec_four = models.ForeignKey(GrcMainSecFour, on_delete=models.CASCADE, related_name='grcmain_sec_four', blank=True, null=True)
    grcmain_sec_five = models.ForeignKey(GrcMainSecFive, on_delete=models.CASCADE, related_name='grcmain_sec_five', blank=True, null=True)
    grcmain_meta = models.ForeignKey(GrcMainMetaTag, on_delete=models.CASCADE, related_name='grcmain_meta', blank=True, null=True)
    

    #Grc Main Page Model Ends



    #Audit Main Page Model Start


class AuditMainMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')




class AuditMainSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    desc = models.TextField()


class AuditMainSecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class AuditMainSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    auditmain_sec_two_list = models.ManyToManyField(AuditMainSecTwoList, related_name='auditmain_sec_two_list')


class AuditMainSecThreeList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
    url = models.TextField()


class AuditMainSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    auditmain_sec_three_list = models.ManyToManyField(AuditMainSecThreeList, related_name='auditmain_sec_three_list')


class AuditMainPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    auditmain_sec_one = models.ForeignKey(AuditMainSecOne, on_delete=models.CASCADE, related_name='auditmain_sec_one', blank=True, null=True)
    auditmain_sec_two = models.ForeignKey(AuditMainSecTwo, on_delete=models.CASCADE, related_name='auditmain_sec_two', blank=True, null=True)
    auditmain_sec_three = models.ForeignKey(AuditMainSecThree, on_delete=models.CASCADE, related_name='auditmain_sec_three', blank=True, null=True)
    auditmain_meta = models.ForeignKey(AuditMainMetaTag, on_delete=models.CASCADE, related_name='auditmain_meta', blank=True, null=True)
    


    #Audit Main Page Model Ends


    #Training Main Page Model Starts

    
class TrnMainMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')




class TrnMainSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    desc = models.TextField()


class TrnMainSecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)


class TrnMainSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    trnmain_sec_two_list = models.ManyToManyField(TrnMainSecTwoList, related_name='trnmain_sec_two_list')


class TrnMainSecThreeList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class TrnMainSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    trnmain_sec_three_list = models.ManyToManyField(TrnMainSecThreeList, related_name='trnmain_sec_three_list')


class TrnMainSecFourList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
    url = models.TextField()


class TrnMainSecFour(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    trnmain_sec_four_list = models.ManyToManyField(TrnMainSecFourList, related_name='trnmain_sec_four_list')


class TrnMainPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    trnmain_sec_one = models.ForeignKey(TrnMainSecOne, on_delete=models.CASCADE, related_name='trnmain_sec_one', blank=True, null=True)
    trnmain_sec_two = models.ForeignKey(TrnMainSecTwo, on_delete=models.CASCADE, related_name='trnmain_sec_two', blank=True, null=True)
    trnmain_sec_three = models.ForeignKey(TrnMainSecThree, on_delete=models.CASCADE, related_name='trnmain_sec_three', blank=True, null=True)
    trnmain_sec_four = models.ForeignKey(TrnMainSecFour, on_delete=models.CASCADE, related_name='trnmain_sec_four', blank=True, null=True)
    trnmain_meta = models.ForeignKey(TrnMainMetaTag, on_delete=models.CASCADE, related_name='trnmain_meta', blank=True, null=True)


    #Training Main Page Ends



# Contact Detail APi

class ContactDetail(models.Model):
    branch_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location_map = models.TextField()

    def __str__(self):
        return self.branch_name


# Management system main training Starts




class MstMainMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')




class MstMainSecOneList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class MstMainSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    desc = models.TextField()
    mstmain_sec_one_list = models.ManyToManyField(MstMainSecOneList, related_name='mstmain_sec_one_list')


class MstMainSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)


class MstMainSecThreeList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class MstMainSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    mstmain_sec_three_list = models.ManyToManyField(MstMainSecThreeList, related_name='mstmain_sec_three_list')

class MstMainSecFourList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)


class MstMainSecFour(models.Model):
    section_title = models.TextField()
    mstmain_sec_four_list = models.ManyToManyField(MstMainSecFourList, related_name='mstmain_sec_four_list')


class MstMainSecFiveList(models.Model):
    list_text = models.TextField()


class MstMainSecFive(models.Model):
    section_title = models.TextField()
    mstmain_sec_five_list = models.ManyToManyField(MstMainSecFiveList, related_name='mstmain_sec_five_list')


class MstMainSecSixList(models.Model):
    list_text = models.TextField()
    


class MstMainSecSix(models.Model):
    section_title = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    mstmain_sec_six_list = models.ManyToManyField(MstMainSecSixList, related_name='mstmain_sec_six_list')


class MstMainSecSevenList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
    url = models.TextField()


class MstMainSecSeven(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    mstmain_sec_seven_list = models.ManyToManyField(MstMainSecSevenList, related_name='mstmain_sec_seven_list')


class MstMainPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    mstmain_sec_one = models.ForeignKey(MstMainSecOne, on_delete=models.CASCADE, related_name='mstmain_sec_one', blank=True, null=True)
    mstmain_sec_two = models.ForeignKey(MstMainSecTwo, on_delete=models.CASCADE, related_name='mstmain_sec_two', blank=True, null=True)
    mstmain_sec_three = models.ForeignKey(MstMainSecThree, on_delete=models.CASCADE, related_name='mstmain_sec_three', blank=True, null=True)
    mstmain_sec_four = models.ForeignKey(MstMainSecFour, on_delete=models.CASCADE, related_name='mstmain_sec_four', blank=True, null=True)
    mstmain_sec_five = models.ForeignKey(MstMainSecFive, on_delete=models.CASCADE, related_name='mstmain_sec_five', blank=True, null=True)
    mstmain_sec_six = models.ForeignKey(MstMainSecSix, on_delete=models.CASCADE, related_name='mstmain_sec_six', blank=True, null=True)
    mstmain_sec_seven = models.ForeignKey(MstMainSecSeven, on_delete=models.CASCADE, related_name='mstmain_sec_seven', blank=True, null=True)
    mstmain_meta = models.ForeignKey(MstMainMetaTag, on_delete=models.CASCADE, related_name='mstmain_meta', blank=True, null=True)


# Management system main training Ends


#professional main training starts

class PtrnMainMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')

class PtrnMainSecOne(models.Model):
    section_title = models.TextField()
    section_sub_title = models.TextField()
    desc1 = models.TextField()
    desc2 = models.TextField()


class PtrnMainSecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class PtrnMainSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    ptrnmain_sec_two_list = models.ManyToManyField(PtrnMainSecTwoList, related_name='ptrnmain_sec_two_list')


class PtrnMainSecThreeList(models.Model):
    list_title = models.TextField(null=True, blank=True)
    list_text = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)

class PtrnMainSecThree(models.Model):
    section_title = models.TextField()
    ptrnmain_sec_three_list = models.ManyToManyField(PtrnMainSecThreeList, related_name='ptrnmain_sec_three_list')




class PtrnMainSecFourList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
    url = models.TextField()


class PtrnMainSecFour(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    ptrnmain_sec_four_list = models.ManyToManyField(PtrnMainSecFourList, related_name='ptrnmain_sec_four_list')


class PtrnMainPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    ptrnmain_sec_one = models.ForeignKey(PtrnMainSecOne, on_delete=models.CASCADE, related_name='ptrnmain_sec_one', blank=True, null=True)
    ptrnmain_sec_two = models.ForeignKey(PtrnMainSecTwo, on_delete=models.CASCADE, related_name='ptrnmain_sec_two', blank=True, null=True)
    ptrnmain_sec_three = models.ForeignKey(PtrnMainSecThree, on_delete=models.CASCADE, related_name='ptrnmain_sec_three', blank=True, null=True)
    ptrnmain_sec_four = models.ForeignKey(PtrnMainSecFour, on_delete=models.CASCADE, related_name='ptrnmain_sec_four', blank=True, null=True)
    ptrnmain_meta = models.ForeignKey(PtrnMainMetaTag, on_delete=models.CASCADE, related_name='ptrnmain_meta', blank=True, null=True)


#professional main training ends

#security testing system main page

class StcMainMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')



class StcMainSecOneList(models.Model):
    list_desc = models.TextField()


class StcMainSecOne(models.Model):
    section_title = models.TextField()
    stcmain_sec_one_list = models.ManyToManyField(StcMainSecOneList, related_name='stcmain_sec_one_list')


class StcMainSecTwoList(models.Model):
    list_title = models.TextField()
    list_desc = models.TextField()


class StcMainSecTwo(models.Model):
    section_title = models.TextField()
    stcmain_sec_two_list = models.ManyToManyField(StcMainSecTwoList, related_name='stcmain_sec_two_list')


class StcMainSecThreeList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class StcMainSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    stcmain_sec_three_list = models.ManyToManyField(StcMainSecThreeList, related_name='stcmain_sec_three_list')



class StcMainSecFourList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class StcMainSecFour(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    stcmain_sec_four_list = models.ManyToManyField(StcMainSecFourList, related_name='stcmain_sec_four_list')


class StcMainSecFiveList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class StcMainSecFive(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    stcmain_sec_five_list = models.ManyToManyField(StcMainSecFiveList, related_name='stcmain_sec_five_list')


class StcMainSecSixList(models.Model):
    list_text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField()
    url = models.TextField()


class StcMainSecSix(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    stcmain_sec_six_list = models.ManyToManyField(StcMainSecSixList, related_name='stcmain_sec_six_list')


class StcMainPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    stcmain_sec_one = models.ForeignKey(StcMainSecOne, on_delete=models.CASCADE, related_name='stcmain_sec_one', blank=True, null=True)
    stcmain_sec_two = models.ForeignKey(StcMainSecTwo, on_delete=models.CASCADE, related_name='stcmain_sec_two', blank=True, null=True)
    stcmain_sec_three = models.ForeignKey(StcMainSecThree, on_delete=models.CASCADE, related_name='stcmain_sec_three', blank=True, null=True)
    stcmain_sec_four = models.ForeignKey(StcMainSecFour, on_delete=models.CASCADE, related_name='stcmain_sec_four', blank=True, null=True)
    stcmain_sec_five = models.ForeignKey(StcMainSecFive, on_delete=models.CASCADE, related_name='stcmain_sec_five', blank=True, null=True)
    stcmain_sec_six = models.ForeignKey(StcMainSecSix, on_delete=models.CASCADE, related_name='stcmain_sec_six', blank=True, null=True)
    stcmain_meta = models.ForeignKey(StcMainMetaTag, on_delete=models.CASCADE, related_name='stcmain_meta', blank=True, null=True)


#security testing and compliance ends  



class ContactForm(models.Model):
    f_name = models.CharField(max_length=100, blank=False, null=False)
    l_name = models.CharField(max_length=100, blank=False, null=False)
    phone =  models.PositiveIntegerField(blank=False, null=False)
    email =  models.EmailField(max_length=200, blank=False, null=False)
    message =  models.TextField( blank=False, null=False)
    
    def __str__(self):
        return self.f_name


class CareerForm(models.Model):
    file= models.FileField(upload_to= 'uploads/', blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone =  models.PositiveIntegerField(blank=False, null=False)
    email =  models.EmailField(max_length=200, blank=False, null=False)
    address =  models.TextField( blank=False, null=False)
    residentaddress1 =  models.TextField( blank=False, null=False)
    residentaddress2 = models.TextField( blank=False, null=False)
    job_title = models.CharField(max_length=100, blank=False, null=False)
    qualification = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.first_name


class CareerPageMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return self.title
 
class CareerPageSecOne(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
 
    def __str__(self):
        return self.section_title
 
 
class CareerPageSecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField(blank=True, null=True)
    url = models.TextField()
 
    def __str__(self):
        return self.list_title
 
 
class CareerPageSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    careerpage_sec_two_list = models.ManyToManyField(CareerPageSecTwoList, related_name='careerpage_sec_two_list')
 
    def __str__(self):
        return self.section_title
 
class CareerPagePage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    careerpage_sec_one = models.ForeignKey(CareerPageSecOne, on_delete=models.CASCADE, related_name='careerpage_sec_one', blank=True, null=True)
    careerpage_sec_two = models.ForeignKey(CareerPageSecTwo, on_delete=models.CASCADE, related_name='careerpage_sec_two', blank=True, null=True)
    careerpage_meta = models.ForeignKey(CareerPageMetaTag, on_delete=models.CASCADE, related_name='careerpage_meta', blank=True, null=True)
   
    def __str__(self):
        return self.section_title
 
 
class PrivacyPolicyMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return self.title
 
class PrivacyPolicySecOne(models.Model):
    paragraph_desc = models.TextField(null=True, blank=True)
    section_title = models.TextField()
    desc = models.TextField()
 
    def __str__(self):
        return self.section_title
   
class PrivacyPolicySecTwoSubList(models.Model):
    sublist_title = models.TextField()
    sublist_text = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.sublist_title
 
class PrivacyPolicySecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField(blank=True, null=True)
    subList = models.ManyToManyField(PrivacyPolicySecTwoSubList, related_name='sublists', blank=True, null=True)
 
    def __str__(self):
        return self.list_title
 
class PrivacyPolicySecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    desc = models.TextField()
    prpolicy_sec_two_list = models.ManyToManyField(PrivacyPolicySecTwoList, related_name='prpolicy_sec_two_list')
 
    def __str__(self):
        return self.section_title
 
class PrivacyPolicySecThreeList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()
 
    def __str__(self):
        return self.list_title
 
class PrivacyPolicySecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    prpolicy_sec_three_list = models.ManyToManyField(PrivacyPolicySecThreeList, related_name='prpolicy_sec_three_list')
 
    def __str__(self):
        return self.section_title
   
class PrivacyPolicyPage(models.Model):
    section_title = models.CharField(max_length=255)
    desc = models.TextField()
    lp_title = models.CharField(max_length=255)
    desc = models.TextField()
    url_string = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    prpolicy_sec_one = models.ForeignKey(PrivacyPolicySecOne, on_delete=models.CASCADE, related_name='prpolicy_sec_one', blank=True, null=True)
    prpolicy_sec_two = models.ForeignKey(PrivacyPolicySecTwo, on_delete=models.CASCADE, related_name='prpolicy_sec_two', blank=True, null=True)
    prpolicy_sec_three = models.ForeignKey(PrivacyPolicySecThree, on_delete=models.CASCADE, related_name='prpolicy_sec_three', blank=True, null=True)
    prpolicy_meta = models.ForeignKey(PrivacyPolicyMetaTag, on_delete=models.CASCADE, related_name='prpolicy_meta', blank=True, null=True)
   
    def __str__(self):
        return self.section_title


class BlogMetaTag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    googlebot = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    google_site_verification = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_type = models.CharField(max_length=50)
    og_title = models.CharField(max_length=255)
    og_desc = models.TextField()
    og_image = models.ImageField(upload_to='images/')
    twitter_card = models.CharField(max_length=50)
    twitter_domain = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    twitter_title = models.CharField(max_length=255)
    twitter_description = models.TextField()
    twitter_image = models.ImageField(upload_to='images/')


class BlogSecOneList(models.Model):
    list_title = models.TextField(blank=True, null=True)
    list_text = models.TextField()


class BlogSecOne(models.Model):
    section_title = models.TextField(blank=True, null=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    blog_sec_one_list = models.ManyToManyField(BlogSecOneList, related_name='blog_sec_one_list')


class BlogSecTwoList(models.Model):
    list_title = models.TextField()
    list_text = models.TextField()


class BlogSecTwo(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    blog_sec_two_list = models.ManyToManyField(BlogSecTwoList, related_name='blog_sec_two_list')


class BlogSecThreeList(models.Model):
    list_title = models.TextField(blank=True, null=True)
    list_text = models.TextField()


class BlogSecThree(models.Model):
    section_title = models.TextField()
    desc = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    blog_sec_three_list = models.ManyToManyField(BlogSecThreeList, related_name='blog_sec_three_list')


class BlogSecFourList(models.Model):
    list_title = models.TextField(blank=True, null=True)
    list_text = models.TextField(blank=True, null=True)


class BlogSecFour(models.Model):
    section_title = models.TextField()
    desc = models.TextField()
    pragraph = models.TextField(blank=True, null=True)
    blog_sec_four_list = models.ManyToManyField(BlogSecFourList, related_name='blog_sec_four_list',blank=True, null=True)

class BlogCtg(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    # desc = HTMLField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    blog_image = models.ImageField(default="400-200.png")
    date = models.DateField(null=True, blank=True)
    blog_sec_one = models.ForeignKey(BlogSecOne, on_delete=models.CASCADE, related_name='blog_sec_one', blank=True, null=True)
    blog_sec_two = models.ForeignKey(BlogSecTwo, on_delete=models.CASCADE, related_name='blog_sec_two', blank=True, null=True)
    blog_sec_three = models.ForeignKey(BlogSecThree, on_delete=models.CASCADE, related_name='blog_sec_three', blank=True, null=True)
    blog_sec_four = models.ForeignKey(BlogSecFour, on_delete=models.CASCADE, related_name='blog_sec_four', blank=True, null=True)
    blog_meta = models.ForeignKey(BlogMetaTag, on_delete=models.CASCADE, related_name='grcmain_meta', blank=True, null=True)
    blog_ctg = models.ForeignKey(BlogCtg, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title


class CustomerFeedbackForm(models.Model):
    company_name = models.CharField(max_length=255, blank=False, null=False)
    contact_name = models.CharField(max_length=255, blank=False, null=False)
    address =  models.TextField(blank=True, null=True)
    email =  models.EmailField(max_length=255, blank=True, null=True)
    phone =  models.PositiveIntegerField(blank=True, null=True)
    date =  models.DateField(blank=True, null=True)
    audit_standard =  models.CharField(max_length=255, blank=True, null=True)
    company_activities = models.CharField(max_length=255,blank=True, null=True)
    audit_type = models.CharField(max_length=255, blank=True, null=True)
    lead_auditor_name = models.CharField(max_length=255, blank=True, null=True)
    other_audit_team_name = models.CharField(max_length=255, blank=True, null=True)
    feedback_audit_team = models.TextField(blank=True, null=True)
    feedback_for_intercert = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return self.company_name