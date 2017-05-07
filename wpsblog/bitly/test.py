from django.test import TestCase
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from bitly.models import Bitlink


class BitlinkModelTestCase(TestCase):

    def test_bitly_should_have_shorten_hash(self):
        # create test user
        test_username = "test_username"
        test_password = "test_password"
        
        user = User.objects.create_user(
            username=test_username,
            password=test_password,
        )
        
        # create test bitlink
        for i in range(100):
            test_original_url = "http://www.example-{i}.com".format(i=i)
            bitlink = Bitlink.objects.create(
                user=user,
                original_url=test_original_url,
            )

            self.assertTrue(
                bitlink.shorten_hash,
            )
