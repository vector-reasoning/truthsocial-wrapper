import asyncio
import json
from typing import NoReturn
from truthsocial import Api

from datetime import datetime

TRUTHSOCIAL_USERNAME = "newsalpha"
TRUTHSOCIAL_PASSWORD = "98%IQSquad"


async def main() -> NoReturn:

    api = Api(username=TRUTHSOCIAL_USERNAME, password=TRUTHSOCIAL_PASSWORD)
    already_seen_id_set = set()

    #first run to fill the post set
    posts = api.pull_statuses("realDonaldTrump")
    count = 25
    for post in posts:
        print(post)
        post_id = str(post.get('id', ''))
        already_seen_id_set.add(post_id)
        count -= 1
        if count == 0:
            break
    await asyncio.sleep(1)

    while True:
        try:
            print(f"Fetching new realDonaldTrump posts...")
            posts = api.pull_statuses("realDonaldTrump")
            for post in posts:
                post_id = str(post.get('id'))
                if not post_id:
                    print("problem with post_id " + str(post))
                    continue
                if post_id in already_seen_id_set:
                    break
                already_seen_id_set.add(post_id)
                post_json = json.dumps(post)

                print(f"Added new post to queue: {post}")

            print("sleeping for " + str(1) + " seconds")

        except Exception as e:
            print(f"Error processing Truth Social posts: {e}")
            await asyncio.sleep(60)  # Wait a minute before retrying on error


if __name__ == "__main__":
    asyncio.run(main())