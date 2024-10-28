from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  # 使用 Textarea 小部件来渲染这个字段，以便用户可以在一个较大的文本框中输入内容，而不仅仅是一行文本
  message = forms.CharField(widget=forms.Textarea)

  # 定义了如何处理表单提交后发送电子邮件的逻辑
  def send_email(self):
    print(f"Sending email from {self.cleaned_data["email"]} with message: {self.cleaned_data["message"]}")
