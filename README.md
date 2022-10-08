# Food Brain
A culinary student's dream! This is a Flash Card game made in python that scrapes and displays cooking terms and their meanings from [The Scramble](https://www.thescramble.com/glossary-of-cooking-terms/) through [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#) to help the user learn and memorize them.
At the end of each session, it sends the user a summary - the words they learnt and the number of words they are yet to go through, by an SMS sent with [Twilio](https://www.twilio.com/).  
![thumbnail](https://user-images.githubusercontent.com/87208681/194730058-07c6fcd8-86b8-472d-85ce-4bf1e0de7879.png)


## Screenshots 
![term_ss](https://user-images.githubusercontent.com/87208681/194726706-77636710-92b8-45d2-98ff-f8f0c894ebb5.jpg)
![desc_ss](https://user-images.githubusercontent.com/87208681/194726693-99ef38bd-b19a-4130-8aa0-60494c261c32.png)
![message_screenshot](https://user-images.githubusercontent.com/87208681/194730045-f49ac1b7-2139-4c58-8551-c62c902ea275.jpeg)


## API
[Twilio](https://www.twilio.com/)

## Data Source
[The Scramble](https://www.thescramble.com/glossary-of-cooking-terms/)

## Tools
[Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#)

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

`TWILIO_ACCOUNT_SID` `TWILIO_AUTH_TOKEN` `SENDERS_NUMBER` `RECEIVERS_NUMBER`

Refer to the [env template](https://github.com/sejalabrol/foodbrain/blob/main/.env.template)

## Run Locally

Clone the project

```bash
  git clone https://github.com/sejalabrol/foodbrain
```

Go to the project directory

```bash
  cd foodbrain
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
Create a .env file and enter environment variables
```bash
  cp .env.template .env
```

Run the script

```bash
  python main.py
```
