### Docker

You can mapping the ports whatever you want. The most important thing about github-trending-crawler port mapping is that github-trending-crawler runs on `5000 HTTP` port. You must consider this during configure your mapping.

- With CLI

```bash
docker run -d -p 5000:5000 enesusta/kur:0109202
```

- With docker-compose

Let's look at this sample.

`docker-compose.yml`

```yml
version: '3'

services:
  kur:
    container_name: kur
    image: enesusta/kur:0109202
    ports:
    - 5000:5000
```

Then:

```bash
docker-compose up -d
```

Sample Response

```json
[
  {
    "change": "-5,12",
    "name": "GRAM ALTIN",
    "value": "995,65"
  },
  {
    "change": "0,0244",
    "name": "DOLAR",
    "value": "18,2093"
  },
  {
    "change": "-0,0339",
    "name": "EURO",
    "value": "18,2630"
  },
  {
    "change": "-0,0271",
    "name": "STERLİN",
    "value": "21,1205"
  },
  {
    "change": "-2,93",
    "name": "BIST 100",
    "value": "3.168,28"
  },
  {
    "change": "-$283,88",
    "name": "BITCOIN",
    "value": "$20.066,04"
  },
  {
    "change": "-0,13",
    "name": "GÜMÜŞ",
    "value": "10,39"
  },
  {
    "change": "0,02",
    "name": "FAİZ",
    "value": "14,60"
  }
]
```