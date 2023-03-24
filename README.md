Following John Crickett code challenge. Original post is on [LinkedIn](https://www.linkedin.com/pulse/coding-challenge-1-john-crickett%3FtrackingId=dE0jIZinRmmvvWUXWih5JQ%253D%253D/?trackingId=dE0jIZinRmmvvWUXWih5JQ%3D%3D)

---
Pipenv is used for virtual env. To install requirements do following
```
pipenv install
```
To run tests
```
pytest -v tests.py
```

To make a terminal tool we use setuptools
```
pip install --editable .
```

To run system
```
ccwc test.txt
ccwc.py -<flag> test.txt
cat test.txt | ccwc.py
cat test.txt | ccwc.py -<flag>
```

flags are the same as for linux `wc` utility. Check manpage
```
man wc
```

