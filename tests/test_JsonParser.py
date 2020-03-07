from tests.test_data.JsonParser_data import json_example_1

from pythonsnippits.JsonParser import JsonParser


class TestNestedJson:
    def test_init(self):
        jp = JsonParser(json_example_1)
        assert jp.glossary.title == "example glossary"
        assert jp.glossary.GlossDiv.title == "S"
        assert jp.glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso == [
            "GML",
            "XML",
        ]

    def test_iterablity(self):
        jp = JsonParser(json_example_1)
        expected = [
            "SGML",
            "SGML",
            "Standard Generalized Markup Language",
            "SGML",
            "ISO 8879:1986",
            {
                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                "GlossSeeAlso": ["GML", "XML"],
            },
            "markup",
        ]
        for e, a in zip(expected, jp.glossary.GlossDiv.GlossList.GlossEntry):
            assert e == a
