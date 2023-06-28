

from .auth import LoginMixIn
from .group import GroupMixIn
from .project import ProjectMixIn
from .collection import CollectionMixIn
from .interface import InterfaceMixIn


class YApi(LoginMixIn, GroupMixIn, ProjectMixIn, CollectionMixIn, InterfaceMixIn): ...