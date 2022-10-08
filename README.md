# Food Brain
A culinary student's dream! This is a Flash Card game made in python that scrapes and displays cooking terms and their meanings from [The Scramble](https://www.thescramble.com/glossary-of-cooking-terms/) through [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#) to help the user learn and memorize them.
At the end of each session, it sends the user a summary - the words they learnt and the number of words they are yet to go through, by an SMS sent with [Twilio](https://www.twilio.com/).  

## Screenshots 
![term_ss](https://user-images.githubusercontent.com/87208681/194726706-77636710-92b8-45d2-98ff-f8f0c894ebb5.jpg)
![desc_ss](https://user-images.githubusercontent.com/87208681/194726693-99ef38bd-b19a-4130-8aa0-60494c261c32.png)


## API
[kanye.rest](https://kanye.rest/)

## Data Source

## Tools

## Run Locally

Clone the project

```bash
  git clone https://github.com/sejalabrol/kanye-quotes-app
```

Go to the project directory

```bash
  cd kanye-quotes-app
```

[Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) (optional but recommended) 
```bash
  python -m venv venv
  source venv/Scripts/activate
```
Install dependencies
```bash
  pip install -r requirements.txt
```

Run the script

```bash
  python main.py
```
