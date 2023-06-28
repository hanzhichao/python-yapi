from enum import Enum, auto


class Variable:
    name: str
    value: str


class Env:
    id: int
    name: str
    domain: str
    header: list[Variable]
    _global: list[Variable]


class Tag:
    name: str
    desc: str


class Group:
    id: int
    name: str
    type: str
    group_name: str
    add_time: int
    up_time: int


class Project:
    group: Group
    id: int
    name: str
    project_type: str
    basepath: str
    env: list[Env]
    tag: list[Tag]
    strice: bool
    is_json5: bool
    switch_notice: bool
    add_time: int
    up_time: int


class User:
    uid: int
    username: str
    email: str
    role: str
    type: str
    add_time: int
    up_time: int


class Category:
    name: str


class HttpMethod(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    PATCH = auto()
    TRACE = auto()


class Interfact:
    project: Project
    cat: Category
    index: int
    title: str
    method: HttpMethod
    path: str
    type: str
    status: str

    req_params: list
    req_query: list
    req_headers: list
    req_body_form: str
    res_body_type: str
    req_body_is_json_schema: bool
    res_body_is_json_schema: bool
    api_opened: bool

    add_time: int
    up_time: int

    user: User
    edit_user: User
