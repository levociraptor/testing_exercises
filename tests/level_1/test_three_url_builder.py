from functions.level_1.three_url_builder import build_url


def test__build_url__return_url_without_params():
    host_name = 'my_site'
    relative_name = 'goods'

    url = build_url(host_name, relative_name)

    assert url == 'my_site/goods'


def test__build_url__return_url_with_params():
    host_name = 'my_site'
    relative_name = 'goods'
    params = {
        'honor': 'smartphones',
        'iphone': 'smartphones',
        'samsung': 'TV'
    }

    url = build_url(host_name, relative_name, params)

    assert url == 'my_site/goods?honor=smartphones&iphone=smartphones&samsung=TV'


def test__build_url__return_url_with_params_with_spaces():
    host_name = 'my_site'
    relative_name = 'goods'
    params = {
        'ho nor': 'smartpho nes',
        'iph one': 'smartphone s',
        'sams ung': 'TV'
    }

    url = build_url(host_name, relative_name, params)

    assert url == 'my_site/goods?ho nor=smartpho nes&iph one=smartphone s&sams ung=TV'