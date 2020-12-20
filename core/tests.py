from django.test import TestCase
from core.distribution import distribute, SecretSantaDistributionException


class DistributionTestClass(TestCase):
    def test_empty_arguments(self):
        try:
            distribute({})
            self.fail("Provided empty dict should raise an exception")
        except SecretSantaDistributionException:
            pass

    def test_singleton_dict_provided(self):
        wishes = {'Anna': 'ball'}
        try:
            distribute(wishes)
            self.fail("Provided singleton dict should raise an exception")
        except SecretSantaDistributionException:
            pass

    def test_correct_two_arguments(self):
        wishes = {'Anna': 'ball', 'Helen': 'dall'}
        expected_result = {'Anna': ('Helen', 'dall'), 'Helen': ('Anna', 'ball')}
        attempts = 100
        correct_results = 0
        for i in range(attempts):
            result_dict = distribute(wishes)
            if result_dict == expected_result:
                correct_results += 1
            self.assertEquals(expected_result, result_dict)
        self.assertEquals(attempts, correct_results)

    def test_correct_three_arguments(self):
        wishes = {'Anna': 'ball', 'Helen': 'dall', 'Bob': 'car'}
        attempts = 100
        correct_results = 0
        for i in range(attempts):
            try:
                results = distribute(wishes)
                for k, v in enumerate(results):
                    if v is None or k == v[0]:
                        self.fail("Incorrect distribution")
            except IndexError:
                self.fail("Incorrect distribution, no available people left")
            correct_results += 1
        self.assertEquals(attempts, correct_results)
