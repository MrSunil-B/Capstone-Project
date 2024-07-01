import unittest
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(unittest.TestCase):

    def setUp(self):
        # Create test instances of the Menu model
        self.menu1 = Menu.objects.create(Title="Hog", Price="30", Inventory=100)
        self.menu2 = Menu.objects.create(Title="Dog", Price="20", Inventory=1001)
        self.menu3 = Menu.objects.create(Title="Kong", Price="10",Inventory=200)

    def test_getall(self):
        # Retrieve all Menu objects
        menus = Menu.objects.all()
        # Serialize the retrieved objects
        serializer = MenuSerializer(menus, many=True)
        # Expected serialized data
        expected_data = [
            {'Title': 'Hog', 'Price': '30', 'Inventory': '100'},
            {'Title': 'Dog', 'Price': '20', 'Inventory': '1001'},
            {'Title': 'Kong', 'Price': '10', 'Inventory': '200'}
        ]
        # Run assertions to check if the serialized data equals the response
        self.assertEqual(serializer.data, expected_data)

if __name__ == '__main__':
    unittest.main()
