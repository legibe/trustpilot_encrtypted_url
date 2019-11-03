import json
from urllib.parse import quote as urlencode
from trustpilot_authenticated_encryption import encrypt
from config import Config


class TrustPilotURLEncryption(object):

    _config = None

    @classmethod
    def encrypt(self, data):
        if self._config is None:
            self._config = Config('config.yaml')
        payload = urlencode(encrypt(json.dumps(data).encode('utf-8'),
                            self._config['trustpilot']['encryption_key'],
                            self._config['trustpilot']['hash_key']))
        return self._config['trustpilot']['url'] % (self._config['trustpilot']['domain'], payload)
