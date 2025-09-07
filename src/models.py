from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    firstname: Mapped[str] = mapped_column()
    lastname: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()

    comment = db.relationship('Comment')
    post = db.relationship('Post')
    followers = db.relationship('Follower', foreign_keys='[Follower.user_to_id]', back_populates="followed") 
    following = db.relationship('Follower', foreign_keys='[Follower.user_from_id]', back_populates="follower")  

    #aqui debo poner la relacion dos veces para que sea muchos a muchos 
    
class Follower(db.Model):
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)

    follower: Mapped['User'] = relationship('User', foreign_keys=[user_from_id], back_populates="following")
    followed: Mapped['User'] = relationship('User', foreign_keys=[user_to_id], back_populates="followers")

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    media = db.relationship('Media')

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)