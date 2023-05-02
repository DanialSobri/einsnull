import unittest
from .student import StudentModel, create_student, read_student

fake_db = {}

class StudentCRUD(unittest.TestCase):

    def test_student_model(self):
        # Create a student using student model and append it in fake_db
        new_student = StudentModel(name="Max Mustaman",email="max.mustaman@example.com")
        # Model validation
        self.assertEqual(new_student.name, 'Max Mustaman')
        self.assertEqual(new_student.email, 'max.mustaman@example.com')

    def test_create_student(self):
        # Create a student using student model and append it in fake_db
        fake_db={}
        new_student = StudentModel(name="Max Mustaman",email="max.mustaman@example.com")
        self.assertTrue(create_student(new_student,fake_db))
        # Existance check TODO: Why return None object instead of Student Model
        self.assertEqual(len(fake_db),1)

    def test_read(self):
        # Create a student using student model and append it in fake_db
        fake_db={}
        new_student = StudentModel(name="Max Mustaman",email="max.mustaman@example.com")
        self.assertTrue(create_student(new_student,fake_db))
        self.assertEqual(len(fake_db),1)
        print(read_student("0",fake_db))

    def test_delete(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_update(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        
if __name__ == '__main__':
    unittest.main()


    