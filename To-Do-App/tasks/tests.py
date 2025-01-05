from django.test import TestCase
from .models import todo  # Import the correct model name
from django.contrib.auth.models import User


class TodoTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    # Test Case 1: Task Creation
    def test_todo_creation(self):
        task = todo.objects.create(user=self.user, todo_name='Sample Task')
        self.assertEqual(task.todo_name, 'Sample Task')  # Check if task is created correctly

    # Test Case 2: Status Default Value
    def test_default_status(self):
        task = todo.objects.create(user=self.user, todo_name='New Task')
        self.assertFalse(task.status)  # Check if default status is False

    # Test Case 3: Update Task Status
    def test_update_status(self):
        task = todo.objects.create(user=self.user, todo_name='Test Update')
        task.status = True
        task.save()
        self.assertTrue(task.status)  # Check if status is updated to True

    # Test Case 4: String Representation
    def test_string_representation(self):
        task = todo.objects.create(user=self.user, todo_name='String Test')
        self.assertEqual(str(task), 'String Test')  # Check string representation

    # Test Case 5: Task Deletion
    def test_task_deletion(self):
        task = todo.objects.create(user=self.user, todo_name='Delete Test')
        task.delete()
        self.assertEqual(todo.objects.count(), 0)  # Check if task is deleted
