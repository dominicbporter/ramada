from django.urls import path
from web.views import index, auckland, albany, christchurch, orewa, queenstown, rotorua, taipa, wanaka

urlpatterns = [
    path('', index.index_view, name='index'),
    path('auckland/', auckland.page_view, name='auckland'),
    path('auckland/studio/', auckland.std_view, name='akl_std'),
    path('auckland/exstudio/', auckland.xstd_view, name='akl_xstd'),
    path('auckland/onebd', auckland.onebd_view, name='akl_1bd'),
    path('auckland/pent', auckland.pent_view, name='akl_pent'),
    path('albany/', albany.page_view, name='albany'),
    path('christchurch/', christchurch.page_view, name='christchurch'),
    path('christchurch/studio/', christchurch.std_view, name='chch_std'),
    path('christchurch/onebedroom', christchurch.onebd_view, name='chch_1bd'),
    path('christchurch/twobedroom', christchurch.twobd_view, name='chch_2bd'),
    path('orewa/', orewa.page_view, name='orewa'),
    path('queenstown/', queenstown.page_view, name='queenstown'),
    path('queenstown/studio', queenstown.std_view, name='qtwn_std'),
    path('queenstown/exstudio', queenstown.xstd_view, name='qtwn_xstd'),
    path('queenstown/onebedroom', queenstown.onebd_view, name='qtwn_1bd'),
    path('queenstown/twobedroom', queenstown.twobd_view, name='qtwn_2bd'),
    path('queenstown/threebedroom', queenstown.threebd_view, name='qtwn_3bd'),
    path('queenstown/loft', queenstown.loft_view, name='qtwn_loft'),
    path('rotorua/', rotorua.page_view, name='rotorua'),
    path('taipa/', taipa.page_view, name='taipa'),
    path('wanaka/', wanaka.page_view, name='wanaka'),

]
