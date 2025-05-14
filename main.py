import interactions, random, os, asyncio, urllib
from time import sleep

bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

@interactions.slash_command(name="take_a_bird", description="Get a random bird!")
async def take_a_bird_function(ctx: interactions.SlashContext):
    await ctx.defer()

    while True:
        try:
            number = random.randrange(1, 635780000)
            test = urllib.request.urlopen("https://macaulaylibrary.org/asset/%s/embed" % f'{number:09}')
            if test.status == 200:
                print("Found %s" % f'{number:09}')
                break
            else:
                await sleep(2)
        except urllib.error.HTTPError as e:
            print(f"An HTTP error occurred: {e.code}")
        except urllib.error.URLError as e:
            print(f"An URL error occurred: {e.reason}")
            
    await ctx.send("https://macaulaylibrary.org/asset/%s" % f"{number:09}")

bot.start(os.environ["BIRD_TOKEN"])