from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__success_case():
    url = 'https://github.com/levociraptor/oop_bases_challenges/pull/1'

    test = is_github_pull_request_url(url)

    assert test == True


def test__is_github_pull_request_url__negative_case():
    url = 'https://vk.com/levociraptor/oop_bases_challenges/pull/1'

    test = is_github_pull_request_url(url)

    assert test == False


def test__is_github_pull_request_url__random_string_case():
    url = 'sdfsafgdfsdfklshdfjh834sdkjfgh'

    test = is_github_pull_request_url(url)

    assert test == False
