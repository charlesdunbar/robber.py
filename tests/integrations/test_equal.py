# -*- coding: utf-8 -*-

from unittest import TestCase

from robber import expect
from tests import must_fail


class TestEqualIntegrations(TestCase):
    def test_eq_success(self):
        expect(1).to.eq(1)
        expect([1, 2]).to.eq([1, 2])
        expect((1, 2)).to.eq((1, 2))
        expect(1).to == 1
        expect(1) == 1
        # unicode string
        expect(u'Mèo').to.eq('Mèo')
        # unicode list
        expect([u'Mèo', u'Chó']).to.eq(['Mèo', 'Chó'])
        # unicode list in list
        expect([[u'Mèo'], [u'Chó']]).to.eq([['Mèo'], ['Chó']])
        # unicode dict
        expect({
            'cat': u'Mèo',
            'dog': u'Chó',
        }).to.eq({
            'cat': 'Mèo',
            'dog': 'Chó',
        })
        # unicode dict in dict
        expect({
            'd1': {'cat': u'Mèo'},
            'd2': {'dog': u'Chó'},
        }).to.eq({
            'd1': {'cat': 'Mèo'},
            'd2': {'dog': 'Chó'},
        })
        # unicode list in dict
        expect({
            'd1': [u'Mèo', u'Chó'],
            'd2': [u'Mèo', u'Chó'],
        }).to.eq({
            'd1': ['Mèo', 'Chó'],
            'd2': ['Mèo', 'Chó'],
        })
        # unicode dict in list
        expect(
            [{'cat': u'Mèo', 'dog': u'Chó'}, {'cat': u'Mèo', 'dog': u'Chó'}]
        ).to.eq(
            [{'cat': 'Mèo', 'dog': 'Chó'}, {'cat': 'Mèo', 'dog': 'Chó'}]
        )

    @must_fail
    def test_eq_failure(self):
        expect(1).to.eq(2)
        expect(1).not_to.eq(1)

    def test_ne_success(self):
        expect(1).to.ne(2)
        expect(1).to != 2
        expect(1) != 2

    @must_fail
    def test_ne_failure(self):
        expect(1).to.ne(1)

    def test_not_to_eq_success(self):
        expect(1).not_to.eq(2)
        expect([1, 2]).not_to.eq([2, 1])
        expect((1, 2)).not_to.eq((2, 1))
        expect(1).not_to == 2
