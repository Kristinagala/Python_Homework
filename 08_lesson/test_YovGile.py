from project_api import Project

api = Project("https://ru.yougile.com")


def test_get_projects():
    body = api.get_project_list()
    count = body["paging"]["count"]
    assert count > 0


def test_get_projects_without_authentication():
    result = api.get_project_list_negative()
    assert result == 401


def test_add_new():
    body = api.get_project_list()
    before = body["paging"]["count"]
    name = "A Beautiful Mind"
    result = api.create_project(name)
    new_id = result["id"]
    body = api.get_project_list()
    after = body["paging"]["count"]
    assert after - before == 1
    assert body["content"][-1]["title"] == name
    assert body["content"][-1]["id"] == new_id


def test_add_new_without_name():
    name = ""
    result = api.create_project_negative(name)
    assert result == 400


def test_add_new_without_name2():
    name = ""
    result = api.create_project(name)
    assert result["error"] == "Bad Request"


def test_get_one_project():
    name = "Black Swan"
    result = api.create_project(name)
    new_id = result["id"] 
    new_project = api.get_project(new_id)
    assert new_project["id"] == new_id
    assert new_project["title"] == name


def test_get_one_project_negative():
    result = api.get_project(None)
    assert result["message"] == "Проект не найден"


def test_edit():
    name = "The Machinist"
    result = api.create_project(name)
    new_id = result["id"]
    new_name = "The Prestige"
    edited = api.edit(new_id, new_name)
    assert edited["id"] == new_id