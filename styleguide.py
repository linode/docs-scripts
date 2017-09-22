# -*- coding: utf-8 -*-

import regex
import os
import sys
import fnmatch

rules = [
    {'rule': '"Open-source" should be hyphenated',
     'regex': 'open source'},
    {'rule': "Avoid the use of 'we', 'our', and 'let\'s'",
     'regex': "([Ww]e\s|[Oo]ur\s|[Ll]et's)"},
    {'rule':"No trailing whitespace",
     'regex':"[ \t]+$"},
    {'rule': "Use a single space after a period",
     'regex': "\.  "},
    {'rule':"Prefer the Oxford comma",
     'regex':"(?:\w+,\s+){1,}\w+\s+and\s+\w+."},
]

def main():
    source_dir = '.'
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    for root, dirnames, filenames in os.walk(source_dir):
        for filename in fnmatch.filter(filenames,'*.md'):
            with open(os.path.join(root,filename)) as infile:
                for line_number, line in enumerate(infile,1):
                    for rule in rules:
                        reg = regex.compile(rule['regex'])
                        match_obj = regex.search(reg, line)
                        if match_obj:
                            print(str(filename) + ":\t" + str(line_number) + ":" + str(match_obj.start()) + "\t" + rule['rule'])
    return True


if __name__ == "__main__":
    main()
