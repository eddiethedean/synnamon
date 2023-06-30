import unittest
from synnamon import get_syns


class TestGetSyns(unittest.TestCase):
    def test_get_syns_pos(self):
        # Test case for a word that exists in the thesaurus
        result = get_syns('jump')
        self.assertIn('noun', result)
        self.assertIn('verb', result)

    def test_get_syns_not_exist(self):
        # Test case for a word that does not exist in the thesaurus
        result = get_syns('notaword')
        self.assertEqual(result, {})

    def test_get_syns_plural(self):
        # Test case for a plural noun that does not exists in the thesaurus
        result = get_syns('dragons')
        self.assertIn('noun', result)
        self.assertListEqual(result['noun'], ['flying lizards',
                                                'tartars',
                                                'Dragons',
                                                'Dracos',
                                                'firedrakes',
                                                'flying dragons'])
        

if __name__ == '__main__':
    unittest.main()