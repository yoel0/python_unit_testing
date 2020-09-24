import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
  """Test for Employee class"""

  @classmethod
  def setUpClass(cls):
    print('setUpClass')
  
  def setUp(self):
    print('setUp')
    self.levin = Employee('Levin', 'Batallones', 2000000)
    self.adam = Employee('Adam', 'Honore', 9999999)
    self.bell = Employee('Bell', 'Cranel', 100000)
    self.albert = Employee('Albert', 'Biton', 200000)

  def tearDown(self):
    print('tearDown\n')

  def test_email(self):
    self.assertEqual(self.levin.email, 'levin.batallones@sei713.com')
    self.assertEqual(self.adam.email, 'adam.honore@sei713.com')
    self.assertEqual(self.bell.email, 'bell.cranel@sei713.com')
    self.assertEqual(self.albert.email, 'albert.biton@sei713.com')

  def test_fullname(self):

    self.assertEqual(self.bell.fullname, 'Bell Cranel')
    self.assertEqual(self.albert.fullname, 'Albert Biton')

  def test_raise_amount(self):

    self.bell.apply_raise()
    self.albert.apply_raise()

    self.assertEqual(self.bell.pay, 115000)
    self.assertEqual(self.albert.pay, 230000)

if __name__ == '__main__':
  unittest.main()
