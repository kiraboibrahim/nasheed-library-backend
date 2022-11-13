from django.conf import settings

import hashids


HASH_IDS = hashids.Hashids(salt=settings.HASHIDS_SALT)
