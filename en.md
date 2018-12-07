# Bitly url shorterer

This program converts long links to short bit.ly links and prints it out  
with total clicks of this link in a month  
If link is already bit.ly short link - it returns only total clicks

### How to install



You must get your own token from bit.ly site and put it in .env file in root directory

Example
```text
TOKEN=e12e1e12312ewdqadqe1231231er23t
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Run Example

Go to project directory and run from cmd :

```
D:\python_proj\bitly_shorter>python main.py -l http://google.ru
bit.ly/2St2pmr
Количество кликов на битли: 1

```
With short bit.ly link:
```
D:\python_proj\bitly_shorter>python main.py -l bit.ly/2St2pmr
Количество кликов на битли: 1

```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).