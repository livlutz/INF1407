from django import forms


#link sobre formulários: https://docs.djangoproject.com/en/5.2/ref/forms/fields/#built-in-field-classes

class ExemploForm(forms.Form):

    campoBooleanField = forms.BooleanField(
        required=False,
        label_suffix="*: ",
        label="Campo booleano",
        initial=False,
        help_text="Marque se for verdadeiro",
        widget=forms.CheckboxInput(attrs={'class': 'classe-booleana'}),
    )

    campoTexto = forms.CharField(
        required=True,
        label="Campo charfield *",
        label_suffix="* ",
        initial="Texto inicial",
        help_text="Digite um texto de até 100 caracteres",
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'classeTexto',
                    'placeholder': 'Digite algo aqui'}),
    )

    campoTelefone = forms.CharField(
        required=True,
        label_suffix="*: ",
        label="Campo telefone",
        help_text="Digite um número de telefone no formato (XX)XXXX-XXXX",
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'classe-telefone', 'placeholder': '(XX)XXXXX-XXXX', 'pattern': r'\(\d{3}\)\d{3,4}-\d{4}'}),
    )

    campoChoiceField = forms.ChoiceField(
        required=True,
        label_suffix="*: ",
        label="Campo choicefield",
        choices=[('opcao1', 'Opção 1'), ('opcao2', 'Opção 2'), ('opcao3', 'Opção 3'), ('opcao4', 'Opção 4'), ('opcao5', 'Opção 5')],
        help_text="Escolha uma das opções",
        initial='opcao3', #opção 3 previamente selecionada
        widget=forms.Select(attrs={'class': 'classe-choiceField'}),
    )

    campoDateField = forms.DateField(
        required=True,
        label_suffix="*: ",
        label="Campo datefield",
        help_text="Selecione uma data",
        initial = '2024-01-01T12:00',
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],  #formatos aceitos
        widget=forms.DateInput(attrs={'class': 'classe-datefield', 'type': 'date'}),
    )

    campoDateTimeField = forms.DateTimeField(
        required=True,
        label_suffix="*: ",
        label="Campo datetimefield",
        help_text="Selecione uma data e hora",
        initial = '2024-01-01T12:00',
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateTimeInput(attrs={'class': 'classe-datetimefield', 'type': 'datetime-local'}),
    )

    campoDecimalField = forms.DecimalField(
        required=True,
        label_suffix="*: ",
        label="Campo decimalfield",
        help_text="Digite um número decimal (ex: 10.50)",
        max_digits=10,
        decimal_places=2,
        initial=0.00,
        widget=forms.NumberInput(attrs={'class': 'classe-decimalfield', 'step': '0.01'}),
    )

    campoIntegerField = forms.IntegerField(
        required=True,
        label_suffix="*: ",
        label="Campo integerfield",
        help_text="Digite um número inteiro",
        initial=0,
        widget=forms.NumberInput(attrs={'class': 'classe-integerfield', 'step': '1'}),
    )

    campoGenericIPAddressField = forms.GenericIPAddressField(
        required=True,
        label_suffix="*: ",
        label="Campo genericipaddressfield",
        help_text="Digite um endereço IP (IPv4 ou IPv6)",
        initial='192.168.0.1',
        widget=forms.TextInput(attrs={'class': 'classe-genericipaddressfield', 'placeholder': 'Digite um IP aqui'}),
    )

    campoMultipleChoiceField = forms.MultipleChoiceField(
        required=True,
        label_suffix="*: ",
        label="Campo multiplechoicefield",
        choices=[('opcao1', 'Opção 1'), ('opcao2', 'Opção 2'), ('opcao3', 'Opção 3'), ('opcao4', 'Opção 4'), ('opcao5', 'Opção 5')],
        help_text="Escolha uma ou mais opções (use Ctrl ou Shift para múltipla seleção)",
        initial=['opcao2', 'opcao4'], #opção 2 e 4 previamente selecionadas
        widget=forms.Select(attrs={'class': 'classe-multiplechoicefield', 'multiple': 'multiple'}),
    )

    campoColorField = forms.CharField(
        required=True,
        label_suffix="*: ",
        label="Campo colorfield",
        help_text="Selecione uma cor",
        initial='#ff0000',
        widget=forms.TextInput(attrs={'class': 'classe-colorfield', 'type': 'color'}),
    )
