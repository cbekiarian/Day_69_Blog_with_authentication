from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField




# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
class CommentForm(FlaskForm):
    comment = CKEditorField("comment", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
class RegisterForm(FlaskForm):
    email = EmailField(label="email", validators=[DataRequired()])
    password = StringField(label="password", validators=[DataRequired()])
    name = StringField(label="name", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
# TODO: Create a RegisterForm to register new users


# TODO: Create a LoginForm to login existing users


# TODO: Create a CommentForm so users can leave comments below posts
