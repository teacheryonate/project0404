from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class QuestionForm(FlaskForm):
    subject = StringField("제목", validators=[DataRequired("제목은 필수 입력 항목입니다.")])
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수 입력 항목입니다.")])
    user_id = StringField("작성자", validators=[DataRequired("로그인 후 사용하세요")])


class AnswerForm(FlaskForm):
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수 입력 항목입니다.")])
    user_id = StringField("작성자", validators=[DataRequired("로그인 후 사용하세요")])



class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=20)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo("password2", "비밀번호가 일치하지 않음")])
    password2 = PasswordField("비밀번호확인", validators=[DataRequired()])
    email = EmailField("이메일", validators=[DataRequired(), Email()])



class UserLoginForm(FlaskForm):
    username = StringField("사용자이름", validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
