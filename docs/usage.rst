=====
Usage
=====

To use python-yapi, first you should login as a user::

    import json
    from python_yapi import YApi

    yapi = YApi(base_url='http://localhost:3000')
    email, password = 'kevin@126.com', 'abc123'
    yapi.login(email, password)

To create a project in your YApi::

    # Create a private project in user default group, with auto basepath, random color and random icon.
    project = yapi.add_project('Demo Project')
    project_id = project['_id']


To create a GET interface in the project::

    # Create a private "GET" interface in project default category with a sample json response.
    yapi.add_interface(project_id=project_id,
                       title='Calc Add',
                       method='GET',
                       path='/add',
                       req_query=[
                           {"name": "a", "required": "1", "example": "1", "desc": "var a"},
                           {"name": "b", "required": "1", "example": "2", "desc": "var b"},
                       ],
                       res_body={"code": 0, "message": "success", "data": {"result": "3"}})

To create a POST interface in the project::

    # Create a private "POST" interface in project default category with a sample json data and a sample json response.
    yapi.add_interface(project_id=project_id,
                       title='Calc Sub',
                       method='POST',
                       path='/sub',
                       req_headers=[{"name": "Content-Type", "value": "application/json"}],
                       req_body_other={"a": "5", "b": "1"},
                       res_body={"code": 0, "message": "success", "data": {"result": "4"}})

