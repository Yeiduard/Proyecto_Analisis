from wtforms import Form
from wtforms import FloatField
from wtforms import validators



class CommentForm(Form):
    valor1=FloatField('Valor 1',
    [
        validators.required(message="se requiere un valor"),
    
        validators.length(min=1,max=100, message= "ingrese un valor numerico ")
    ]
    )
    valor2=FloatField('Valor 2')
    