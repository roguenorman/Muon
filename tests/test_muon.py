import requests
import base64




url1 = base64.b64encode(b'github.com:443/roguenorman/Muon/tree/deployment').decode('utf-8')
url2 = (base64.b64encode(b'en.wikipedia.org/wiki/Python_(programming_language')).decode('utf-8')

def test_add_url():
    response = requests.post(f'http://localhost:5000/urlinfo/1/{url1}?verified=True')
    assert response.status_code == 201

def test_known_url():
    response = requests.get(f'http://localhost:5000/urlinfo/1/{url1}')
    assert response.status_code == 200

def test_unknown_url():
    response = requests.get(f'http://localhost:5000/urlinfo/1/{url2}')
    assert response.status_code == 404




