import  unittest


class Testclass(unittest.TestCase):
    def setUp(self):
        """
        Method called to prepare the test fixture.
        This is called immediately before calling the test method
        :return:
        """
        print("Setup Method Called")

    def tearDown(self):
        """
        Method called immediately after the test method has been called and the result recorded.
        :return:
        """
        print("Tear Down Method Called")

    @unittest.skip('inprogress')
    def test_isupper(self):
        a = input("Enter you name")
        self.assertTrue(a.isupper())
        self.assertFalse('foo'.isupper())


if __name__ == "_main_":
    unittest.main()