import docclass

cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('test.db')
docclass.sampletrain(cl)

cl2=docclass.naivebayes(docclass.getwords)
cl2.setdb('test2.db')
docclass.sampletrain(cl2)
