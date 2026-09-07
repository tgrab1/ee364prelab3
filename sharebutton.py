posts = {
    1: {
        "message": "Check out my new post!",
        "shares": 0
    }
}


def share_post(post_id):
    if post_id in posts:
        posts[post_id]["shares"] += 1
        print(f"Post {post_id} has been shared.")
        print(f"Total shares: {posts[post_id]['shares']}")
    else:
        print("Post not found.")


def main():
    print("Before share:", posts[1]["shares"])
    share_post(1)
    print("After share:", posts[1]["shares"])


if __name__ == "__main__":
    main()