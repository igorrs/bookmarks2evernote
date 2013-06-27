from bs4 import BeautifulSoup
import codecs
import argparse
import time

class Bookmark():
    """docstring for Bookmark"""
    def __init__(self, title, url, tag, date):
        self.title = title
        self.url = url
        self.tag = '<tag>' + tag + '</tag>'
        self.date = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime(float(long(date) / 1000000)))
        self.content = '''<a href="%(url)s">%(title)s</a>''' % {'title': self.title, 'url': self.url}

    def printAsEnex(self):
        output = """<note><title>%(title)s</title><content><![CDATA[<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note style="word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space;">%(content)s</en-note>]]></content><created>%(date)s</created><updated>%(date)s</updated>%(tag)s<note-attributes><source-url>%(url)s</source-url></note-attributes></note>""" % {'title': self.title, 'content': self.content, 'tag': self.tag, 'url': self.url, 'date': self.date,}
        return output.replace('&', '&amp;')

    def __str__(self):
        return unicode(self.title + " " + self.url + " " + self.tag)

def unique(bookmarks):
    found = {}
    res = []

    for bookmark in bookmarks:
        if bookmark.url not in found:
            found[bookmark.url] = bookmark
        else:
            found[bookmark.url].tag += bookmark.tag

    for key in found:
        res.append(found[key])

    return res

def main():
    

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("html_file", help="the file that contains the bookmarks in html format")
        args = parser.parse_args()
        soup = BeautifulSoup(codecs.open(args.html_file, encoding='utf-8'), 'html.parser')

        html_tags = soup.findAll(['h3', 'a'])

        en_tag = ''

        bookmarks = []

        for tag in html_tags:
            if tag.name == 'h3':
                en_tag = tag.string
            if tag.name == 'a':
                new_bm = Bookmark(tag.string, tag['href'], en_tag, tag['add_date'])
                bookmarks.append(new_bm)

        print "Total Bookmarks: " + str(len(bookmarks))

        bookmarks = unique(bookmarks)

        print "Unique Bookmarks: " + str(len(bookmarks))

        output_file = args.html_file.split('.')[0] + ".enex"
        out = codecs.open(output_file, 'w', encoding='utf-8')

        out.write("""<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export.dtd"><en-export application="Evernote/Windows" version="4.x">""")
        for n in bookmarks:
            out.write(n.printAsEnex())

        out.write("</en-export>")
        out.close()

        print "Success! Output file name: " + output_file
    except Exception as e:
        print "Error!"
        print type(e)
        print e.args


if __name__ == '__main__':
    main()
