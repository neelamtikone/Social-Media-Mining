Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> nltk.corpus.gutenberg.fileids()
[u'austen-emma.txt', u'austen-persuasion.txt', u'austen-sense.txt', u'bible-kjv.txt', u'blake-poems.txt', u'bryant-stories.txt', u'burgess-busterbrown.txt', u'carroll-alice.txt', u'chesterton-ball.txt', u'chesterton-brown.txt', u'chesterton-thursday.txt', u'edgeworth-parents.txt', u'melville-moby_dick.txt', u'milton-paradise.txt', u'shakespeare-caesar.txt', u'shakespeare-hamlet.txt', u'shakespeare-macbeth.txt', u'whitman-leaves.txt']
>>> emma = nltk.corpus.gutenberg.words('austen-emma.txt')
>>> len(emma)
192427
>>> emma.concordance("surprize")

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    emma.concordance("surprize")
AttributeError: 'StreamBackedCorpusView' object has no attribute 'concordance'
>>> emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
>>> emma.concordance("surprize")
Displaying 25 of 37 matches:
er father , was sometimes taken by surprize at his being still able to pity ` 
hem do the other any good ." " You surprize me ! Emma must do Harriet good : a
Knightley actually looked red with surprize and displeasure , as he stood up ,
r . Elton , and found to his great surprize , that Mr . Elton was actually on 
d aid ." Emma saw Mrs . Weston ' s surprize , and felt that it must be great ,
father was quite taken up with the surprize of so sudden a journey , and his f
y , in all the favouring warmth of surprize and conjecture . She was , moreove
he appeared , to have her share of surprize , introduction , and pleasure . Th
ir plans ; and it was an agreeable surprize to her , therefore , to perceive t
talking aunt had taken me quite by surprize , it must have been the death of m
f all the dialogue which ensued of surprize , and inquiry , and congratulation
 the present . They might chuse to surprize her ." Mrs . Cole had many to agre
the mode of it , the mystery , the surprize , is more like a young woman ' s s
 to her song took her agreeably by surprize -- a second , slightly but correct
" " Oh ! no -- there is nothing to surprize one at all .-- A pretty fortune ; 
t to be considered . Emma ' s only surprize was that Jane Fairfax should accep
of your admiration may take you by surprize some day or other ." Mr . Knightle
ation for her will ever take me by surprize .-- I never had a thought of her i
 expected by the best judges , for surprize -- but there was great joy . Mr . 
 sound of at first , without great surprize . " So unreasonably early !" she w
d Frank Churchill , with a look of surprize and displeasure .-- " That is easy
; and Emma could imagine with what surprize and mortification she must be retu
tled that Jane should go . Quite a surprize to me ! I had not the least idea !
 . It is impossible to express our surprize . He came to speak to his father o
g engaged !" Emma even jumped with surprize ;-- and , horror - struck , exclai
>>> em== nltk.corpus.gutenberg.words('austen-emma.txt')

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    em== nltk.corpus.gutenberg.words('austen-emma.txt')
NameError: name 'em' is not defined
>>> em= nltk.corpus.gutenberg.words('austen-emma.txt')
>>> type(em)
<class 'nltk.corpus.reader.util.StreamBackedCorpusView'>
>>> type(emma)
<class 'nltk.text.Text'>
>>> print fileids

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print fileids
NameError: name 'fileids' is not defined
>>> print(fileids)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(fileids)
NameError: name 'fileids' is not defined
>>> print fileids()

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print fileids()
NameError: name 'fileids' is not defined
>>> print gutenberg.fileids()

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print gutenberg.fileids()
NameError: name 'gutenberg' is not defined
>>> print gutenberg.fileids

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print gutenberg.fileids
NameError: name 'gutenberg' is not defined
>>> print fileid in gutenberg.fileids()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print fileid in gutenberg.fileids()
NameError: name 'fileid' is not defined
>>> for fileid in gutenberg.fileids():
	print fileid

	

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    for fileid in gutenberg.fileids():
NameError: name 'gutenberg' is not defined
>>> for fileid in gutenberg.fileids():
	print (fileid)

	

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    for fileid in gutenberg.fileids():
NameError: name 'gutenberg' is not defined
>>> for fileid in gutenberg.fileids():
	print fileid

	

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    for fileid in gutenberg.fileids():
NameError: name 'gutenberg' is not defined
>>> from nltk.corpus import gutenberg
>>> for fileid in gutenberg.fileids():
	print fileid

	
austen-emma.txt
austen-persuasion.txt
austen-sense.txt
bible-kjv.txt
blake-poems.txt
bryant-stories.txt
burgess-busterbrown.txt
carroll-alice.txt
chesterton-ball.txt
chesterton-brown.txt
chesterton-thursday.txt
edgeworth-parents.txt
melville-moby_dick.txt
milton-paradise.txt
shakespeare-caesar.txt
shakespeare-hamlet.txt
shakespeare-macbeth.txt
whitman-leaves.txt
>>> type(fileid)
<type 'unicode'>
>>> len(shakespeare-caesar.txt)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    len(shakespeare-caesar.txt)
NameError: name 'shakespeare' is not defined
>>> num_words = len(gutenberg.words(fileid))
>>> len(num_words)

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    len(num_words)
TypeError: object of type 'int' has no len()
>>> num_words
154883
>>> for fileid in gutenberg.fileids():
	num_words = len(gutenberg.words(fileid))
	print(num_words)

	
192427
98171
141576
1010654
8354
55563
18963
34110
96996
86063
69213
210663
260819
96825
25833
37360
23140
154883
>>> macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
>>> macbeth_sentences
[[u'[', u'The', u'Tragedie', u'of', u'Macbeth', u'by', u'William', u'Shakespeare', u'1603', u']'], [u'Actus', u'Primus', u'.'], ...]
>>> len(macbeth_sentences)
1907
>>> macbeth_sentences[1000]
[u'quite', u'vnmann', u"'", u'd', u'in', u'folly']
>>> macbeth_sentences[0]
[u'[', u'The', u'Tragedie', u'of', u'Macbeth', u'by', u'William', u'Shakespeare', u'1603', u']']
>>> macbeth_sentences[0:1]
[[u'[', u'The', u'Tragedie', u'of', u'Macbeth', u'by', u'William', u'Shakespeare', u'1603', u']']]
>>> macbeth_sentences[0:2]
[[u'[', u'The', u'Tragedie', u'of', u'Macbeth', u'by', u'William', u'Shakespeare', u'1603', u']'], [u'Actus', u'Primus', u'.']]
>>>  longest_len = max(len(s) for s in macbeth_sentences)
 
  File "<pyshell#45>", line 2
    longest_len = max(len(s) for s in macbeth_sentences)
    ^
IndentationError: unexpected indent
>>>  longest_len = max(len(s) for s in macbeth_sentences)
 
  File "<pyshell#46>", line 2
    longest_len = max(len(s) for s in macbeth_sentences)
    ^
IndentationError: unexpected indent
>>> 
KeyboardInterrupt
>>> longest_len = max(len(s) for s in macbeth_sentences)
>>> len(longest_len)

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    len(longest_len)
TypeError: object of type 'int' has no len()
>>> longest_len
158
>>> macbeth_sentences[158]
[u'Rosse', u'.']
>>> [s for s in macbeth_sentences if len(s) == longest_len]
[[u'Doubtfull', u'it', u'stood', u',', u'As', u'two', u'spent', u'Swimmers', u',', u'that', u'doe', u'cling', u'together', u',', u'And', u'choake', u'their', u'Art', u':', u'The', u'mercilesse', u'Macdonwald', u'(', u'Worthie', u'to', u'be', u'a', u'Rebell', u',', u'for', u'to', u'that', u'The', u'multiplying', u'Villanies', u'of', u'Nature', u'Doe', u'swarme', u'vpon', u'him', u')', u'from', u'the', u'Westerne', u'Isles', u'Of', u'Kernes', u'and', u'Gallowgrosses', u'is', u'supply', u"'", u'd', u',', u'And', u'Fortune', u'on', u'his', u'damned', u'Quarry', u'smiling', u',', u'Shew', u"'", u'd', u'like', u'a', u'Rebells', u'Whore', u':', u'but', u'all', u"'", u's', u'too', u'weake', u':', u'For', u'braue', u'Macbeth', u'(', u'well', u'hee', u'deserues', u'that', u'Name', u')', u'Disdayning', u'Fortune', u',', u'with', u'his', u'brandisht', u'Steele', u',', u'Which', u'smoak', u"'", u'd', u'with', u'bloody', u'execution', u'(', u'Like', u'Valours', u'Minion', u')', u'caru', u"'", u'd', u'out', u'his', u'passage', u',', u'Till', u'hee', u'fac', u"'", u'd', u'the', u'Slaue', u':', u'Which', u'neu', u"'", u'r', u'shooke', u'hands', u',', u'nor', u'bad', u'farwell', u'to', u'him', u',', u'Till', u'he', u'vnseam', u"'", u'd', u'him', u'from', u'the', u'Naue', u'toth', u"'", u'Chops', u',', u'And', u'fix', u"'", u'd', u'his', u'Head', u'vpon', u'our', u'Battlements']]
>>> from nltk.corpus import webtext

>>> from nltk.corpus import webtext
>>> for fileid in webtext.fileids():
	print(fileid, webtext.raw(fileid)[:65], '...')

	
(u'firefox.txt', u'Cookie Manager: "Don\'t allow sites that set removed cookies to se', '...')
(u'grail.txt', u'SCENE 1: [wind] [clop clop clop] \nKING ARTHUR: Whoa there!  [clop', '...')
(u'overheard.txt', u'White guy: So, do you have any plans for this evening?\nAsian girl', '...')
(u'pirates.txt', u"PIRATES OF THE CARRIBEAN: DEAD MAN'S CHEST, by Ted Elliott & Terr", '...')
(u'singles.txt', u'25 SEXY MALE, seeks attrac older single lady, for discreet encoun', '...')
(u'wine.txt', u'Lovely delicate, fragrant Rhone wine. Polished leather and strawb', '...')
>>> print(fileid, webtext.raw(fileid)[:70], '...')
(u'wine.txt', u'Lovely delicate, fragrant Rhone wine. Polished leather and strawberrie', '...')
>>> print(fileid, webtext.raw(fileid)[:80], '...')
(u'wine.txt', u'Lovely delicate, fragrant Rhone wine. Polished leather and strawberries. Perhaps', '...')
>>> from nltk.corpus import nps_chat
>>> chatroom=nps_chat.posts('10-19-20s_706posts.xml')
>>> len(chatroom)
706
>>> chatroom[100]
[u'PART']
>>> chatroom[123]
[u'i', u'do', u"n't", u'want', u'hot', u'pics', u'of', u'a', u'female', u',', u'I', u'can', u'look', u'in', u'a', u'mirror', u'.']
>>> from nltk.corpus import brown
>>> news_text = brown.words(categories='news')
>>> fdist = nltk.FreqDist(w.lower() for w in news_text)
>>> modals = ['can', 'could', 'may', 'might', 'must', 'will']
>>> for m in modals:
	print(m + ':', fdist[m], end=' ')
	
SyntaxError: invalid syntax
>>> for m in modals:
	print(m + ':', fdist[m], end=' ')
	
SyntaxError: invalid syntax
>>> for m in modals:
	print(m + ':', fdist[m],' ')

	
('can:', 94, ' ')
('could:', 87, ' ')
('may:', 93, ' ')
('might:', 38, ' ')
('must:', 53, ' ')
('will:', 389, ' ')
>>> 
