# -*- coding: utf-8 -*-


def test_tmp(app):
    app.wd.get("http://localhost/addressbook")
    app.wd.find_element_by_name("pass").click()
    input("press any key")
