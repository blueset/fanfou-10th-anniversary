from leancloud import Object
from flask_login import UserMixin


class FFAuth(Object, UserMixin):

    @property
    def is_active(self):
        return True
