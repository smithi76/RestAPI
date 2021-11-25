# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from emploapp.views import Studentlist, GenericempListCreate, Studlist, Empupdate
#
# class TestUrls(SimpleTestCase):
#     def test_stude_list_url_is_resloved(self):
#         url = reverse('stude-list')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func.view_class, Studentlist)
#
#     def test_genericemp_list_url_is_resloved(self):
#         url = reverse('generic-emplist')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func.view_class, GenericempListCreate)
#
#     def test_stud_list_url_is_resloved(self):
#         url = reverse('stud-list')
#         self.assertEquals(resolve(url).func, Studlist)
#
#     # def test_empupdt_list_url_is_resloved(self):
#     #     url = reverse('emp-update', args=[''])
#     #     self.assertEquals(resolve(url).func.view_class, Empupdate)