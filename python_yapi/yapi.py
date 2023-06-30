

from .user import UserMixIn
from .group import GroupMixIn
from .project import ProjectMixIn
from .collection import CollectionMixIn
from .interface import InterfaceMixIn


class YApi(UserMixIn, GroupMixIn, ProjectMixIn, CollectionMixIn, InterfaceMixIn): ...
