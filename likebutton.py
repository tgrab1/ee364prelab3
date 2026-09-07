posts = {
    1: {
        "message": "Hello world!",
        "likes": 0
    }
}


def like_post(post_id):
    if post_id in posts:
        posts[post_id]["likes"] += 1
        print(f"Post {post_id} now has {posts[post_id]['likes']} likes.")
    else:
        print("Post not found.")


def main():
    print("Before like:", posts[1]["likes"])
    like_post(1)
    print("After like:", posts[1]["likes"])


if __name__ == "__main__":
    main()