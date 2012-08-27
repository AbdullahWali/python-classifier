import docclass
import feedfilter

#
# Naive Bayes classifier
#
#cl2=docclass.naivebayes(docclass.getwords)
#cl2.setdb('test2.db')
#docclass.sampletrain(cl2)

#
# Fisher classifier
#

cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('feed.db')
docclass.sampletrain(cl)
feedfilter.read('python_search.xml', cl)
