from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Entry
from api import views
from django.contrib.auth.models import User

class EntryTests(APITestCase):
    def post_entry(self, name, city, school):
        url = reverse(views.EntryList.name)
        data = {
            'name': name,
            'city': city,
            'school': school,
        }
        response = self.client.post(url, data, format='json')
        return response

    def create_superuser_and_login(self):
        username = 'admin'
        password = '666666'
        email = '666666@qq.com'
        user = User.objects.create_superuser(username=username, password=password, email=email)
        login = self.client.login(username=username, password=password)
        self.assertTrue(login)

    def logout_user(self):
        self.client.logout()


    def test_post_and_get_entry(self):
        self.create_superuser_and_login()
        new_entry_name = 'kk'
        new_entry_city = '珠海市'
        new_entry_school = '暨南大学'
        response = self.post_entry(new_entry_name,new_entry_city,new_entry_school)
        assert response.status_code == status.HTTP_201_CREATED
        assert Entry.objects.count() == 1
        assert Entry.objects.get().name == new_entry_name
        self.logout_user()

    def test_post_entry_without_login(self):
        new_entry_name = 'kk'
        new_entry_city = '珠海市'
        new_entry_school = '暨南大学'
        response = self.post_entry(new_entry_name,new_entry_city,new_entry_school)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_filter_by_name(self):
        new_entry_name1 = 'asjlkviwejlkj'
        new_entry_city1 = '珠海市'
        new_entry_school1 = '暨南大学'
        new_entry_name2 = 'asjlkviwejlkj23'
        new_entry_city2 = '珠海市'
        new_entry_school2 = '暨南大学'
        self.create_superuser_and_login()
        self.post_entry(name=new_entry_name1,city=new_entry_city1,school=new_entry_school1)
        self.post_entry(name=new_entry_name2,city=new_entry_city2,school=new_entry_school2)
        filter_by_name = {'name': new_entry_name1}
        url = '{0}?{1}'.format(reverse(views.EntryList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_entry_name1

    def test_patch_entry_detail(self):
        self.create_superuser_and_login()
        new_entry_name = 'kk'
        new_entry_city = '珠海市'
        new_entry_school = '暨南大学'
        update_entry_name = 'kk1'
        response = self.post_entry(new_entry_name,new_entry_city,new_entry_school)
        url = response.data['url']

        detail_response = self.client.get(url)
        print(detail_response)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data['name'] == new_entry_name

        data = {
            'name': update_entry_name
        }
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == update_entry_name
        self.logout_user()

    def test_throttle_validation(self):
        count = 150
        url = reverse(views.EntryList.name)
        for i in range(count):
            self.client.get(url)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

        for i in range(count+50):
            self.client.get(url)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS


