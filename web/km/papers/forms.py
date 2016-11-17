from django import forms

class SearchPapers(forms.Form):
	title_search = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class' : 'input-group'}))
	author_search = forms.CharField()
	MISQ = forms.BooleanField()
	ISR = forms.BooleanField()
	JMIS = forms.BooleanField()
	JAIS = forms.BooleanField()
	JSIS = forms.BooleanField()
	ISJ = forms.BooleanField()
	JIT = forms.BooleanField()
	EJIS = forms.BooleanField()
