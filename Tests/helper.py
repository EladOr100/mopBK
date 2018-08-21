# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import allure_commons
from allure_pytest.utils import ALLURE_TITLE
from allure_pytest.utils import ALLURE_DESCRIPTION, ALLURE_DESCRIPTION_HTML
from allure_pytest.utils import ALLURE_LABEL_PREFIX, ALLURE_LINK_PREFIX


@allure_commons.hookimpl
def decorate_as_title(test_title):
    allure_title = getattr(pytest.mark, ALLURE_TITLE)
    return allure_title(test_title)


@allure_commons.hookimpl
def decorate_as_description(test_description):
    allure_description = getattr(pytest.mark, ALLURE_DESCRIPTION)
    return allure_description(test_description)


@allure_commons.hookimpl
def decorate_as_description_html(test_description_html):
    allure_description_html = getattr(pytest.mark, ALLURE_DESCRIPTION_HTML)
    return allure_description_html(test_description_html)


@allure_commons.hookimpl
def decorate_as_label(label_type, labels):
    allure_label_marker = '{prefix}.{label_type}'.format(prefix=ALLURE_LABEL_PREFIX, label_type=label_type)
    allure_label = getattr(pytest.mark, allure_label_marker)
    return allure_label(*labels, label_type=label_type)
