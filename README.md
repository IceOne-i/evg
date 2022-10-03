
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
### File - locales/ru/example.json
```json
{
    "hello1": "Hello world!",
    "hello2": "Hello {name}!"
}
```
### Base
```python
import evg
_ = evg.MSG(Interaction.locale).msg
print(_("hello1"))
```
* Output: Hello world!
OR
```python
import evg
from nextcord import Interaction, PartialInteractionMessage
async def hi(ctx: Interaction) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(text=_("hello1"))
```
* Output: Hello Nik!
### Kwargs
```python
import evg
import asyncio
from nextcord import Interaction, PartialInteractionMessage
async def hi(ctx: Interaction, **kwargs) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(text=_("hello2", **kwargs))
asyncio.run(hi(ctx, name="Nik"))
```
* Output: Hello Nik!
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

