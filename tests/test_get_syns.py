import unittest
from synnamon import get_syns


class TestGetSyns(unittest.TestCase):
    def test_get_syns_pos(self):
        # Test case for a word that exists in the thesaurus
        result = get_syns('jump')
        expected = {'noun': ['leap', 'parachuting', 'jumping', 'saltation', 'startle', 'start'],
                    'verb': ['leap',
                            'spring',
                            'stand out',
                            'alternate',
                            'startle',
                            'climb up',
                            'chute',
                            'jump-start',
                            'jump out',
                            'skip over',
                            'stick out',
                            'jump off',
                            'jumpstart',
                            'pass over',
                            'derail',
                            'start',
                            'rise',
                            'bound',
                            'parachute',
                            'jump on',
                            'leap out',
                            'skip']}
        self.assertEqual(result, expected)

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
        
    def test_get_syns_empty_word(self):
        # Test case for an empty string
        result = get_syns('')
        self.assertEqual(result, {})

    def test_get_syns_multiple_pos(self):
        # Test case for a word with multiple parts of speech
        result = get_syns('run')
        self.assertIn('noun', result)
        self.assertIn('verb', result)

    def test_get_syns_case_insensitive(self):
        # Test case for a word with mixed case
        result = get_syns('HaPpY')
        expected = {'adj': ['halcyon',
                            'glad',
                            'prosperous',
                            'laughing',
                            'riant',
                            'joyous',
                            'blessed',
                            'felicitous',
                            'contented',
                            'willing',
                            'elated',
                            'well-chosen',
                            'blissful',
                            'content',
                            'golden',
                            'bright',
                            'cheerful',
                            'euphoric',
                            'joyful',
                            'fortunate']}
        self.assertEqual(result, expected)

    def test_get_syns_special_chars(self):
        # Test case for a word with special characters
        result = get_syns('c++')
        self.assertEqual(result, {})
        

if __name__ == '__main__':
    unittest.main()