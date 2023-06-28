=====
Usage
=====

To use python-yapi in a project::

    from python_yapi import YApi

    yapi = YApi('http://localhost:3000')
    yapi.login('admin@admin.com', 'ylme.com'

    yapi.create_project(name='Demo Project')
