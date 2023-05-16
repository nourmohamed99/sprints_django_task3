from django import forms
from .models import Student
from django.forms import ModelForm
# from formValidationApp.models import *

#creating a form
class InputForm(forms.Form):
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
		help_text = "Enter 6 digit roll number"
		)
	password = forms.CharField(widget = forms.PasswordInput())



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields="__all__"	


# # define the class of a form
# class PostForm(ModelForm):
#     class Meta:
#         # write the name of models for which the form is made
#         model = Post       
 
#         # Custom fields
#         fields =["username", "gender", "text"]
 
#     # this function will be used for the validation
#     def clean(self):
 
#         # data from the form is fetched using super function
#         super(PostForm, self).clean()
         
#         # extract the username and text field from the data
#         username = self.cleaned_data.get('username')
#         text = self.cleaned_data.get('text')
 
#         # conditions to be met for the username length
#         if len(username) < 5:
#             self._errors['username'] = self.error_class([
#                 'Minimum 5 characters required'])
#         if len(text) <10:
#             self._errors['text'] = self.error_class([
#                 'Post Should Contain a minimum of 10 characters'])
 
#         # return any errors if found
#         return self.cleaned_data        


###################################

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields =["username", "gender", "text"]
# 	def clean(self): 
# 		super(PostForm, self).clean()
# 		username = self.cleaned_data.get('username')
# 		text = self.cleaned_data.get('text')
# 		if len(username) <5:
# 			self._errors['username'] = self.error_class([
# 				'minimum 5 characters required'])
# 		if len(text) <10: 
# 			self._errors['text'] = self.error_class([
# 				'minimum 10 characters'])
# 		return self.cleaned_data	






	





        

	

	        	


        		        