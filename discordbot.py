import gspread
from oauth2client.service_account import ServiceAccountCredentials
import discord
from discord.ext import commands
import string

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

json_file_name = 'preleague-schedule-36c22ff31a0c.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/11WmMV2-YIHG0K02V510lJVm1yTUDsbOY5geriLN8Oas/edit#gid=0'

doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet('시트1')

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='match')
async def print_data(ctx):
    cell_data = worksheet.range('A1:F10')
    output = ''
    for i, cell in enumerate(cell_data):
        if i % 6 == 0 and i != 0:
            output += '\n'
        my_string = str(cell.value)
        output += f'{my_string.ljust(15)} '
    await ctx.send(f'```\n{output}\n```')

bot.run('MTA5NjU4MTk5MTc5MDU1MTA5MA.GHXviO.1kb2mMxC5VAPT4-1-Zl8fhuhVbDF1bVyyWYbQ4')
