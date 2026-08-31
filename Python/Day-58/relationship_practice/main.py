"""
Day 58 relationship practice - exercising relationship()/back_populates
on a plain User <-> Post one-to-many link.

Run:
    python main.py

Practice covered:
    1. Create a user.
    2. Create multiple posts.
    3. Associate the posts with that user.
    4. Retrieve the user.
    5. Retrieve their posts (user.posts).
    6. Retrieve the author of a post (post.author).
"""

from database import Base, SessionLocal, engine
from models import Post, User

# Create the users/posts tables on startup if they don't already exist.
Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # 1. Create a user.
    user = User(name="Adarsh", email="adarsh@example.com")
    db.add(user)
    db.commit()
    db.refresh(user)

    # 2 & 3. Create multiple posts and associate them with that user
    # (setting user_id directly - either this or user.posts.append(...)
    # would work, since both sides of the relationship stay in sync).
    post1 = Post(title="First Post", content="Hello, world!", user_id=user.id)
    post2 = Post(title="Second Post", content="Learning SQLAlchemy.", user_id=user.id)
    post3 = Post(title="Third Post", content="One-to-many relationships.", user_id=user.id)
    db.add_all([post1, post2, post3])
    db.commit()

    # 4. Retrieve the user.
    fetched_user = db.query(User).filter(User.name == "Adarsh").first()
    print(f"User: {fetched_user.name} ({fetched_user.email})")

    # 5. Retrieve their posts via the relationship - no manual query.
    print("Posts:")
    for post in fetched_user.posts:
        print(f"  - {post.title}: {post.content}")

    # 6. Retrieve the author of a post via the relationship.
    fetched_post = db.query(Post).filter(Post.title == "First Post").first()
    print(f"Author of '{fetched_post.title}': {fetched_post.author.name}")

finally:
    db.close()
