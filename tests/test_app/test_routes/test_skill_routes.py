# test_skill_routes.py

import unittest
from app import create_app, db
from app.models import User, Skill, Role, SkillLevel, SkillCategory
from bs4 import BeautifulSoup


class SkillRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

        self.admin_user = User(email='admin@example.com',
                               password='adminpassword', username='adminuser')
        self.admin_user.roles.append(Role(name='ADMIN'))
        db.session.add(self.admin_user)
        self.dummy_skill = Skill(
            name='Dummy Skill', level=SkillLevel.BEGINNER, category="DevOps")
        db.session.add(self.dummy_skill)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login_admin_user(self):
        return self.client.post('/signin', data={
            'email': 'admin@example.com',
            'password': 'adminpassword'
        }, follow_redirects=True)

    def test_add_skill(self):
        self.login_admin_user()
        form_data = {
            'name': "NewSkill",
            'level': SkillLevel.BEGINNER.value,
            'category': "DevOps"
        }
        response = self.client.post(
            '/interface/add_skill', data=form_data, follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        flashed_messages = soup.find_all('div', class_='alert alert-success')
        self.assertTrue(any('Your skill has been added!' in message.get_text()
                        for message in flashed_messages))
        new_skill = Skill.query.filter_by(name='NewSkill').first()
        self.assertIsNotNone(new_skill)

    def test_delete_skill(self):
        self.login_admin_user()
        response = self.client.post('/interface/delete_skill', data={
            "related_skills": self.dummy_skill.id
        }, follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        flashed_messages = soup.find_all('div', class_='alert alert-success')
        self.assertTrue(any('Skill has been deleted!' in message.get_text(
        ) for message in flashed_messages))
        deleted_skill = Skill.query.filter_by(name='Delete Me').first()
        self.assertIsNone(deleted_skill)

    def test_update_skill(self):
        self.login_admin_user()
        skill_form_data = {
            'skill_id': self.dummy_skill.id,
            'name': 'UpdatedName',
            'category': "DevOps",
            'level': SkillLevel.BEGINNER.value,
        }
        response = self.client.post(
            '/interface/update_skill', data=skill_form_data, follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        flashed_messages = soup.find_all('div', class_='alert alert-success')
        print(flashed_messages)
        self.assertTrue(any('Skill has been updated!' in message.get_text(
        ) for message in flashed_messages))
        updated_skill = Skill.query.filter_by(name='UpdatedName').first()
        self.assertIsNotNone(updated_skill)


if __name__ == '__main__':
    unittest.main()
