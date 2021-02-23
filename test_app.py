import os
import unittest
import json

from app import create_app
from models import setup_db, Movie, Actor


token = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndJUHo4a2NjT2lfa2VTaVFpeV9XLSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtay5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmYzRkZGQwNDAyYzUwMDc1NjVlZmI3IiwiYXVkIjoidGFsZW50IiwiaWF0IjoxNjE0MDY4MTc4LCJleHAiOjE2MTQxNTQ1NzgsImF6cCI6Ikc1M1VZdnVJa01UWUJwU3QyZmdwRkl6aXNGUVlOc28wIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Su3qU7I8UQxoejJbrKF2J4mJX0SsgYST2G1SHgFx55DTCY4JXV6uB1xewNEs5D2gPQAeyzdFGTVBvGo8qwtjYXX9mvfP0acJErQBUEZq3ATZ1CzJdUE4G3MMDbyBuX8q30EmxkeAaYpTbZ34LGLVyvx1fGg18DCEi_g6Gazj4sMBukdPY0W3x7ttLaqsp6QoEPSOvNDO1471zNX3HFpS9ymD3ni-2ySvb-0qnwm9Qh5czQNrBqoGLuAwODg4w00TPr3D-4syjlCD_WDAKt3txJOjs20TFUTO4kzOoi4Oq6VECFJxcdDAfQ5ZfipaNmaKaMWRL-RXE3OpjlnBA4dzAA')
token_unauth = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndJUHo4a2NjT2lfa2VTaVFpeV9XLSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtay5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmMjA2NWFiMmFjNTAwMDZmNzg0YWU1IiwiYXVkIjoidGFsZW50IiwiaWF0IjoxNjE0MDcxMzk3LCJleHAiOjE2MTQxNTc3OTcsImF6cCI6Ikc1M1VZdnVJa01UWUJwU3QyZmdwRkl6aXNGUVlOc28wIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.l4_CPoG-kCOjeveFyJmUQdpdxAfg7OOlgi60-kTdg468DPAQPhHNLFr_vrS9YAyqAogv4xucpDIQHSK3y3fuOpstDiPKmTolYNQJIH3Q54Mf52C4av1ZnzyQOhMys-2x3t7P6_ol2UoSwEtIHk92P0SS-AFvjSU2tszg4RfQ7k6zTsPDddpYKc61RtvRvtyUbN68Xdx3GS6wJpVKuXLUxK9T_N-qJUCALyS7csyNJifyryP8-1FA5s9_AdSHbxwduKKPMFOIwRRoUw_0u2ROhM2_tvCYdTFDvotTTb96hOkL8QmYmSKZdFskFCoJkOLRdAoGwqEvOory97jbfO2ayg')


class CastingAgencyTest(unittest.TestCase):
    """Setup test suite for the routes"""

    def setUp(self):
        """Setup application """
        self.app = create_app()
        self.client = self.app.test_client
        self.test_movie = {"title": "Jonny Gun", "release_date": "2022-05-06"}
        self.database_path = 'postgres://fdtixnzpqczohg:4b0218613153bd586c7c757a7d85eee7b258203a9893e517679faefc915e8c06@ec2-34-239-33-57.compute-1.amazonaws.com:5432/dcqcjnilm2ktfd'

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_get_all_movies(self):
        response = self.client().get(
            '/movies',
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movie_by_id(self):
        response = self.client().get(
            '/movies/1',
            headers={"Authorization": f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_404_get_movie_by_id(self):
        response = self.client().get(
            '/movies/100',
            headers={"Authorization": f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_post_movie(self):
        response = self.client().post(
            '/movies',
            json={'title': 'Kit', "release_date": "2022-05-06"},
            headers={'Authorization': f'Bearer {token}'}
        )

        self.assertEqual(response.status_code, 201)

    def test_400_post_movie(self):
        response = self.client().post(
            '/movies',
            json={},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_401_post_movie_unauthorized(self):
        response = self.client().post(
            '/movies',
            json=self.test_movie,
            headers={'Authorization': f'Bearer {token_unauth}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_patch_movie(self):
        response = self.client().patch(
            '/movies/1',
            json={'title': 'Jesus 2', 'release_date': "2022-08-04"},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie']['title'], 'Jesus 2')
        self.assertEqual(
            data['movie']['release_date'],
            '2022-08-04'
        )

    def test_400_patch_movie(self):
        response = self.client().patch(
            '/movies/1',
            json={},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_401_patch_movie_unauthorized(self):
        response = self.client().patch(
            '/movies/1',
            json=self.test_movie,
            headers={'Authorization': f'Bearer {token_unauth}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_404_patch_movie(self):
        response = self.client().patch(
            '/movies/12323',
            json=self.test_movie,
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_movie(self):
        response = self.client().delete(
            '/movies/2',
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])

    def test_401_delete_movie(self):
        response = self.client().delete(
            '/movies/2',
            headers={'Authorization': f'Bearer {token_unauth}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_404_delete_movie(self):
        response = self.client().delete(
            '/movies/22321',
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_all_actors(self):
        response = self.client().get(
            '/actors',
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actor_by_id(self):
        response = self.client().get(
            '/actors/1',
            headers={"Authorization": "Bearer " + token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(data['actor']['name'], 'Jessie')

    def test_404_get_actor_by_id(self):
        response = self.client().get(
            '/actors/100',
            headers={"Authorization": "Bearer " + token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_post_actor(self):
        response = self.client().post(
            '/actors',
            json={'name': 'Kit', 'age': 18, "gender": "male"},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], 'Kit')
        self.assertEqual(data['actor']['age'], 18)
        self.assertEqual(data['actor']['gender'], 'male')

    def test_400_post_actor(self):
        response = self.client().post(
            '/actors',
            json={},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_401_post_actor_unauthorized(self):
        response = self.client().post(
            '/actors',
            json={'name': 'Maggie', 'age': 2, "gender": "female"},
            headers={'Authorization': f'Bearer {token_unauth}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_patch_actor(self):
        response = self.client().patch(
            '/actors/1',
            json={'name': 'Jessie', 'age': 24, "gender": "female"},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], 'Jessie')
        self.assertEqual(data['actor']['age'], 24)
        self.assertEqual(data['actor']['gender'], 'female')

    def test_400_patch_actor(self):
        response = self.client().patch(
            '/actors/1',
            json={'name': 'Jason', 'age': 22, "gender": "male"},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_401_patch_actor_unauthorized(self):
        response = self.client().patch(
            '/actors/1',
            json={'name': 'Johnny', 'age': 22, "gender": "male"},
            headers={'Authorization': f'Bearer {token_unauth}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_404_patch_actor(self):
        response = self.client().patch(
            '/actor/12323',
            json={'name': 'Johnathan', 'age': 25, "gender": "male"},
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_actor(self):
        response = self.client().delete(
            '/actors/2',
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])

    def test_401_delete_actor(self):
        response = self.client().delete(
            '/actors/2',
            headers={'Authorization': f'Bearer {token_unauth}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    def test_404_delete_actor(self):
        response = self.client().delete(
            '/actors/22321',
            headers={'Authorization': f'Bearer {token}'}
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')


# Make the tests executable
if __name__ == "__main__":
    unittest.main()
