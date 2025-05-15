import interactions, random, os, asyncio, urllib
from time import sleep

bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

@interactions.slash_command(name="take_a_bird", description="Get a random bird!")
async def take_a_bird_function(ctx: interactions.SlashContext):
    await ctx.defer()

    attempts = 0

    while True:
        try:
            number = random.randrange(1, 635780000)
            test = urllib.request.urlopen("https://macaulaylibrary.org/asset/%s/embed" % f'{number:09}')
            if test.status == 200:
                print("Found {} after {} attempts".format(f'{number:09}', attempts))
                break
            else:
                sleep(1)
        except urllib.error.HTTPError as e:
            attempts += 1
            sleep(1)
            #print(f"An HTTP error occurred: {e.code}")
        except urllib.error.URLError as e:
            print(f"An URL error occurred: {e.reason}")
            sleep(1)
            
    await ctx.send("https://macaulaylibrary.org/asset/%s" % f"{number:09}")

bot.start(os.environ["BIRD_TOKEN"])