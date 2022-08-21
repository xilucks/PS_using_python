import sys
import re

htmlString = sys.stdin.readline()
titles = []
pTags = []


def paser(htmlString: str):
    divTags = htmlString.split('</div>')
    titleParser = re.compile('(?<=title=")(.*?)(?=">)')
    pTagPaser = re.compile('(?<=\<p>)(.*?)(?=<\/p>)')
    for div in divTags:
        title = titleParser.findall(div)
        pTag = pTagPaser.findall(div)
        titles.append(title)
        pTags.append(pTag)


def replacer(element):
    tagDeleter = re.compile('(?<=<)(.*?)(?=>)')
    fixElement = re.sub(tagDeleter, '', element).replace('<', '').replace('>', '')
    return ' '.join(fixElement.split())


def result(titles, pTags):
    for divIdx in range(len(titles)-1):
        if titles[divIdx][0] == '': break
        print('title : ' + titles[divIdx][0])

        for pTag in pTags[divIdx]:
            print(replacer(pTag))


paser(htmlString)
result(titles, pTags)