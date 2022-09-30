
## Features
- Dicord Interactions Translator
- Optimization
- Easy to use


## Installation

 - Install evg with pip

```
  pip install evg
```
- Set up a new folder /locales
- Add language packs with the file extension.json according to the template /locales/ru/example.json
## Examples
### Base
```python
import evg
_ = evg.MSG(Interaction.locale).msg
print(_("hello"))
```
### Change settings
#### Default language
```python
evg.Setup.language("ru")
```
#### Default text if no translation was found
```python
evg.Setup.text("💕")
```
## Support

For support, [VK](https://vk.com/id441692401); [DISCORD](https://discordapp.com/users/468846682843381760/).

