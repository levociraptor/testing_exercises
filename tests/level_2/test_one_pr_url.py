import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__return_true():
    url = 'https://github.com/levociraptor/oop_bases_challenges/pull/1'

    test = is_github_pull_request_url(url)

    assert test is True


def test__is_github_pull_request_url__return_false():
    url = 'https://vk.com/levociraptor/oop_bases_challenges/pull/1'

    test = is_github_pull_request_url(url)

    assert test is False


def test__is_github_pull_request_url__invalid_url_return_false():
    url = 'sdfsafgdfsdfklshdfjh834sdkjfgh'

    test = is_github_pull_request_url(url)

    assert test is False

# Не уверен стоит ли тут использовать parametrize, по этому оставил оба варианта
@pytest.mark.parametrize(
    'url, expected_result',
    [
        ('https://github.com/levociraptor/oop_bases_challenges/pull/1', True),
        ('https://vk.com/levociraptor/oop_bases_challenges/pull/1', False),
        ('sdfsafgdfsdfklshdfjh834sdkjfgh', False)
    ]
)
def test__is_github_pull_request_url__return_true_if_valid_url_else_false(url, expected_result):
    assert is_github_pull_request_url(url) is expected_result
