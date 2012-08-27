import feedparser
import re

def read(feed, classifier):
    """docstring for read"""
    f=feedparser.parse(feed)

    for entry in f['entries']:
        print
        print '----'
        print 'Title : ' + entry['title'].encode('utf-8')
        print 'Author: ' + entry['publisher'].encode('utf-8')
        print
        print entry['summary'].encode('utf-8')

        fulltext='%s\n%s\n%s' % (entry['title'], entry['publisher'], entry['summary'])

        print 'Theory: ' + str(classifier.classify(fulltext))
        cl=raw_input('Enter category: ')
        classifier.train(fulltext, cl)
