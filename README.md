
## Features
- Dicord interactions translator
- Optimization
- Easy to use


## Installation

 - Install evg with pip

```
  pip install evg
```
- Set up a new folder /locales
- Add language packs with the file extension ".json" according to the template /locales/en-US/example.json
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
* <b>Output text</b>:  Hello world!
 
OR
```python
import evg
from nextcord import Interaction, PartialInteractionMessage
async def hi(ctx: Interaction) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(content=_("hello1"))
```
* <b>Output text</b>:  Hello world!
 
OR
```python
import evg
from nextcord import Interaction, PartialInteractionMessage

async def hi(ctx: Interaction) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(content=(_("hello2")).format(name="Nikita"))

async def hi2(ctx: Interaction) -> PartialInteractionMessage:
    _ = evg.MSG(ctx.locale).msg
    return await ctx.send(content=(_("hello3")).format("Bob"))
```
<b>Output text</b>: 
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

[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/468846682843381760/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nikitabelan@gmail.com)

