import unittest, sys, os

from emoji import Emoji


class TestSnakefire(unittest.TestCase):
    """

    A test class for the snakefire module

    """

    def setUp(self):
        pass

    def testSanity(self):
        self.assertEqual(0, 0)

    def testValidEmoji(self):
        emoji = Emoji()
        self.assertEqual(emoji.replace(':neckbeard:'), '<img class="emoji" title="neckbeard" alt="neckbeard" height="20" width="20" src="https://assets-cdn.github.com/images/icons/emoji/neckbeard.png?v5" align="top">')

    def testInvalidEmoji(self):
        emoji = Emoji()
        invalid = ':neckbeard2:'
        self.assertEqual(emoji.replace(invalid), invalid)

    def testEmojiWithEmpty(self):
        emoji = Emoji()
        self.assertEqual(emoji.replace(''), '')
        self.assertEqual(emoji.replace(None), None)
