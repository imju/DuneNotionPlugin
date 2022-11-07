# DuneNotionPlugin
> DuneNotionPlugin is a [Dune API](https://dune.com/) integration with Notion


Like to find out who the big whales are at the moment in notion? This service will find the top whales by the volume by recent data and will populate notion database here for ease of naviation.

![DuneNotion](/assets/DuneNotion_icon.png)

## How to Deploy

OS X & Linux:

```sh
deta deploy
```


### System Architecture
 
![Dune Notion System Flow](/assets/DuneNotionAPI_FlowDiagram.png?raw=true "Dune Notion Architecture")

### Notion page sample

![Whale Tracking Notion Page](/assets/WhaleTracking_NotionPage.png?raw=true "Whale Tracking Notion page sample")

### Whale DB sample

![Whale DB sample](/assets/NotionDB_sample.png?raw=true "Whale DB sample")


## Development setup
1. Clone this repo
2. Download cli based on [this document](https://docs.deta.sh/docs/micros/getting_started)
3. Download [python 3.9](https://www.python.org/downloads/release/python-390/) and follow the installation instruction from the distribution
4. If python3.9 was installed, you can create a virtual env inside of the project
```
python3.9 -m venv "venv"
```
5. Need to login first to deta if not done once
```
deta login
```
6. Deploy the micro to deta cloud
```
deta deploy
```

## Release History

* 0.1
    * CHANGE: Update docs (module code remains unchanged)


## Meta

Contributor: Imju Byon[@imjubyon](https://twitter.com/imjubyon), Alex Duckworth  

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/imju/DuneNotionPlugin](https://github.com/imju/DuneNotionPlugin)

## Contributing

1. Fork it (<https://github.com/imju/DuneNotionPlugin>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

