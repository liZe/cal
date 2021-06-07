from contextlib import contextmanager

from radicale.auth import BaseAuth
from radicale.storage import BaseCollection, BaseStorage

PLUGIN_CONFIG_SCHEMA = {
}


class Auth(BaseAuth):
    def __init__(self, configuration):
        super().__init__(configuration.copy(PLUGIN_CONFIG_SCHEMA))

    def login(self, login, password):
        return login


class Collection(BaseCollection):
    @property
    def path(self):
        raise NotImplementedError

    @property
    def owner(self):
        return super().owner()

    @property
    def is_principal(self):
        return super().is_principal()

    @property
    def etag(self):
        return super().etag()

    def sync(self, old_token=None):
        return super().sync(old_token)

    def get_multi(self, hrefs):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def get_filtered(self, filters):
        return super().get_filtered(filters)

    def has_uid(self, uid):
        return super().has_uid(uid)

    def upload(self, href, item):
        raise NotImplementedError

    def delete(self, href=None):
        raise NotImplementedError

    def get_meta(self, key=None):
        raise NotImplementedError

    def set_meta(self, props):
        raise NotImplementedError

    @property
    def last_modified(self):
        raise NotImplementedError

    def serialize(self):
        return super().serialize()


class Storage(BaseStorage):
    _collection_class = Collection

    def __init__(self, configuration):
        super().__init__(configuration.copy(PLUGIN_CONFIG_SCHEMA))

    def discover(self, path, depth='0'):
        raise NotImplementedError

    def move(self, item, to_collection, to_href):
        raise NotImplementedError

    def create_collection(self, href, items=None, props=None):
        raise NotImplementedError

    @contextmanager
    def acquire_lock(self, mode, user=None):
        raise NotImplementedError

    def verify(self):
        raise NotImplementedError
