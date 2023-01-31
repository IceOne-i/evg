
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
- Add language packs with the file <extension>.json according to the template /locales/en-US/<example>.json
## Examples
### File - locales/en-US/example.json
```json
{
    "hello1": "Hello world!",
    "hello2": "Hello {name}!",
    "hello3": "Hello {0}!"
}
```
### Base
```python
import evg
_ = evg.MSG("en-US").msg
print(_("hello1"))
```
* Output text: Hello world!
 
OR
```python
import evg
from nextcord import Interaction, PartialInteractionMessage
async def hi(ctx: Interaction) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(text=_("hello1"))
```
* Output text: Hello world!
 
OR
```python
import evg
from nextcord import Interaction, PartialInteractionMessage
async def hi(ctx: Interaction) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(text=(_("hello2")).format(name="Nikita"))

async def hi2(ctx: Interaction) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(text=(_("hello3")).format("Bob"))
```
Output text: 
* Hello Nikita!
* Hello Bob!

### Change settings
#### Default language
```python
evg.Setup.language("en-US")
```
#### Default text if no translation was found
```python
evg.Setup.text("💕")
```
## Support

For support, [VK](https://vk.com/id441692401); [DISCORD](https://discordapp.com/users/468846682843381760/).

