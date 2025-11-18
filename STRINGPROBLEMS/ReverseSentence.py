s = "Hello world from Python"

WordSplitter = s.split()
ReverseOfWordSplitter = WordSplitter[::-1]
Joiner = " ".join(ReverseOfWordSplitter)
print(Joiner)