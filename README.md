Following John Cricket code challenge. Original post is on [LinkedIn](https://www.linkedin.com/pulse/coding-challenge-1-john-crickett%3FtrackingId=dE0jIZinRmmvvWUXWih5JQ%253D%253D/?trackingId=dE0jIZinRmmvvWUXWih5JQ%3D%3D)

---
Pipenv is used for virtual env. To install requirements do following
```
pipenv install
```
To run tests
```
pytest -v tests.py
```
To run system
```
python ccwc.py test.txt
python ccwc.py -<flag> test.txt
cat test.txt | python ccwc.py
cat test.txt | python ccwc.py -<flag>
```

flags are the same as for linux `wc` utility. Check manpage
```
man wc
```