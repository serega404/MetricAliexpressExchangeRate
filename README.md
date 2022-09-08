# MetricAliexpressExchangeRate

[![MIT License](https://img.shields.io/github/license/serega404/EasyESPRealy)](https://github.com/serega404/MetricAliexpressExchangeRate)

Экспортер курса Aliexpress и ЦБ РФ

Для сбора метрик я использую [Victoria Metric](https://github.com/VictoriaMetrics/VictoriaMetrics) в режиме CSV

Особая благадарность сайту cbr-xml-daily.ru за предоставление данных с сайта cbr.ru

### Запуск через Cron

``` Cron
*/10 * * * * python3 /home/bots/KursExporter/main.py
```

### Отображение в Grafana

Файл для импорта: [grafana.json](./grafana.json)
<img src="./grafana.png" width="400" height="300" />

### Библиотеки

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

### Лицензия

Распространяется под MIT License. Смотри файл [`LICENSE`](./LICENSE) для того что бы узнать подробности.
