# coding: utf-8
import unittest

from scieloh5m5 import h5m5


class H5M5Test(unittest.TestCase):

    def test_load_issn(self):

        result = h5m5.get_metrics('0103-3352')

        expected = {
            u'2017': {
                'h5': '13',
                'm5': '18',
                'url': 'http://scholar.google.com/citations?view_op=list_hcore&venue=7e-4gBNaGSMJ.2017&hl=en',
                'year': '2017'
            },
            u'2016': {
                'h5': u'12',
                'm5': u'17',
                'url': u'http://scholar.google.com/citations?view_op=list_hcore&venue=Q_f-804K9OAJ.2016&hl=en',
                'year': u'2016'
            },
            u'2015': {
                'm5': u'16',
                'url': u'http://scholar.google.com/citations?view_op=list_hcore&venue=EqPlmpMQjygJ.2015&hl=pt-BR',
                'h5': u'10',
                'year': u'2015'
            },
            u'2014': {
                'm5': u'12',
                'url': u'http://scholar.google.com/citations?view_op=list_hcore&venue=EqPlmpMQjygJ.2014&hl=pt-br',
                'h5': u'9',
                'year': u'2014'
            },
            u'2013': {
                'm5': u'8',
                'url': u'http://scholar.google.com/citations?view_op=list_hcore&venue=EqPlmpMQjygJ.2013&hl=pt-br',
                'h5': u'7',
                'year': u'2013'
            }
        }

        self.maxDiff = None
        self.assertEqual(expected, result)

    def test_load_issn_year(self):

        result = h5m5.get_metrics('0103-3352', '2015')

        expected = {
            'h5': u'10',
            'm5': u'16',
            'url': u'http://scholar.google.com/citations?view_op=list_hcore&venue=EqPlmpMQjygJ.2015&hl=pt-BR',
            'year': u'2015'
        }

        self.assertEqual(expected, result)

    def test_load_issn_year_not_available_year(self):

        result = h5m5.get_metrics('0103-3352', 'XXXX')

        expected = None

        self.assertEqual(expected, result)

    def test_load_issn_year_not_available_issn(self):

        result = h5m5.get_metrics('0103-XXXX')

        expected = None

        self.assertEqual(expected, result)
