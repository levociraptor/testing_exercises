from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('my_site', 'goods') == 'my_site/goods'
    params = {
        'honor': 'smartphones',
        'iphone': 'smartphones',
        'samsung': 'TV'
    }
    assert (build_url('my_site', 'goods', params) == 'my_site/goods?honor=smartphones&iphone=smartphones&samsung=TV')
